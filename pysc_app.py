from PySide.QtGui import *

from ui.windows import *
from ui.tools import *


class PyscApp(QApplication):

    def __init__(self):
        super(PyscApp, self).__init__([])

    def run(self):
        w = Window()
        w.show()
        w.resize(600, 600)
        move_center(w)
        self.exec_()

if __name__ == '__main__':
    PyscApp().run()
