import sys
from PyQt5.QtWidgets import QApplication

from window.My_login_and_signup_window import My_login_and_signup_window

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = My_login_and_signup_window()
    w.show()
    sys.exit(app.exec_())