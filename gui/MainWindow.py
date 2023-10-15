import sys
from datetime import datetime

from PIL.Image import Image
from PIL.ImageQt import ImageQt
from PySide6.QtCore import QEvent, Qt, QDate
from PySide6.QtGui import QPixmap, QMouseEvent
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog

from Classes.CelestialBody import CelestialBody, Star, Planet
from Classes.Game import Game
from Classes.SolarSystem import CelestialBSystem, StarSystem
from graphics.FrameDrawer import Frame
from gui.MapTooltip import MapTooltip
from gui.mainwindow_ui import Ui_MainWindow
from gui.filesave_dialog_ui import FileSaveDialog
from gui.new_game_dialog_ui import NewGameDialog


class MainWindow(QMainWindow):
    is_ready = False
    current_system: CelestialBSystem | None = None
    loaded_game: Game

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.centralwidget.installEventFilter(self)
        self.ui.lblDisplay.installEventFilter(self)
        self.ui.btnSave.clicked.connect(self.save_game)
        self.ui.btnNewGame.clicked.connect(self.new_game)

    def display(self, app: QApplication):
        self.showMaximized()
        self.is_ready = True
        sys.exit(app.exec())

    def update_frame_image(self):
        if self.current_system is not None:
            frame = Frame()
            self.current_system: StarSystem
            img = frame.draw(self.current_system, self.get_display_size())
            lbl = self.ui.lblDisplay
            lbl.setPixmap(QPixmap.fromImage(ImageQt(img)))
            lbl.setScaledContents(True)


    def get_display_size(self) -> tuple[int, int]:
        lbl = self.ui.lblDisplay
        return lbl.width(), lbl.height()

    def eventFilter(self, watched, event):
        if watched == self.ui.lblDisplay:
            if event.type() == QEvent.MouseButtonPress:
                press_event = QMouseEvent(event)
                obj = self.parse_map_object(press_event.pos().toTuple())
                if obj is not None:
                    self.display_map_tooltip(obj)

                return True
            else:
                return False

        elif watched == self.ui.centralwidget:
            if event.type() == QEvent.Resize:
                if self.current_system is not None:
                    frame = Frame()
                    self.current_system: StarSystem
                    self.update_frame_image()

                return True
            else:
                return False
        else:
            return QMainWindow.eventFilter(self, watched, event)

    def parse_map_object(self, xy: tuple[int, int]) -> CelestialBody | None:
        if self.current_system is None:
            raise ValueError

        # Transform the coordinates
        transform = self.get_display_size()
        click_xy = xy[0] - transform[0] // 2, xy[1] - transform[1] // 2
        objects: list[CelestialBody] = self.current_system.orbiting_bodies.copy()
        objects.append(self.current_system.host_body)
        for object in objects:
            if abs(click_xy[0] - object.x * .001) <= max(object.radius * 20, 20):
                if abs(click_xy[1] - object.y * .001) <= max(object.radius * 20, 20):
                    return object
        return None

    def display_map_tooltip(self, obj):
        tooltip = MapTooltip()

        tooltip.ui.lblTitle.setText(obj.name)

        tooltip.ui.listWidget.addItem(f"Mass: {obj.mass * 10 ** 12:.2e} kg")
        tooltip.ui.listWidget.addItem(f"Radius: {obj.radius * 10 ** 6:.2e} m")
        tooltip.ui.listWidget.addItem(f"Temperature: {obj.temperature:.2e} K")

        if isinstance(obj, Star):
            obj: Star
            tooltip.ui.listWidget.insertItem(0, f"Object type: Star, {obj.star_class.verboseName}")
            tooltip.ui.listWidget.addItem(f"Luminosity: {obj.luminosity * 10 ** 12:.2e} Wt")
            tooltip.ui.listWidget.addItem(f"Color: {obj.star_class.color}")

        elif isinstance(obj, Planet):
            obj: Planet
            tooltip.ui.listWidget.insertItem(0, f"Object type: Planet, {obj.type.verboseName}")
            tooltip.ui.listWidget.addItem(f"Orbit radius: {obj.orbital_radius * 10 ** 6:.2e} m")
            tooltip.ui.listWidget.addItem(f"Orbital period: {obj.orbital_period} yr")

        self.ui.vloSideMenu.insertWidget(0, tooltip, alignment=Qt.AlignTop)

    def save_game(self):
        def accept_save(filename):
            pass

        qd = QDialog(self.ui.centralwidget)
        qd.ui = FileSaveDialog()
        qd.ui.setupUi(qd)

        qd.accepted.connect(lambda: accept_save(qd.ui.lineEdit.text()))
        qd.exec_()

    def new_game(self):
        def create_new_game(empire_name: str, home_sys_name: str, starting_date: QDate):
            starting_date = datetime(
                starting_date.year(), starting_date.month(), starting_date.day()
            )
            self.loaded_game = Game()
            self.loaded_game.new(
                current_date=starting_date,
                empire_name=empire_name,
                capital_name=home_sys_name
            )
            self.setWindowTitle(f"{self.loaded_game.empire_name} - Not saved")
            self.current_system = self.loaded_game.capital
            self.update_frame_image()

        qd = QDialog(self.ui.centralwidget)
        qd.ui = NewGameDialog()
        qd.ui.setupUi(qd)
        qd.accepted.connect(lambda: create_new_game(
            empire_name=qd.ui.ledEmpireName.text(),
            home_sys_name=qd.ui.ledHomeName.text(),
            starting_date=qd.ui.dateEdit.date()
        ))
        qd.exec_()
