# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1120, 894)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.openBtn = QtWidgets.QPushButton(self.centralwidget)
        self.openBtn.setGeometry(QtCore.QRect(740, 680, 75, 23))
        self.openBtn.setObjectName("openBtn")
        self.openText = QtWidgets.QTextEdit(self.centralwidget)
        self.openText.setGeometry(QtCore.QRect(40, 670, 671, 61))
        self.openText.setObjectName("openText")
        self.upText = QtWidgets.QListView(self.centralwidget)
        self.upText.setGeometry(QtCore.QRect(40, 750, 671, 61))
        self.upText.setObjectName("upText")
        self.leaBtn = QtWidgets.QPushButton(self.centralwidget)
        self.leaBtn.setGeometry(QtCore.QRect(740, 730, 75, 23))
        self.leaBtn.setObjectName("leaBtn")
        self.actBtn = QtWidgets.QPushButton(self.centralwidget)
        self.actBtn.setGeometry(QtCore.QRect(740, 780, 75, 23))
        self.actBtn.setObjectName("actBtn")
        self.G1 = QtWidgets.QListView(self.centralwidget)
        self.G1.setGeometry(QtCore.QRect(710, 150, 401, 361))
        self.G1.setObjectName("G1")
        self.resText = QtWidgets.QListView(self.centralwidget)
        self.resText.setGeometry(QtCore.QRect(40, 20, 651, 621))
        self.resText.setObjectName("resText")
        self.hrChk = QtWidgets.QCheckBox(self.centralwidget)
        self.hrChk.setGeometry(QtCore.QRect(860, 670, 81, 16))
        self.hrChk.setObjectName("hrChk")
        self.tempChk = QtWidgets.QCheckBox(self.centralwidget)
        self.tempChk.setGeometry(QtCore.QRect(860, 700, 81, 16))
        self.tempChk.setObjectName("tempChk")
        self.preChk = QtWidgets.QCheckBox(self.centralwidget)
        self.preChk.setGeometry(QtCore.QRect(860, 730, 81, 16))
        self.preChk.setObjectName("preChk")
        self.windChk = QtWidgets.QCheckBox(self.centralwidget)
        self.windChk.setGeometry(QtCore.QRect(860, 760, 81, 16))
        self.windChk.setObjectName("windChk")
        self.humiChk = QtWidgets.QCheckBox(self.centralwidget)
        self.humiChk.setGeometry(QtCore.QRect(860, 790, 81, 16))
        self.humiChk.setObjectName("humiChk")
        self.cntChk = QtWidgets.QCheckBox(self.centralwidget)
        self.cntChk.setGeometry(QtCore.QRect(960, 760, 81, 16))
        self.cntChk.setObjectName("cntChk")
        self.visiChk = QtWidgets.QCheckBox(self.centralwidget)
        self.visiChk.setGeometry(QtCore.QRect(960, 670, 81, 16))
        self.visiChk.setObjectName("visiChk")
        self.pm10Chk = QtWidgets.QCheckBox(self.centralwidget)
        self.pm10Chk.setGeometry(QtCore.QRect(960, 700, 81, 16))
        self.pm10Chk.setObjectName("pm10Chk")
        self.pm25Chk = QtWidgets.QCheckBox(self.centralwidget)
        self.pm25Chk.setGeometry(QtCore.QRect(960, 730, 81, 16))
        self.pm25Chk.setObjectName("pm25Chk")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 10, 56, 12))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 660, 56, 12))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 740, 56, 12))
        self.label_3.setObjectName("label_3")
        self.allChk = QtWidgets.QCheckBox(self.centralwidget)
        self.allChk.setGeometry(QtCore.QRect(960, 790, 81, 16))
        self.allChk.setObjectName("allChk")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(710, 140, 56, 12))
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1120, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.openBtn.setText(_translate("MainWindow", "Open"))
        self.leaBtn.setText(_translate("MainWindow", "Leaning"))
        self.actBtn.setText(_translate("MainWindow", "Result"))
        self.hrChk.setText(_translate("MainWindow", "Hour"))
        self.tempChk.setText(_translate("MainWindow", "Temperature"))
        self.preChk.setText(_translate("MainWindow", "Precipitation"))
        self.windChk.setText(_translate("MainWindow", "Windspped"))
        self.humiChk.setText(_translate("MainWindow", "Humidity"))
        self.cntChk.setText(_translate("MainWindow", "Count"))
        self.visiChk.setText(_translate("MainWindow", "Visibility"))
        self.pm10Chk.setText(_translate("MainWindow", "Pm10"))
        self.pm25Chk.setText(_translate("MainWindow", "Pm2.5"))
        self.label.setText(_translate("MainWindow", "resText"))
        self.label_2.setText(_translate("MainWindow", "openText"))
        self.label_3.setText(_translate("MainWindow", "upText"))
        self.allChk.setText(_translate("MainWindow", "All"))
        self.label_4.setText(_translate("MainWindow", "G1"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

