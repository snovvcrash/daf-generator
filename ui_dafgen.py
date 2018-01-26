# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dafgen.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

"""
@file ui_dafgen.py
@author snovvcrash <snovvcrash@protonmail.com>
@date 2018-01

@brief Simple DAF Generator Ui

@license
Copyright (C) 2018 snovvcrash

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
@endlicense
"""

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DAFGen(object):
    def setupUi(self, DAFGen):
        DAFGen.setObjectName("DAFGen")
        DAFGen.resize(441, 95)
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
        self.actualDelayLabel.setGeometry(QtCore.QRect(20, 50, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.actualDelayLabel.setFont(font)
        self.actualDelayLabel.setObjectName("actualDelayLabel")
        self.startButton = QtWidgets.QPushButton(DAFGen)
        self.startButton.setGeometry(QtCore.QRect(190, 50, 71, 31))
        self.startButton.setObjectName("startButton")
        self.stopButton = QtWidgets.QPushButton(DAFGen)
        self.stopButton.setGeometry(QtCore.QRect(270, 50, 71, 31))
        self.stopButton.setObjectName("stopButton")
        self.quitButton = QtWidgets.QPushButton(DAFGen)
        self.quitButton.setGeometry(QtCore.QRect(350, 50, 71, 31))
        self.quitButton.setObjectName("quitButton")
        self.delaySlider = QtWidgets.QSlider(DAFGen)
        self.delaySlider.setGeometry(QtCore.QRect(110, 10, 241, 21))
        self.delaySlider.setMinimum(50)
        self.delaySlider.setMaximum(200)
        self.delaySlider.setOrientation(QtCore.Qt.Horizontal)
        self.delaySlider.setObjectName("delaySlider")
        self.delayEdit = QtWidgets.QPlainTextEdit(DAFGen)
        self.delayEdit.setGeometry(QtCore.QRect(360, 10, 61, 31))
        self.delayEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.delayEdit.setReadOnly(True)
        self.delayEdit.setObjectName("delayEdit")
        self.actualDelayEdit = QtWidgets.QPlainTextEdit(DAFGen)
        self.actualDelayEdit.setGeometry(QtCore.QRect(110, 50, 61, 31))
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

