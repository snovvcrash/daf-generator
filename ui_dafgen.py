# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dafgen.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DAFGen(object):
    def setupUi(self, DAFGen):
        DAFGen.setObjectName("DAFGen")
        DAFGen.resize(451, 95)
        DAFGen.setMinimumSize(QtCore.QSize(451, 95))
        DAFGen.setMaximumSize(QtCore.QSize(451, 95))
        font = QtGui.QFont()
        font.setPointSize(11)
        DAFGen.setFont(font)
        self.delayLabel = QtWidgets.QLabel(DAFGen)
        self.delayLabel.setGeometry(QtCore.QRect(20, 10, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.delayLabel.setFont(font)
        self.delayLabel.setObjectName("delayLabel")
        self.actualDelayLabel = QtWidgets.QLabel(DAFGen)
        self.actualDelayLabel.setGeometry(QtCore.QRect(20, 50, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.actualDelayLabel.setFont(font)
        self.actualDelayLabel.setObjectName("actualDelayLabel")
        self.startButton = QtWidgets.QPushButton(DAFGen)
        self.startButton.setGeometry(QtCore.QRect(200, 50, 71, 31))
        self.startButton.setObjectName("startButton")
        self.stopButton = QtWidgets.QPushButton(DAFGen)
        self.stopButton.setGeometry(QtCore.QRect(280, 50, 71, 31))
        self.stopButton.setObjectName("stopButton")
        self.quitButton = QtWidgets.QPushButton(DAFGen)
        self.quitButton.setGeometry(QtCore.QRect(360, 50, 71, 31))
        self.quitButton.setObjectName("quitButton")
        self.delaySlider = QtWidgets.QSlider(DAFGen)
        self.delaySlider.setGeometry(QtCore.QRect(120, 10, 241, 21))
        self.delaySlider.setMinimum(50)
        self.delaySlider.setMaximum(200)
        self.delaySlider.setOrientation(QtCore.Qt.Horizontal)
        self.delaySlider.setObjectName("delaySlider")
        self.delayEdit = QtWidgets.QPlainTextEdit(DAFGen)
        self.delayEdit.setGeometry(QtCore.QRect(370, 10, 61, 31))
        self.delayEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.delayEdit.setReadOnly(True)
        self.delayEdit.setObjectName("delayEdit")
        self.actualDelayEdit = QtWidgets.QPlainTextEdit(DAFGen)
        self.actualDelayEdit.setGeometry(QtCore.QRect(120, 50, 61, 31))
        self.actualDelayEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.actualDelayEdit.setReadOnly(True)
        self.actualDelayEdit.setObjectName("actualDelayEdit")

        self.retranslateUi(DAFGen)
        QtCore.QMetaObject.connectSlotsByName(DAFGen)

    def retranslateUi(self, DAFGen):
        _translate = QtCore.QCoreApplication.translate
        DAFGen.setWindowTitle(_translate("DAFGen", "DAF Gen"))
        self.delayLabel.setText(_translate("DAFGen", "Delay"))
        self.actualDelayLabel.setText(_translate("DAFGen", "Actual Delay"))
        self.startButton.setText(_translate("DAFGen", "Start"))
        self.stopButton.setText(_translate("DAFGen", "Stop"))
        self.quitButton.setText(_translate("DAFGen", "Quit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DAFGen = QtWidgets.QDialog()
    ui = Ui_DAFGen()
    ui.setupUi(DAFGen)
    DAFGen.show()
    sys.exit(app.exec_())

