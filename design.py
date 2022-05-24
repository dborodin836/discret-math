# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'design.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(736, 485)
        MainWindow.setStyleSheet(u"QWidget {\n"
"	color: white;\n"
"	background-color: #303030;\n"
"	font-family: Rubik;\n"
"	font-size: 16pt;\n"
"	font-weight: 600;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #666;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #888;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setStyleSheet(u"font-size: 40pt;\n"
"border: none;")
        self.lineEdit.setReadOnly(True)

        self.verticalLayout_2.addWidget(self.lineEdit)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lineEdit_2 = QTextEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setReadOnly(True)

        self.horizontalLayout.addWidget(self.lineEdit_2)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.btn_arr_down = QPushButton(self.centralwidget)
        self.btn_arr_down.setObjectName(u"btn_arr_down")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_arr_down.sizePolicy().hasHeightForWidth())
        self.btn_arr_down.setSizePolicy(sizePolicy)
        self.btn_arr_down.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.btn_arr_down, 2, 3, 1, 1)

        self.btn_or_2 = QPushButton(self.centralwidget)
        self.btn_or_2.setObjectName(u"btn_or_2")
        sizePolicy.setHeightForWidth(self.btn_or_2.sizePolicy().hasHeightForWidth())
        self.btn_or_2.setSizePolicy(sizePolicy)
        self.btn_or_2.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.btn_or_2, 5, 1, 1, 1)

        self.btn_b = QPushButton(self.centralwidget)
        self.btn_b.setObjectName(u"btn_b")
        sizePolicy.setHeightForWidth(self.btn_b.sizePolicy().hasHeightForWidth())
        self.btn_b.setSizePolicy(sizePolicy)
        self.btn_b.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.btn_b, 3, 5, 1, 1)

        self.btn_eq = QPushButton(self.centralwidget)
        self.btn_eq.setObjectName(u"btn_eq")
        sizePolicy.setHeightForWidth(self.btn_eq.sizePolicy().hasHeightForWidth())
        self.btn_eq.setSizePolicy(sizePolicy)
        self.btn_eq.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.btn_eq, 3, 0, 1, 1)

        self.btn_z = QPushButton(self.centralwidget)
        self.btn_z.setObjectName(u"btn_z")
        sizePolicy.setHeightForWidth(self.btn_z.sizePolicy().hasHeightForWidth())
        self.btn_z.setSizePolicy(sizePolicy)
        self.btn_z.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.btn_z, 6, 3, 1, 1)

        self.btn_brace_right = QPushButton(self.centralwidget)
        self.btn_brace_right.setObjectName(u"btn_brace_right")
        sizePolicy.setHeightForWidth(self.btn_brace_right.sizePolicy().hasHeightForWidth())
        self.btn_brace_right.setSizePolicy(sizePolicy)
        self.btn_brace_right.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.btn_brace_right, 2, 1, 1, 1)

        self.btn_or = QPushButton(self.centralwidget)
        self.btn_or.setObjectName(u"btn_or")
        sizePolicy.setHeightForWidth(self.btn_or.sizePolicy().hasHeightForWidth())
        self.btn_or.setSizePolicy(sizePolicy)
        self.btn_or.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.btn_or, 5, 3, 1, 1)

        self.btn_brace_left = QPushButton(self.centralwidget)
        self.btn_brace_left.setObjectName(u"btn_brace_left")
        sizePolicy.setHeightForWidth(self.btn_brace_left.sizePolicy().hasHeightForWidth())
        self.btn_brace_left.setSizePolicy(sizePolicy)
        self.btn_brace_left.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.btn_brace_left, 2, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(15, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 3, 4, 1, 1)

        self.btn_xor = QPushButton(self.centralwidget)
        self.btn_xor.setObjectName(u"btn_xor")
        sizePolicy.setHeightForWidth(self.btn_xor.sizePolicy().hasHeightForWidth())
        self.btn_xor.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Rubik"])
        font.setPointSize(16)
        font.setBold(True)
        self.btn_xor.setFont(font)
        self.btn_xor.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.btn_xor, 5, 0, 1, 1)

        self.btn_x = QPushButton(self.centralwidget)
        self.btn_x.setObjectName(u"btn_x")
        sizePolicy.setHeightForWidth(self.btn_x.sizePolicy().hasHeightForWidth())
        self.btn_x.setSizePolicy(sizePolicy)
        self.btn_x.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.btn_x, 6, 0, 1, 1)

        self.btn_sheff = QPushButton(self.centralwidget)
        self.btn_sheff.setObjectName(u"btn_sheff")
        sizePolicy.setHeightForWidth(self.btn_sheff.sizePolicy().hasHeightForWidth())
        self.btn_sheff.setSizePolicy(sizePolicy)
        self.btn_sheff.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.btn_sheff, 3, 1, 1, 1)

        self.btn_calc = QPushButton(self.centralwidget)
        self.btn_calc.setObjectName(u"btn_calc")
        sizePolicy.setHeightForWidth(self.btn_calc.sizePolicy().hasHeightForWidth())
        self.btn_calc.setSizePolicy(sizePolicy)
        self.btn_calc.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.btn_calc, 1, 3, 1, 1)

        self.btn_a = QPushButton(self.centralwidget)
        self.btn_a.setObjectName(u"btn_a")
        sizePolicy.setHeightForWidth(self.btn_a.sizePolicy().hasHeightForWidth())
        self.btn_a.setSizePolicy(sizePolicy)
        self.btn_a.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.btn_a, 2, 5, 1, 1)

        self.btn_ce = QPushButton(self.centralwidget)
        self.btn_ce.setObjectName(u"btn_ce")
        sizePolicy.setHeightForWidth(self.btn_ce.sizePolicy().hasHeightForWidth())
        self.btn_ce.setSizePolicy(sizePolicy)
        self.btn_ce.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.btn_ce, 1, 1, 1, 1)

        self.btn_d = QPushButton(self.centralwidget)
        self.btn_d.setObjectName(u"btn_d")
        sizePolicy.setHeightForWidth(self.btn_d.sizePolicy().hasHeightForWidth())
        self.btn_d.setSizePolicy(sizePolicy)
        self.btn_d.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.btn_d, 6, 5, 1, 1)

        self.btn_not = QPushButton(self.centralwidget)
        self.btn_not.setObjectName(u"btn_not")
        sizePolicy.setHeightForWidth(self.btn_not.sizePolicy().hasHeightForWidth())
        self.btn_not.setSizePolicy(sizePolicy)
        self.btn_not.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.btn_not, 1, 5, 1, 1)

        self.btn_c = QPushButton(self.centralwidget)
        self.btn_c.setObjectName(u"btn_c")
        sizePolicy.setHeightForWidth(self.btn_c.sizePolicy().hasHeightForWidth())
        self.btn_c.setSizePolicy(sizePolicy)
        self.btn_c.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.btn_c, 5, 5, 1, 1)

        self.btn_arr_right = QPushButton(self.centralwidget)
        self.btn_arr_right.setObjectName(u"btn_arr_right")
        sizePolicy.setHeightForWidth(self.btn_arr_right.sizePolicy().hasHeightForWidth())
        self.btn_arr_right.setSizePolicy(sizePolicy)
        self.btn_arr_right.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.btn_arr_right, 3, 3, 1, 1)

        self.btn_y = QPushButton(self.centralwidget)
        self.btn_y.setObjectName(u"btn_y")
        sizePolicy.setHeightForWidth(self.btn_y.sizePolicy().hasHeightForWidth())
        self.btn_y.setSizePolicy(sizePolicy)
        self.btn_y.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.btn_y, 6, 1, 1, 1)

        self.btn_clear = QPushButton(self.centralwidget)
        self.btn_clear.setObjectName(u"btn_clear")
        sizePolicy.setHeightForWidth(self.btn_clear.sizePolicy().hasHeightForWidth())
        self.btn_clear.setSizePolicy(sizePolicy)
        self.btn_clear.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.btn_clear, 1, 0, 1, 1)


        self.horizontalLayout.addLayout(self.gridLayout)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"DiscreteMath", None))
        self.btn_arr_down.setText(QCoreApplication.translate("MainWindow", u"\u2193", None))
        self.btn_or_2.setText(QCoreApplication.translate("MainWindow", u"\u2228", None))
        self.btn_b.setText(QCoreApplication.translate("MainWindow", u"B", None))
        self.btn_eq.setText(QCoreApplication.translate("MainWindow", u"~", None))
        self.btn_z.setText(QCoreApplication.translate("MainWindow", u"Z", None))
        self.btn_brace_right.setText(QCoreApplication.translate("MainWindow", u")", None))
        self.btn_or.setText(QCoreApplication.translate("MainWindow", u"\u2227", None))
        self.btn_brace_left.setText(QCoreApplication.translate("MainWindow", u"(", None))
        self.btn_xor.setText(QCoreApplication.translate("MainWindow", u"\u2295", None))
        self.btn_x.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.btn_sheff.setText(QCoreApplication.translate("MainWindow", u"|", None))
        self.btn_calc.setText(QCoreApplication.translate("MainWindow", u"->", None))
        self.btn_a.setText(QCoreApplication.translate("MainWindow", u"A", None))
        self.btn_ce.setText(QCoreApplication.translate("MainWindow", u"CE", None))
        self.btn_d.setText(QCoreApplication.translate("MainWindow", u"D", None))
        self.btn_not.setText(QCoreApplication.translate("MainWindow", u"NOT", None))
        self.btn_c.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.btn_arr_right.setText(QCoreApplication.translate("MainWindow", u"\u2192", None))
        self.btn_y.setText(QCoreApplication.translate("MainWindow", u"Y", None))
        self.btn_clear.setText(QCoreApplication.translate("MainWindow", u"C", None))
    # retranslateUi

