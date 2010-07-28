#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui

import subprocess

class CallPickerDialog(QtGui.QDialog):
    """
    Writes and reads the xml file with the channel lists.
    """
    def __init__(self, env, command):
        """
        Standart edit.
        """
        super(CallPickerDialog, self).__init__()
        self.env = env
        self.command = command
        self._initInterface()
        self._connectSignals()

    def _initInterface(self):
        """
        Constructs the interface.
        """
        self.setWindowTitle('Call Picker')
        self.layout = QtGui.QVBoxLayout()
        self.setLayout(self.layout)
        desc = 'Edit the command for the picker if necessary and press OK to execute it.'
        self.description_label = QtGui.QLabel(desc)
        self.layout.addWidget(self.description_label)
        self.command_edit = QtGui.QLineEdit(self.command)
        self.layout.addWidget(self.command_edit)
        # Frame for the buttons.
        self.button_frame = QtGui.QFrame()
        self.layout.addWidget(self.button_frame)
        self.button_layout = QtGui.QHBoxLayout()
        self.button_layout.setMargin(0)
        self.button_frame.setLayout(self.button_layout)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding,
                                        QtGui.QSizePolicy.Minimum)
        self.button_layout.addItem(spacerItem)
        # Add buttons.
        self.reset_button = QtGui.QPushButton('Reset')
        self.cancel_button = QtGui.QPushButton('Cancel')
        self.ok_button = QtGui.QPushButton('OK')
        self.button_layout.addWidget(self.reset_button)
        self.button_layout.addWidget(self.cancel_button)
        self.button_layout.addWidget(self.ok_button)
        self.ok_button.setDefault(True)

    def reset(self):
        """
        Resets the content of the command edit line.
        """
        self.command_edit.setText(self.command)

    def accept(self):
        """
        Executes the command.
        """
        command = str(self.command_edit.text())
        subprocess.Popen(command, shell=True)
        super(CallPickerDialog, self).accept()

    def _connectSignals(self):
        """
        Connects signals and slots.
        """
        QtCore.QObject.connect(self.reset_button, QtCore.SIGNAL("clicked()"),
                               self.reset)
        QtCore.QObject.connect(self.cancel_button, QtCore.SIGNAL("clicked()"),
                               self.reject)
        QtCore.QObject.connect(self.ok_button, QtCore.SIGNAL("clicked()"),
                               self.accept)