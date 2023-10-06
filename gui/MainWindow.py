import sys

from PIL.Image import Image
from PIL.ImageQt import ImageQt
from PySide6.QtCore import QEvent, Qt
from PySide6.QtGui import QPixmap, QMouseEvent
from PySide6.QtWidgets import QApplication, QMainWindow

from Classes.CelestialBody import CelestialBody, Star, Planet
from Classes.SolarSystem import CelestialBSystem, StarSystem
from graphics.FrameDrawer import Frame
from gui.MapTooltip import MapTooltip
from gui.mainwindow_ui import Ui_MainWindow


class MainWindow(QMainWindow):
    is_ready = False
    current_system: CelestialBSystem | None = None

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.centralwidget.installEventFilter(self)
        self.ui.lblDisplay.installEventFilter(self)

    def display(self, app: QApplication):
        self.showMaximized()
        self.is_ready = True
        sys.exit(app.exec())

    def update_frame_image(self, img: Image, system: CelestialBSystem | None):
        lbl = self.ui.lblDisplay
        lbl.setPixmap(QPixmap.fromImage(ImageQt(img)))
        lbl.setScaledContents(True)
        if system is not None:
            self.current_system = system

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
                    self.update_frame_image(frame.draw(self.current_system, self.get_display_size()),
                                            self.current_system)

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
        tooltip.ui.listWidget.addItem(f"Radius: {obj.radius * 10 * 6:.2e} m")
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
