from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Login_and_signup_window(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(958, 677)
        font = QFont()
        font.setPointSize(10)
        Form.setFont(font)
        self.gridLayout_2 = QGridLayout(Form)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.tabWidget = QTabWidget(Form)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setStyleSheet(u"QTabBar::tab{width:0}\n"
                                     "QTabBar::tab{height:0}\n"
                                     "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout = QGridLayout(self.tab)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.random_dialog = QLabel(self.tab)
        self.random_dialog.setObjectName(u"random_dialog")
        font1 = QFont()
        font1.setPointSize(14)
        self.random_dialog.setFont(font1)
        self.random_dialog.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.verticalLayout_6.addWidget(self.random_dialog)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_2 = QLabel(self.tab)
        self.label_2.setObjectName(u"label_2")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font2 = QFont()
        font2.setPointSize(30)
        font2.setBold(False)
        font2.setWeight(50)
        font2.setStrikeOut(False)
        self.label_2.setFont(font2)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_2)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_5)

        self.label_3 = QLabel(self.tab)
        self.label_3.setObjectName(u"label_3")
        font3 = QFont()
        font3.setPointSize(20)
        self.label_3.setFont(font3)

        self.horizontalLayout_6.addWidget(self.label_3)

        self.input_username_in_login = QLineEdit(self.tab)
        self.input_username_in_login.setObjectName(u"input_username_in_login")
        sizePolicy.setHeightForWidth(self.input_username_in_login.sizePolicy().hasHeightForWidth())
        self.input_username_in_login.setSizePolicy(sizePolicy)
        self.input_username_in_login.setFont(font3)

        self.horizontalLayout_6.addWidget(self.input_username_in_login)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_6)

        self.horizontalLayout_6.setStretch(0, 1)
        self.horizontalLayout_6.setStretch(2, 2)
        self.horizontalLayout_6.setStretch(3, 1)

        self.verticalLayout_3.addLayout(self.horizontalLayout_6)

        self.input_username_is_none_in_login = QLabel(self.tab)
        self.input_username_is_none_in_login.setObjectName(u"input_username_is_none_in_login")
        palette = QPalette()
        brush = QBrush(QColor(255, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(120, 120, 120, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        self.input_username_is_none_in_login.setPalette(palette)
        self.input_username_is_none_in_login.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.input_username_is_none_in_login)

        self.verticalLayout_3.setStretch(0, 4)
        self.verticalLayout_3.setStretch(1, 1)

        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)

        self.label_4 = QLabel(self.tab)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font3)

        self.horizontalLayout_5.addWidget(self.label_4)

        self.input_password_in_login = QLineEdit(self.tab)
        self.input_password_in_login.setObjectName(u"input_password_in_login")
        sizePolicy.setHeightForWidth(self.input_password_in_login.sizePolicy().hasHeightForWidth())
        self.input_password_in_login.setSizePolicy(sizePolicy)
        self.input_password_in_login.setFont(font3)

        self.horizontalLayout_5.addWidget(self.input_password_in_login)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_4)

        self.horizontalLayout_5.setStretch(0, 1)
        self.horizontalLayout_5.setStretch(2, 2)
        self.horizontalLayout_5.setStretch(3, 1)

        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.input_password_is_none_in_login = QLabel(self.tab)
        self.input_password_is_none_in_login.setObjectName(u"input_password_is_none_in_login")
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        self.input_password_is_none_in_login.setPalette(palette1)
        self.input_password_is_none_in_login.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.input_password_is_none_in_login)

        self.verticalLayout_2.setStretch(0, 4)
        self.verticalLayout_2.setStretch(1, 1)

        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.signup_button_in_login = QPushButton(self.tab)
        self.signup_button_in_login.setObjectName(u"signup_button_in_login")
        self.signup_button_in_login.setFont(font3)

        self.horizontalLayout_4.addWidget(self.signup_button_in_login)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.horizontalLayout_4.addItem(self.verticalSpacer_4)

        self.confirm_button_in_login = QPushButton(self.tab)
        self.confirm_button_in_login.setObjectName(u"confirm_button_in_login")
        font4 = QFont()
        font4.setPointSize(20)
        font4.setBold(False)
        font4.setWeight(50)
        self.confirm_button_in_login.setFont(font4)

        self.horizontalLayout_4.addWidget(self.confirm_button_in_login)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 2)
        self.horizontalLayout_4.setStretch(3, 2)
        self.horizontalLayout_4.setStretch(4, 1)

        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.verticalLayout_4.setStretch(0, 2)
        self.verticalLayout_4.setStretch(1, 2)
        self.verticalLayout_4.setStretch(2, 4)

        self.verticalLayout_5.addLayout(self.verticalLayout_4)

        self.verticalLayout_5.setStretch(0, 1)
        self.verticalLayout_5.setStretch(1, 2)

        self.verticalLayout_6.addLayout(self.verticalLayout_5)

        self.verticalLayout_6.setStretch(1, 9)

        self.gridLayout.addLayout(self.verticalLayout_6, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_3 = QGridLayout(self.tab_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_3)

        self.label = QLabel(self.tab_2)
        self.label.setObjectName(u"label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setFont(font2)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_2)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_11)

        self.username_in_signup = QLabel(self.tab_2)
        self.username_in_signup.setObjectName(u"username_in_signup")
        self.username_in_signup.setFont(font3)

        self.horizontalLayout.addWidget(self.username_in_signup)

        self.input_username_in_signup = QLineEdit(self.tab_2)
        self.input_username_in_signup.setObjectName(u"input_username_in_signup")
        sizePolicy.setHeightForWidth(self.input_username_in_signup.sizePolicy().hasHeightForWidth())
        self.input_username_in_signup.setSizePolicy(sizePolicy)
        self.input_username_in_signup.setFont(font3)

        self.horizontalLayout.addWidget(self.input_username_in_signup)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_13)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(2, 2)
        self.horizontalLayout.setStretch(3, 1)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.input_username_wrong_in_signup = QLabel(self.tab_2)
        self.input_username_wrong_in_signup.setObjectName(u"input_username_wrong_in_signup")
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        self.input_username_wrong_in_signup.setPalette(palette2)
        self.input_username_wrong_in_signup.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.input_username_wrong_in_signup)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_14)

        self.password_in_signup = QLabel(self.tab_2)
        self.password_in_signup.setObjectName(u"password_in_signup")
        self.password_in_signup.setFont(font3)

        self.horizontalLayout_2.addWidget(self.password_in_signup)

        self.input_password_in_signup = QLineEdit(self.tab_2)
        self.input_password_in_signup.setObjectName(u"input_password_in_signup")
        sizePolicy.setHeightForWidth(self.input_password_in_signup.sizePolicy().hasHeightForWidth())
        self.input_password_in_signup.setSizePolicy(sizePolicy)
        self.input_password_in_signup.setFont(font3)

        self.horizontalLayout_2.addWidget(self.input_password_in_signup)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_16)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(2, 2)
        self.horizontalLayout_2.setStretch(3, 1)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.input_password_wrong_in_signup = QLabel(self.tab_2)
        self.input_password_wrong_in_signup.setObjectName(u"input_password_wrong_in_signup")
        palette3 = QPalette()
        palette3.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        self.input_password_wrong_in_signup.setPalette(palette3)
        self.input_password_wrong_in_signup.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.input_password_wrong_in_signup)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_17)

        self.password_to_confirm_in_signup = QLabel(self.tab_2)
        self.password_to_confirm_in_signup.setObjectName(u"password_to_confirm_in_signup")
        self.password_to_confirm_in_signup.setFont(font3)

        self.horizontalLayout_3.addWidget(self.password_to_confirm_in_signup)

        self.input_password_to_confirm_in_signup = QLineEdit(self.tab_2)
        self.input_password_to_confirm_in_signup.setObjectName(u"input_password_to_confirm_in_signup")
        sizePolicy.setHeightForWidth(self.input_password_to_confirm_in_signup.sizePolicy().hasHeightForWidth())
        self.input_password_to_confirm_in_signup.setSizePolicy(sizePolicy)
        self.input_password_to_confirm_in_signup.setFont(font3)

        self.horizontalLayout_3.addWidget(self.input_password_to_confirm_in_signup)

        self.horizontalSpacer_19 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_19)

        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(2, 2)
        self.horizontalLayout_3.setStretch(3, 1)

        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.input_password_to_confirm_wrong_in_signup = QLabel(self.tab_2)
        self.input_password_to_confirm_wrong_in_signup.setObjectName(u"input_password_to_confirm_wrong_in_signup")
        palette4 = QPalette()
        palette4.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        self.input_password_to_confirm_wrong_in_signup.setPalette(palette4)
        self.input_password_to_confirm_wrong_in_signup.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.input_password_to_confirm_wrong_in_signup)

        self.verticalLayout.setStretch(0, 3)
        self.verticalLayout.setStretch(2, 3)
        self.verticalLayout.setStretch(4, 3)

        self.verticalLayout_7.addLayout(self.verticalLayout)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_8)

        self.return_to_login_button_in_signup = QPushButton(self.tab_2)
        self.return_to_login_button_in_signup.setObjectName(u"return_to_login_button_in_signup")
        self.return_to_login_button_in_signup.setFont(font4)

        self.horizontalLayout_7.addWidget(self.return_to_login_button_in_signup)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.horizontalLayout_7.addItem(self.verticalSpacer)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_9)

        self.confirm_button_in_signup = QPushButton(self.tab_2)
        self.confirm_button_in_signup.setObjectName(u"confirm_button_in_signup")
        self.confirm_button_in_signup.setFont(font4)

        self.horizontalLayout_7.addWidget(self.confirm_button_in_signup)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_10)

        self.horizontalLayout_7.setStretch(0, 1)
        self.horizontalLayout_7.setStretch(1, 2)
        self.horizontalLayout_7.setStretch(4, 2)
        self.horizontalLayout_7.setStretch(5, 1)

        self.verticalLayout_7.addLayout(self.horizontalLayout_7)

        self.verticalLayout_7.setStretch(0, 4)
        self.verticalLayout_7.setStretch(1, 2)

        self.verticalLayout_8.addLayout(self.verticalLayout_7)

        self.verticalLayout_8.setStretch(0, 2)
        self.verticalLayout_8.setStretch(1, 1)
        self.verticalLayout_8.setStretch(3, 8)

        self.gridLayout_3.addLayout(self.verticalLayout_8, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")

        self.gridLayout_2.addWidget(self.tabWidget, 0, 1, 1, 1)

        self.retranslateUi(Form)

        self.tabWidget.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.random_dialog.setText(QCoreApplication.translate("Form", u"\u6bcf\u65e5\u4e00\u53e5", None))
        self.label_2.setText(
            QCoreApplication.translate("Form", u"\u6b22\u8fce\u767b\u5f55Python\u67e5\u91cd\u7cfb\u7edf", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u7528\u6237\u540d\uff1a", None))
        self.input_username_is_none_in_login.setText(
            QCoreApplication.translate("Form", u"\u7528\u6237\u540d\u4e0d\u80fd\u4e3a\u7a7a", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u5bc6\u7801\uff1a  ", None))
        self.input_password_is_none_in_login.setText(
            QCoreApplication.translate("Form", u"\u5bc6\u7801\u4e0d\u80fd\u4e3a\u7a7a", None))
        self.signup_button_in_login.setText(QCoreApplication.translate("Form", u"\u6ce8\u518c", None))
        self.confirm_button_in_login.setText(QCoreApplication.translate("Form", u"\u786e\u8ba4", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab),
                                  QCoreApplication.translate("Form", u"\u767b\u5f55", None))
        self.label.setText(
            QCoreApplication.translate("Form", u"\u6b22\u8fce\u6ce8\u518cPython\u67e5\u91cd\u7cfb\u7edf", None))
        self.username_in_signup.setText(QCoreApplication.translate("Form", u"\u7528\u6237\u540d\uff1a ", None))
        self.input_username_wrong_in_signup.setText("")
        self.password_in_signup.setText(QCoreApplication.translate("Form", u"\u5bc6\u7801\uff1a   ", None))
        self.input_password_wrong_in_signup.setText("")
        self.password_to_confirm_in_signup.setText(
            QCoreApplication.translate("Form", u"\u786e\u8ba4\u5bc6\u7801\uff1a", None))
        self.input_password_to_confirm_wrong_in_signup.setText("")
        self.return_to_login_button_in_signup.setText(
            QCoreApplication.translate("Form", u"\u8fd4\u56de\u767b\u5f55\u754c\u9762", None))
        self.confirm_button_in_signup.setText(QCoreApplication.translate("Form", u"\u786e\u8ba4", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2),
                                  QCoreApplication.translate("Form", u"\u6ce8\u518c", None))
    # retranslateUi
