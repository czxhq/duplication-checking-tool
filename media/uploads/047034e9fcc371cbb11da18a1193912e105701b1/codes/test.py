import sys

from PyQt5.QtWidgets import QApplication

from ui.Logined_in_window import Logined_in_window
from ui_rqh.FunctionPageParts import FunctionPage

if __name__ == '__main__':
    app = QApplication(sys.argv)
    function = FunctionPage('czx')
    function.fileToResult('C:/Users/Leon/PycharmProjects/Front_endian/Compare.zip')
    app.exec_()
print('done')