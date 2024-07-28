import sys

from PyQt5.QtWidgets import QApplication

from ui.FunctionPageParts import FunctionPage

if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = FunctionPage("czx")
    w.show()

    app.exec_()
