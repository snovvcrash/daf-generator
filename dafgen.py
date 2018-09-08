#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@file dafgen.py
@author snovvcrash <scr.im/emsnovvcrash>
@date 2018-01

@brief Simple DAF (Delayed Auditory Feedback) Generator

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

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from ui_dafgen import Ui_DAFGen

from pyaudio import PyAudio, paFloat32
from math import floor
from time import clock

import sys

class Worker(QThread):

	_trigger = pyqtSignal(float)

	def __init__(self, bufferSize, streamIn, streamOut):
		QThread.__init__(self)
		self._bufferSize = bufferSize
		self._streamIn = streamIn
		self._streamOut = streamOut

	def __del__(self):
		self.wait()

	def _genDAF(self):
		while self._streamIn.is_active():
			start = clock()
			audioData = self._streamIn.read(self._bufferSize)
			self._streamOut.write(audioData)
			actualDelay = clock() - start
			self._trigger.emit(actualDelay)

	def run(self):
		self._genDAF()

class MainApp(QMainWindow, Ui_DAFGen):

	_CHANNELS = 2
	_RATE = 44100

	def __init__(self):
		super().__init__()
		self.setupUi(self)

		self.stopButton.setEnabled(False)
		#self.delaySlider.setValue(190)
		self._updateDelay()

		self.delaySlider.valueChanged.connect(self._updateDelay)
		self.startButton.clicked.connect(self._startCapture)
		self.stopButton.clicked.connect(self._stopCapture)
		self.quitButton.clicked.connect(QApplication.quit)

	def _updateDelay(self):
		self.delayEdit.setPlainText(str(self.delaySlider.value()) + ' ms')

	def _startCapture(self):
		bufferSize = floor(self.delaySlider.value() / 1000 * self._RATE)
		device = PyAudio()

		try:
			streamIn = device.open(format=paFloat32, channels=self._CHANNELS, rate=self._RATE, input=True, frames_per_buffer=bufferSize)
			streamOut = device.open(format=paFloat32, channels=self._CHANNELS, rate=self._RATE, output=True, frames_per_buffer=bufferSize)
		except OSError as e:
			QMessageBox.critical(self, 'Error', 'No input/output device found! Connect and rerun.')
			return

		self._workerThread = Worker(bufferSize, streamIn, streamOut)
		self._workerThread._trigger.connect(self._updateActualDelay)

		self.startButton.setEnabled(False)
		self.delaySlider.setEnabled(False)
		self.stopButton.setEnabled(True)

		self._workerThread.start()

	def _stopCapture(self):
		self._workerThread.terminate()

		self.actualDelayEdit.clear()
		self.startButton.setEnabled(True)
		self.delaySlider.setEnabled(True)
		self.stopButton.setEnabled(False)

	def _updateActualDelay(self, t):
		newValue = floor(t * 1000)
		self.actualDelayEdit.setPlainText(str(newValue) + ' ms')

def main():
	app = QApplication(sys.argv)
	win = MainApp()
	win.show()
	sys.exit(app.exec_())


if __name__ == '__main__':
	main()
