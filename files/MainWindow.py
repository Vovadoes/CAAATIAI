# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'files/MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 310)
        MainWindow.setMinimumSize(QtCore.QSize(800, 310))
        MainWindow.setMaximumSize(QtCore.QSize(800, 350))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_10 = QtWidgets.QGridLayout()
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.label_39 = QtWidgets.QLabel(self.centralwidget)
        self.label_39.setMinimumSize(QtCore.QSize(370, 35))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_39.setFont(font)
        self.label_39.setObjectName("label_39")
        self.gridLayout_10.addWidget(self.label_39, 0, 0, 1, 1)
        self.label_41 = QtWidgets.QLabel(self.centralwidget)
        self.label_41.setMinimumSize(QtCore.QSize(30, 0))
        self.label_41.setMaximumSize(QtCore.QSize(30, 16777215))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setItalic(True)
        self.label_41.setFont(font)
        self.label_41.setObjectName("label_41")
        self.gridLayout_10.addWidget(self.label_41, 0, 1, 1, 1)
        self.label_42 = QtWidgets.QLabel(self.centralwidget)
        self.label_42.setMinimumSize(QtCore.QSize(20, 0))
        self.label_42.setMaximumSize(QtCore.QSize(20, 16777215))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_42.setFont(font)
        self.label_42.setObjectName("label_42")
        self.gridLayout_10.addWidget(self.label_42, 0, 2, 1, 1)
        self.doubleSpinBox_8 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_8.setMinimumSize(QtCore.QSize(214, 25))
        self.doubleSpinBox_8.setMaximumSize(QtCore.QSize(16777215, 220))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.doubleSpinBox_8.setFont(font)
        self.doubleSpinBox_8.setDecimals(0)
        self.doubleSpinBox_8.setMinimum(-999999999.0)
        self.doubleSpinBox_8.setMaximum(16777215.0)
        self.doubleSpinBox_8.setSingleStep(1.0)
        self.doubleSpinBox_8.setObjectName("doubleSpinBox_8")
        self.gridLayout_10.addWidget(self.doubleSpinBox_8, 0, 3, 1, 1)
        self.label_43 = QtWidgets.QLabel(self.centralwidget)
        self.label_43.setMinimumSize(QtCore.QSize(50, 0))
        self.label_43.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_43.setFont(font)
        self.label_43.setObjectName("label_43")
        self.gridLayout_10.addWidget(self.label_43, 0, 4, 1, 1)
        self.label_44 = QtWidgets.QLabel(self.centralwidget)
        self.label_44.setText("")
        self.label_44.setObjectName("label_44")
        self.gridLayout_10.addWidget(self.label_44, 0, 5, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_10, 0, 0, 1, 1)
        self.gridLayout_11 = QtWidgets.QGridLayout()
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.label_45 = QtWidgets.QLabel(self.centralwidget)
        self.label_45.setMinimumSize(QtCore.QSize(30, 0))
        self.label_45.setMaximumSize(QtCore.QSize(30, 16777215))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setItalic(True)
        self.label_45.setFont(font)
        self.label_45.setObjectName("label_45")
        self.gridLayout_11.addWidget(self.label_45, 0, 1, 1, 1)
        self.label_40 = QtWidgets.QLabel(self.centralwidget)
        self.label_40.setMinimumSize(QtCore.QSize(370, 35))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_40.setFont(font)
        self.label_40.setObjectName("label_40")
        self.gridLayout_11.addWidget(self.label_40, 0, 0, 1, 1)
        self.label_46 = QtWidgets.QLabel(self.centralwidget)
        self.label_46.setMinimumSize(QtCore.QSize(20, 0))
        self.label_46.setMaximumSize(QtCore.QSize(20, 16777215))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_46.setFont(font)
        self.label_46.setObjectName("label_46")
        self.gridLayout_11.addWidget(self.label_46, 0, 2, 1, 1)
        self.label_48 = QtWidgets.QLabel(self.centralwidget)
        self.label_48.setText("")
        self.label_48.setObjectName("label_48")
        self.gridLayout_11.addWidget(self.label_48, 0, 5, 1, 1)
        self.label_47 = QtWidgets.QLabel(self.centralwidget)
        self.label_47.setMinimumSize(QtCore.QSize(50, 0))
        self.label_47.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_47.setFont(font)
        self.label_47.setObjectName("label_47")
        self.gridLayout_11.addWidget(self.label_47, 0, 4, 1, 1)
        self.doubleSpinBox_9 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_9.setMinimumSize(QtCore.QSize(214, 25))
        self.doubleSpinBox_9.setMaximumSize(QtCore.QSize(16777215, 220))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.doubleSpinBox_9.setFont(font)
        self.doubleSpinBox_9.setDecimals(0)
        self.doubleSpinBox_9.setMinimum(-16777215.0)
        self.doubleSpinBox_9.setMaximum(16777215.0)
        self.doubleSpinBox_9.setSingleStep(1.0)
        self.doubleSpinBox_9.setObjectName("doubleSpinBox_9")
        self.gridLayout_11.addWidget(self.doubleSpinBox_9, 0, 3, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_11, 1, 0, 1, 1)
        self.gridLayout_12 = QtWidgets.QGridLayout()
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.label_49 = QtWidgets.QLabel(self.centralwidget)
        self.label_49.setMinimumSize(QtCore.QSize(370, 35))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_49.setFont(font)
        self.label_49.setObjectName("label_49")
        self.gridLayout_12.addWidget(self.label_49, 0, 0, 1, 1)
        self.label_50 = QtWidgets.QLabel(self.centralwidget)
        self.label_50.setMinimumSize(QtCore.QSize(30, 0))
        self.label_50.setMaximumSize(QtCore.QSize(30, 16777215))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setItalic(True)
        self.label_50.setFont(font)
        self.label_50.setObjectName("label_50")
        self.gridLayout_12.addWidget(self.label_50, 0, 1, 1, 1)
        self.label_51 = QtWidgets.QLabel(self.centralwidget)
        self.label_51.setMinimumSize(QtCore.QSize(20, 0))
        self.label_51.setMaximumSize(QtCore.QSize(20, 16777215))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_51.setFont(font)
        self.label_51.setObjectName("label_51")
        self.gridLayout_12.addWidget(self.label_51, 0, 2, 1, 1)
        self.doubleSpinBox_10 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_10.setMinimumSize(QtCore.QSize(214, 25))
        self.doubleSpinBox_10.setMaximumSize(QtCore.QSize(16777215, 220))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.doubleSpinBox_10.setFont(font)
        self.doubleSpinBox_10.setDecimals(2)
        self.doubleSpinBox_10.setMinimum(-16777215.0)
        self.doubleSpinBox_10.setMaximum(16777215.0)
        self.doubleSpinBox_10.setSingleStep(0.01)
        self.doubleSpinBox_10.setObjectName("doubleSpinBox_10")
        self.gridLayout_12.addWidget(self.doubleSpinBox_10, 0, 3, 1, 1)
        self.label_52 = QtWidgets.QLabel(self.centralwidget)
        self.label_52.setMinimumSize(QtCore.QSize(50, 0))
        self.label_52.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_52.setFont(font)
        self.label_52.setObjectName("label_52")
        self.gridLayout_12.addWidget(self.label_52, 0, 4, 1, 1)
        self.label_53 = QtWidgets.QLabel(self.centralwidget)
        self.label_53.setText("")
        self.label_53.setObjectName("label_53")
        self.gridLayout_12.addWidget(self.label_53, 0, 5, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_12, 2, 0, 1, 1)
        self.gridLayout_13 = QtWidgets.QGridLayout()
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.label_54 = QtWidgets.QLabel(self.centralwidget)
        self.label_54.setMinimumSize(QtCore.QSize(370, 35))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_54.setFont(font)
        self.label_54.setObjectName("label_54")
        self.gridLayout_13.addWidget(self.label_54, 0, 0, 1, 1)
        self.label_55 = QtWidgets.QLabel(self.centralwidget)
        self.label_55.setMinimumSize(QtCore.QSize(30, 0))
        self.label_55.setMaximumSize(QtCore.QSize(30, 16777215))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setItalic(True)
        self.label_55.setFont(font)
        self.label_55.setObjectName("label_55")
        self.gridLayout_13.addWidget(self.label_55, 0, 1, 1, 1)
        self.label_56 = QtWidgets.QLabel(self.centralwidget)
        self.label_56.setMinimumSize(QtCore.QSize(20, 0))
        self.label_56.setMaximumSize(QtCore.QSize(20, 16777215))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_56.setFont(font)
        self.label_56.setObjectName("label_56")
        self.gridLayout_13.addWidget(self.label_56, 0, 2, 1, 1)
        self.doubleSpinBox_11 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_11.setMinimumSize(QtCore.QSize(214, 25))
        self.doubleSpinBox_11.setMaximumSize(QtCore.QSize(16777215, 220))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.doubleSpinBox_11.setFont(font)
        self.doubleSpinBox_11.setDecimals(0)
        self.doubleSpinBox_11.setMinimum(-16777215.0)
        self.doubleSpinBox_11.setMaximum(16777215.0)
        self.doubleSpinBox_11.setSingleStep(1.0)
        self.doubleSpinBox_11.setObjectName("doubleSpinBox_11")
        self.gridLayout_13.addWidget(self.doubleSpinBox_11, 0, 3, 1, 1)
        self.label_57 = QtWidgets.QLabel(self.centralwidget)
        self.label_57.setMinimumSize(QtCore.QSize(50, 0))
        self.label_57.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_57.setFont(font)
        self.label_57.setObjectName("label_57")
        self.gridLayout_13.addWidget(self.label_57, 0, 4, 1, 1)
        self.label_58 = QtWidgets.QLabel(self.centralwidget)
        self.label_58.setText("")
        self.label_58.setObjectName("label_58")
        self.gridLayout_13.addWidget(self.label_58, 0, 5, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_13, 3, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setMinimumSize(QtCore.QSize(400, 35))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.gridLayout_3.addWidget(self.label_12, 0, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_2.addWidget(self.pushButton_2, 0, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_2.addWidget(self.pushButton, 0, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 1, 0, 1, 1)
        self.gridLayout_3.setRowMinimumHeight(0, 1)
        self.gridLayout_3.setRowMinimumHeight(1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_3, 1, 0, 1, 1)
        self.gridLayout_4.setRowStretch(0, 4)
        self.gridLayout_4.setRowStretch(1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Расчет реальной наращенной суммы с учетом инфляции"))
        self.label_39.setText(_translate("MainWindow", "<html><head/><body><p>Введите исходную сумму:</p></body></html>"))
        self.label_41.setText(_translate("MainWindow", "<html><head/><body><p>P</p></body></html>"))
        self.label_42.setText(_translate("MainWindow", "<html><head/><body><p>=</p></body></html>"))
        self.label_43.setText(_translate("MainWindow", "<html><head/><body><p>руб.</p></body></html>"))
        self.label_45.setText(_translate("MainWindow", "<html><head/><body><p>m</p></body></html>"))
        self.label_40.setText(_translate("MainWindow", "<html><head/><body><p>Введите годовую ставку:</p></body></html>"))
        self.label_46.setText(_translate("MainWindow", "<html><head/><body><p>=</p></body></html>"))
        self.label_47.setText(_translate("MainWindow", "<html><head/><body><p>%</p></body></html>"))
        self.label_49.setText(_translate("MainWindow", "<html><head/><body><p>Введите срок финансовой операции:</p></body></html>"))
        self.label_50.setText(_translate("MainWindow", "<html><head/><body><p>n</p></body></html>"))
        self.label_51.setText(_translate("MainWindow", "<html><head/><body><p>=</p></body></html>"))
        self.label_52.setText(_translate("MainWindow", "<html><head/><body><p>лет</p></body></html>"))
        self.label_54.setText(_translate("MainWindow", "<html><head/><body><p>Введите годовую инфляцию:</p></body></html>"))
        self.label_55.setText(_translate("MainWindow", "<html><head/><body><p>h</p></body></html>"))
        self.label_56.setText(_translate("MainWindow", "<html><head/><body><p>=</p></body></html>"))
        self.label_57.setText(_translate("MainWindow", "<html><head/><body><p>%</p></body></html>"))
        self.label_12.setText(_translate("MainWindow", "<html><head/><body><p>Сделать расчет для ставки:</p></body></html>"))
        self.pushButton_2.setText(_translate("MainWindow", "простой"))
        self.pushButton.setText(_translate("MainWindow", "сложной"))
