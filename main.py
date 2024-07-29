import sys

from PyQt5.QtWidgets import QApplication

from ui_functionPage.FunctionPageParts import FunctionPage

if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = FunctionPage()
    w.setUsername('czx')
    w.show()

    app.exec_()
