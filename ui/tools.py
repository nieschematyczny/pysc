from PySide.QtGui import *


def move_center(window):
    ctr = QDesktopWidget().availableGeometry().center()
    geom = window.frameGeometry()
    geom.moveCenter(ctr)
    window.move(geom.topLeft())
