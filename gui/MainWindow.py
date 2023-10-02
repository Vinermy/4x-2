import sys

from PIL.Image import Image
from PIL.ImageQt import ImageQt
from PySide6.QtGui import QImage, QPixmap, QResizeEvent, QScreen
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication, QWidget, QLabel
from PySide6.QtCore import QFile, QIODevice, QSize


class MainWindow:
    ui_file_path: str
    window: QWidget
    is_loaded: bool = False

    def __init__(self, ui_file_path: str):
        self.ui_file_path = ui_file_path

    def display(self):
        app = QApplication(sys.argv)

        ui_file = QFile(self.ui_file_path)
        if not ui_file.open(QIODevice.ReadOnly):
            print(f"Cannot open {self.ui_file_path}: {ui_file.errorString()}")
            sys.exit(-1)
        loader = QUiLoader()
        self.window = loader.load(ui_file)
        ui_file.close()
        if not self.window:
            print(loader.errorString())
            sys.exit(-1)

        self.window.showMaximized()
        self.is_loaded = True

        sys.exit(app.exec())

    def update_frame_image(self, img: Image):
        lbl: QLabel | object = self.window.findChild(QLabel, "lblDisplay")
        lbl.setPixmap(QPixmap.fromImage(ImageQt(img)), )
        lbl.setScaledContents(True)

    def get_display_size(self) -> list[int, int]:
        lbl: QLabel | object = self.window.findChild(QLabel, "lblDisplay")
        return [lbl.width(), lbl.height()]
