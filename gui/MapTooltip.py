from PySide6.QtWidgets import QWidget

from gui.maptooltip_ui import Ui_MapTooltip


class MapTooltip(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MapTooltip()
        self.ui.setupUi(self)
