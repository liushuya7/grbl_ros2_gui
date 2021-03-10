# -*- coding: UTF-8 -*-

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'                                                                         '
' Copyright 2018-2021 Gauthier Brière (gauthier.briere "at" gmail.com)    '
'                                                                         '
' This file is part of cn5X++                                             '
'                                                                         '
' cn5X++ is free software: you can redistribute it and/or modify it       '
'  under the terms of the GNU General Public License as published by      '
' the Free Software Foundation, either version 3 of the License, or       '
' (at your option) any later version.                                     '
'                                                                         '
' cn5X++ is distributed in the hope that it will be useful, but           '
' WITHOUT ANY WARRANTY; without even the implied warranty of              '
' MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the           '
' GNU General Public License for more details.                            '
'                                                                         '
' You should have received a copy of the GNU General Public License       '
' along with this program.  If not, see <http://www.gnu.org/licenses/>.   '
'                                                                         '
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

import sys, os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal, pyqtSlot

class cnLed(QtWidgets.QLabel):
  ''' QLabel affichant une image de Led eteinte ou allumee '''

  statusChanged = pyqtSignal(bool) # signal emis a chaque changement de valeur

  def __init__(self, parent=None):
    super(cnLed, self).__init__(parent=parent)

    # Chemin des images dans le fichier de resources
    self.__imagePath = ":/images/"
    #self.iconOff = QtGui.QIcon() :/images/ledRougeEteinte.svg
    #self.iconOn  = QtGui.QIcon()
    #self.iconOff.addPixmap(QtGui.QPixmap(self.__imagePath + "ledRougeEteinte.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    #self.iconOn.addPixmap(QtGui.QPixmap(self.__imagePath + "ledRougeAlumee.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    self.iconOff = QtGui.QPixmap(self.__imagePath + "ledRougeEteinte.svg")
    self.iconOn  = QtGui.QPixmap(self.__imagePath + "ledRougeAlumee.svg")

    # Proprietes du label
    self.setMaximumSize(QtCore.QSize(20, 20))
    self.setText("")
    self.setPixmap(self.iconOff)
    self.setScaledContents(True)

    self.__ledStatus = False # led eteinte a l'initialisation


  @pyqtSlot()
  def getLedStatus(self):
    ''' Renvoie le status de la Led '''
    return self.__ledStatus


  @pyqtSlot(bool)
  def setLedStatus(self, s: bool):
    ''' Allume (s=True) ou eteind (s=False) la Led '''
    if self.__ledStatus != s:
      if s:
        self.setPixmap(self.iconOn)
      else:
        self.setPixmap(self.iconOff)
      self.__ledStatus = s
      self.statusChanged.emit(s)


  # Definie la propriete pour permettre la configuration par Designer
  ledStatus = QtCore.pyqtProperty(bool, fget=getLedStatus, fset=setLedStatus)

#---------------------------------------------------------------------------------

# Resource object code
#
# Created by: The Resource Compiler for PyQt5 (Qt v5.10.1)
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore

qt_resource_data = b"\
\x00\x00\x0f\x21\
\x3c\
\x3f\x78\x6d\x6c\x20\x76\x65\x72\x73\x69\x6f\x6e\x3d\x22\x31\x2e\
\x30\x22\x20\x65\x6e\x63\x6f\x64\x69\x6e\x67\x3d\x22\x55\x54\x46\
\x2d\x38\x22\x20\x73\x74\x61\x6e\x64\x61\x6c\x6f\x6e\x65\x3d\x22\
\x6e\x6f\x22\x3f\x3e\x0a\x3c\x21\x2d\x2d\x20\x43\x72\x65\x61\x74\
\x65\x64\x20\x77\x69\x74\x68\x20\x49\x6e\x6b\x73\x63\x61\x70\x65\
\x20\x28\x68\x74\x74\x70\x3a\x2f\x2f\x77\x77\x77\x2e\x69\x6e\x6b\
\x73\x63\x61\x70\x65\x2e\x6f\x72\x67\x2f\x29\x20\x2d\x2d\x3e\x0a\
\x0a\x3c\x73\x76\x67\x0a\x20\x20\x20\x78\x6d\x6c\x6e\x73\x3a\x64\
\x63\x3d\x22\x68\x74\x74\x70\x3a\x2f\x2f\x70\x75\x72\x6c\x2e\x6f\
\x72\x67\x2f\x64\x63\x2f\x65\x6c\x65\x6d\x65\x6e\x74\x73\x2f\x31\
\x2e\x31\x2f\x22\x0a\x20\x20\x20\x78\x6d\x6c\x6e\x73\x3a\x63\x63\
\x3d\x22\x68\x74\x74\x70\x3a\x2f\x2f\x63\x72\x65\x61\x74\x69\x76\
\x65\x63\x6f\x6d\x6d\x6f\x6e\x73\x2e\x6f\x72\x67\x2f\x6e\x73\x23\
\x22\x0a\x20\x20\x20\x78\x6d\x6c\x6e\x73\x3a\x72\x64\x66\x3d\x22\
\x68\x74\x74\x70\x3a\x2f\x2f\x77\x77\x77\x2e\x77\x33\x2e\x6f\x72\
\x67\x2f\x31\x39\x39\x39\x2f\x30\x32\x2f\x32\x32\x2d\x72\x64\x66\
\x2d\x73\x79\x6e\x74\x61\x78\x2d\x6e\x73\x23\x22\x0a\x20\x20\x20\
\x78\x6d\x6c\x6e\x73\x3a\x73\x76\x67\x3d\x22\x68\x74\x74\x70\x3a\
\x2f\x2f\x77\x77\x77\x2e\x77\x33\x2e\x6f\x72\x67\x2f\x32\x30\x30\
\x30\x2f\x73\x76\x67\x22\x0a\x20\x20\x20\x78\x6d\x6c\x6e\x73\x3d\
\x22\x68\x74\x74\x70\x3a\x2f\x2f\x77\x77\x77\x2e\x77\x33\x2e\x6f\
\x72\x67\x2f\x32\x30\x30\x30\x2f\x73\x76\x67\x22\x0a\x20\x20\x20\
\x78\x6d\x6c\x6e\x73\x3a\x78\x6c\x69\x6e\x6b\x3d\x22\x68\x74\x74\
\x70\x3a\x2f\x2f\x77\x77\x77\x2e\x77\x33\x2e\x6f\x72\x67\x2f\x31\
\x39\x39\x39\x2f\x78\x6c\x69\x6e\x6b\x22\x0a\x20\x20\x20\x78\x6d\
\x6c\x6e\x73\x3a\x73\x6f\x64\x69\x70\x6f\x64\x69\x3d\x22\x68\x74\
\x74\x70\x3a\x2f\x2f\x73\x6f\x64\x69\x70\x6f\x64\x69\x2e\x73\x6f\
\x75\x72\x63\x65\x66\x6f\x72\x67\x65\x2e\x6e\x65\x74\x2f\x44\x54\
\x44\x2f\x73\x6f\x64\x69\x70\x6f\x64\x69\x2d\x30\x2e\x64\x74\x64\
\x22\x0a\x20\x20\x20\x78\x6d\x6c\x6e\x73\x3a\x69\x6e\x6b\x73\x63\
\x61\x70\x65\x3d\x22\x68\x74\x74\x70\x3a\x2f\x2f\x77\x77\x77\x2e\
\x69\x6e\x6b\x73\x63\x61\x70\x65\x2e\x6f\x72\x67\x2f\x6e\x61\x6d\
\x65\x73\x70\x61\x63\x65\x73\x2f\x69\x6e\x6b\x73\x63\x61\x70\x65\
\x22\x0a\x20\x20\x20\x77\x69\x64\x74\x68\x3d\x22\x34\x38\x22\x0a\
\x20\x20\x20\x68\x65\x69\x67\x68\x74\x3d\x22\x34\x38\x22\x0a\x20\
\x20\x20\x76\x69\x65\x77\x42\x6f\x78\x3d\x22\x30\x20\x30\x20\x34\
\x38\x20\x34\x38\x22\x0a\x20\x20\x20\x76\x65\x72\x73\x69\x6f\x6e\
\x3d\x22\x31\x2e\x31\x22\x0a\x20\x20\x20\x69\x64\x3d\x22\x73\x76\
\x67\x38\x22\x0a\x20\x20\x20\x69\x6e\x6b\x73\x63\x61\x70\x65\x3a\
\x76\x65\x72\x73\x69\x6f\x6e\x3d\x22\x30\x2e\x39\x32\x2e\x33\x20\
\x28\x32\x34\x30\x35\x35\x34\x36\x2c\x20\x32\x30\x31\x38\x2d\x30\
\x33\x2d\x31\x31\x29\x22\x0a\x20\x20\x20\x73\x6f\x64\x69\x70\x6f\
\x64\x69\x3a\x64\x6f\x63\x6e\x61\x6d\x65\x3d\x22\x6c\x65\x64\x52\
\x6f\x75\x67\x65\x41\x6c\x75\x6d\x65\x65\x2e\x73\x76\x67\x22\x3e\
\x0a\x20\x20\x3c\x64\x65\x66\x73\x0a\x20\x20\x20\x20\x20\x69\x64\
\x3d\x22\x64\x65\x66\x73\x32\x22\x3e\x0a\x20\x20\x20\x20\x3c\x6c\
\x69\x6e\x65\x61\x72\x47\x72\x61\x64\x69\x65\x6e\x74\x0a\x20\x20\
\x20\x20\x20\x20\x20\x69\x6e\x6b\x73\x63\x61\x70\x65\x3a\x63\x6f\
\x6c\x6c\x65\x63\x74\x3d\x22\x61\x6c\x77\x61\x79\x73\x22\x0a\x20\
\x20\x20\x20\x20\x20\x20\x69\x64\x3d\x22\x6c\x69\x6e\x65\x61\x72\
\x47\x72\x61\x64\x69\x65\x6e\x74\x34\x35\x33\x38\x22\x3e\x0a\x20\
\x20\x20\x20\x20\x20\x3c\x73\x74\x6f\x70\x0a\x20\x20\x20\x20\x20\
\x20\x20\x20\x20\x73\x74\x79\x6c\x65\x3d\x22\x73\x74\x6f\x70\x2d\
\x63\x6f\x6c\x6f\x72\x3a\x23\x66\x66\x66\x66\x66\x66\x3b\x73\x74\
\x6f\x70\x2d\x6f\x70\x61\x63\x69\x74\x79\x3a\x31\x22\x0a\x20\x20\
\x20\x20\x20\x20\x20\x20\x20\x6f\x66\x66\x73\x65\x74\x3d\x22\x30\
\x22\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x20\x69\x64\x3d\x22\x73\
\x74\x6f\x70\x34\x35\x33\x34\x22\x20\x2f\x3e\x0a\x20\x20\x20\x20\
\x20\x20\x3c\x73\x74\x6f\x70\x0a\x20\x20\x20\x20\x20\x20\x20\x20\
\x20\x73\x74\x79\x6c\x65\x3d\x22\x73\x74\x6f\x70\x2d\x63\x6f\x6c\
\x6f\x72\x3a\x23\x65\x30\x33\x66\x33\x66\x3b\x73\x74\x6f\x70\x2d\
\x6f\x70\x61\x63\x69\x74\x79\x3a\x31\x22\x0a\x20\x20\x20\x20\x20\
\x20\x20\x20\x20\x6f\x66\x66\x73\x65\x74\x3d\x22\x31\x22\x0a\x20\
\x20\x20\x20\x20\x20\x20\x20\x20\x69\x64\x3d\x22\x73\x74\x6f\x70\
\x34\x35\x33\x36\x22\x20\x2f\x3e\x0a\x20\x20\x20\x20\x3c\x2f\x6c\
\x69\x6e\x65\x61\x72\x47\x72\x61\x64\x69\x65\x6e\x74\x3e\x0a\x20\
\x20\x20\x20\x3c\x6c\x69\x6e\x65\x61\x72\x47\x72\x61\x64\x69\x65\
\x6e\x74\x0a\x20\x20\x20\x20\x20\x20\x20\x69\x6e\x6b\x73\x63\x61\
\x70\x65\x3a\x63\x6f\x6c\x6c\x65\x63\x74\x3d\x22\x61\x6c\x77\x61\
\x79\x73\x22\x0a\x20\x20\x20\x20\x20\x20\x20\x69\x64\x3d\x22\x6c\
\x69\x6e\x65\x61\x72\x47\x72\x61\x64\x69\x65\x6e\x74\x34\x35\x32\
\x38\x22\x3e\x0a\x20\x20\x20\x20\x20\x20\x3c\x73\x74\x6f\x70\x0a\
\x20\x20\x20\x20\x20\x20\x20\x20\x20\x73\x74\x79\x6c\x65\x3d\x22\
\x73\x74\x6f\x70\x2d\x63\x6f\x6c\x6f\x72\x3a\x23\x65\x30\x33\x66\
\x33\x66\x3b\x73\x74\x6f\x70\x2d\x6f\x70\x61\x63\x69\x74\x79\x3a\
\x31\x22\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x20\x6f\x66\x66\x73\
\x65\x74\x3d\x22\x30\x22\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x20\
\x69\x64\x3d\x22\x73\x74\x6f\x70\x34\x35\x32\x34\x22\x20\x2f\x3e\
\x0a\x20\x20\x20\x20\x20\x20\x3c\x73\x74\x6f\x70\x0a\x20\x20\x20\
\x20\x20\x20\x20\x20\x20\x73\x74\x79\x6c\x65\x3d\x22\x73\x74\x6f\
\x70\x2d\x63\x6f\x6c\x6f\x72\x3a\x23\x63\x30\x31\x66\x31\x66\x3b\
\x73\x74\x6f\x70\x2d\x6f\x70\x61\x63\x69\x74\x79\x3a\x31\x22\x0a\
\x20\x20\x20\x20\x20\x20\x20\x20\x20\x6f\x66\x66\x73\x65\x74\x3d\
\x22\x31\x22\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x20\x69\x64\x3d\
\x22\x73\x74\x6f\x70\x34\x35\x32\x36\x22\x20\x2f\x3e\x0a\x20\x20\
\x20\x20\x3c\x2f\x6c\x69\x6e\x65\x61\x72\x47\x72\x61\x64\x69\x65\
\x6e\x74\x3e\x0a\x20\x20\x20\x20\x3c\x6c\x69\x6e\x65\x61\x72\x47\
\x72\x61\x64\x69\x65\x6e\x74\x0a\x20\x20\x20\x20\x20\x20\x20\x69\
\x6e\x6b\x73\x63\x61\x70\x65\x3a\x63\x6f\x6c\x6c\x65\x63\x74\x3d\
\x22\x61\x6c\x77\x61\x79\x73\x22\x0a\x20\x20\x20\x20\x20\x20\x20\
\x78\x6c\x69\x6e\x6b\x3a\x68\x72\x65\x66\x3d\x22\x23\x6c\x69\x6e\
\x65\x61\x72\x47\x72\x61\x64\x69\x65\x6e\x74\x34\x35\x32\x38\x22\
\x0a\x20\x20\x20\x20\x20\x20\x20\x69\x64\x3d\x22\x6c\x69\x6e\x65\
\x61\x72\x47\x72\x61\x64\x69\x65\x6e\x74\x34\x35\x33\x30\x22\x0a\
\x20\x20\x20\x20\x20\x20\x20\x78\x31\x3d\x22\x38\x22\x0a\x20\x20\
\x20\x20\x20\x20\x20\x79\x31\x3d\x22\x32\x39\x35\x2e\x32\x39\x39\
\x39\x39\x22\x0a\x20\x20\x20\x20\x20\x20\x20\x78\x32\x3d\x22\x34\
\x30\x22\x0a\x20\x20\x20\x20\x20\x20\x20\x79\x32\x3d\x22\x33\x32\
\x31\x2e\x32\x39\x39\x39\x39\x22\x0a\x20\x20\x20\x20\x20\x20\x20\
\x67\x72\x61\x64\x69\x65\x6e\x74\x55\x6e\x69\x74\x73\x3d\x22\x75\
\x73\x65\x72\x53\x70\x61\x63\x65\x4f\x6e\x55\x73\x65\x22\x20\x2f\
\x3e\x0a\x20\x20\x20\x20\x3c\x6c\x69\x6e\x65\x61\x72\x47\x72\x61\
\x64\x69\x65\x6e\x74\x0a\x20\x20\x20\x20\x20\x20\x20\x69\x6e\x6b\
\x73\x63\x61\x70\x65\x3a\x63\x6f\x6c\x6c\x65\x63\x74\x3d\x22\x61\
\x6c\x77\x61\x79\x73\x22\x0a\x20\x20\x20\x20\x20\x20\x20\x78\x6c\
\x69\x6e\x6b\x3a\x68\x72\x65\x66\x3d\x22\x23\x6c\x69\x6e\x65\x61\
\x72\x47\x72\x61\x64\x69\x65\x6e\x74\x34\x35\x33\x38\x22\x0a\x20\
\x20\x20\x20\x20\x20\x20\x69\x64\x3d\x22\x6c\x69\x6e\x65\x61\x72\
\x47\x72\x61\x64\x69\x65\x6e\x74\x34\x35\x34\x30\x22\x0a\x20\x20\
\x20\x20\x20\x20\x20\x78\x31\x3d\x22\x36\x34\x22\x0a\x20\x20\x20\
\x20\x20\x20\x20\x79\x31\x3d\x22\x33\x30\x32\x2e\x32\x39\x39\x39\
\x39\x22\x0a\x20\x20\x20\x20\x20\x20\x20\x78\x32\x3d\x22\x36\x34\
\x22\x0a\x20\x20\x20\x20\x20\x20\x20\x79\x32\x3d\x22\x33\x31\x34\
\x2e\x32\x39\x39\x39\x39\x22\x0a\x20\x20\x20\x20\x20\x20\x20\x67\
\x72\x61\x64\x69\x65\x6e\x74\x55\x6e\x69\x74\x73\x3d\x22\x75\x73\
\x65\x72\x53\x70\x61\x63\x65\x4f\x6e\x55\x73\x65\x22\x0a\x20\x20\
\x20\x20\x20\x20\x20\x67\x72\x61\x64\x69\x65\x6e\x74\x54\x72\x61\
\x6e\x73\x66\x6f\x72\x6d\x3d\x22\x6d\x61\x74\x72\x69\x78\x28\x31\
\x2e\x35\x36\x30\x37\x35\x37\x36\x2c\x30\x2c\x30\x2c\x31\x2e\x35\
\x36\x30\x37\x35\x37\x36\x2c\x2d\x33\x30\x30\x2e\x38\x37\x37\x33\
\x34\x2c\x2d\x32\x35\x33\x2e\x35\x31\x36\x34\x37\x29\x22\x20\x2f\
\x3e\x0a\x20\x20\x3c\x2f\x64\x65\x66\x73\x3e\x0a\x20\x20\x3c\x73\
\x6f\x64\x69\x70\x6f\x64\x69\x3a\x6e\x61\x6d\x65\x64\x76\x69\x65\
\x77\x0a\x20\x20\x20\x20\x20\x69\x64\x3d\x22\x62\x61\x73\x65\x22\
\x0a\x20\x20\x20\x20\x20\x70\x61\x67\x65\x63\x6f\x6c\x6f\x72\x3d\
\x22\x23\x66\x66\x66\x66\x66\x66\x22\x0a\x20\x20\x20\x20\x20\x62\
\x6f\x72\x64\x65\x72\x63\x6f\x6c\x6f\x72\x3d\x22\x23\x36\x36\x36\
\x36\x36\x36\x22\x0a\x20\x20\x20\x20\x20\x62\x6f\x72\x64\x65\x72\
\x6f\x70\x61\x63\x69\x74\x79\x3d\x22\x31\x2e\x30\x22\x0a\x20\x20\
\x20\x20\x20\x69\x6e\x6b\x73\x63\x61\x70\x65\x3a\x70\x61\x67\x65\
\x6f\x70\x61\x63\x69\x74\x79\x3d\x22\x30\x2e\x30\x22\x0a\x20\x20\
\x20\x20\x20\x69\x6e\x6b\x73\x63\x61\x70\x65\x3a\x70\x61\x67\x65\
\x73\x68\x61\x64\x6f\x77\x3d\x22\x32\x22\x0a\x20\x20\x20\x20\x20\
\x69\x6e\x6b\x73\x63\x61\x70\x65\x3a\x7a\x6f\x6f\x6d\x3d\x22\x31\
\x36\x22\x0a\x20\x20\x20\x20\x20\x69\x6e\x6b\x73\x63\x61\x70\x65\
\x3a\x63\x78\x3d\x22\x32\x32\x2e\x31\x30\x36\x35\x34\x35\x22\x0a\
\x20\x20\x20\x20\x20\x69\x6e\x6b\x73\x63\x61\x70\x65\x3a\x63\x79\
\x3d\x22\x33\x30\x2e\x35\x34\x37\x34\x31\x34\x22\x0a\x20\x20\x20\
\x20\x20\x69\x6e\x6b\x73\x63\x61\x70\x65\x3a\x64\x6f\x63\x75\x6d\
\x65\x6e\x74\x2d\x75\x6e\x69\x74\x73\x3d\x22\x70\x78\x22\x0a\x20\
\x20\x20\x20\x20\x69\x6e\x6b\x73\x63\x61\x70\x65\x3a\x63\x75\x72\
\x72\x65\x6e\x74\x2d\x6c\x61\x79\x65\x72\x3d\x22\x6c\x61\x79\x65\
\x72\x31\x22\x0a\x20\x20\x20\x20\x20\x73\x68\x6f\x77\x67\x72\x69\
\x64\x3d\x22\x74\x72\x75\x65\x22\x0a\x20\x20\x20\x20\x20\x75\x6e\
\x69\x74\x73\x3d\x22\x70\x78\x22\x0a\x20\x20\x20\x20\x20\x69\x6e\
\x6b\x73\x63\x61\x70\x65\x3a\x77\x69\x6e\x64\x6f\x77\x2d\x77\x69\
\x64\x74\x68\x3d\x22\x31\x33\x36\x36\x22\x0a\x20\x20\x20\x20\x20\
\x69\x6e\x6b\x73\x63\x61\x70\x65\x3a\x77\x69\x6e\x64\x6f\x77\x2d\
\x68\x65\x69\x67\x68\x74\x3d\x22\x37\x33\x39\x22\x0a\x20\x20\x20\
\x20\x20\x69\x6e\x6b\x73\x63\x61\x70\x65\x3a\x77\x69\x6e\x64\x6f\
\x77\x2d\x78\x3d\x22\x30\x22\x0a\x20\x20\x20\x20\x20\x69\x6e\x6b\
\x73\x63\x61\x70\x65\x3a\x77\x69\x6e\x64\x6f\x77\x2d\x79\x3d\x22\
\x30\x22\x0a\x20\x20\x20\x20\x20\x69\x6e\x6b\x73\x63\x61\x70\x65\
\x3a\x77\x69\x6e\x64\x6f\x77\x2d\x6d\x61\x78\x69\x6d\x69\x7a\x65\
\x64\x3d\x22\x31\x22\x3e\x0a\x20\x20\x20\x20\x3c\x69\x6e\x6b\x73\
\x63\x61\x70\x65\x3a\x67\x72\x69\x64\x0a\x20\x20\x20\x20\x20\x20\
\x20\x74\x79\x70\x65\x3d\x22\x78\x79\x67\x72\x69\x64\x22\x0a\x20\
\x20\x20\x20\x20\x20\x20\x69\x64\x3d\x22\x67\x72\x69\x64\x33\x37\
\x31\x33\x22\x20\x2f\x3e\x0a\x20\x20\x3c\x2f\x73\x6f\x64\x69\x70\
\x6f\x64\x69\x3a\x6e\x61\x6d\x65\x64\x76\x69\x65\x77\x3e\x0a\x20\
\x20\x3c\x6d\x65\x74\x61\x64\x61\x74\x61\x0a\x20\x20\x20\x20\x20\
\x69\x64\x3d\x22\x6d\x65\x74\x61\x64\x61\x74\x61\x35\x22\x3e\x0a\
\x20\x20\x20\x20\x3c\x72\x64\x66\x3a\x52\x44\x46\x3e\x0a\x20\x20\
\x20\x20\x20\x20\x3c\x63\x63\x3a\x57\x6f\x72\x6b\x0a\x20\x20\x20\
\x20\x20\x20\x20\x20\x20\x72\x64\x66\x3a\x61\x62\x6f\x75\x74\x3d\
\x22\x22\x3e\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x3c\x64\x63\x3a\
\x66\x6f\x72\x6d\x61\x74\x3e\x69\x6d\x61\x67\x65\x2f\x73\x76\x67\
\x2b\x78\x6d\x6c\x3c\x2f\x64\x63\x3a\x66\x6f\x72\x6d\x61\x74\x3e\
\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x3c\x64\x63\x3a\x74\x79\x70\
\x65\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x72\x64\x66\
\x3a\x72\x65\x73\x6f\x75\x72\x63\x65\x3d\x22\x68\x74\x74\x70\x3a\
\x2f\x2f\x70\x75\x72\x6c\x2e\x6f\x72\x67\x2f\x64\x63\x2f\x64\x63\
\x6d\x69\x74\x79\x70\x65\x2f\x53\x74\x69\x6c\x6c\x49\x6d\x61\x67\
\x65\x22\x20\x2f\x3e\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x3c\x64\
\x63\x3a\x74\x69\x74\x6c\x65\x20\x2f\x3e\x0a\x20\x20\x20\x20\x20\
\x20\x3c\x2f\x63\x63\x3a\x57\x6f\x72\x6b\x3e\x0a\x20\x20\x20\x20\
\x3c\x2f\x72\x64\x66\x3a\x52\x44\x46\x3e\x0a\x20\x20\x3c\x2f\x6d\
\x65\x74\x61\x64\x61\x74\x61\x3e\x0a\x20\x20\x3c\x67\x0a\x20\x20\
\x20\x20\x20\x69\x6e\x6b\x73\x63\x61\x70\x65\x3a\x6c\x61\x62\x65\
\x6c\x3d\x22\x43\x61\x6c\x71\x75\x65\x20\x31\x22\x0a\x20\x20\x20\
\x20\x20\x69\x6e\x6b\x73\x63\x61\x70\x65\x3a\x67\x72\x6f\x75\x70\
\x6d\x6f\x64\x65\x3d\x22\x6c\x61\x79\x65\x72\x22\x0a\x20\x20\x20\
\x20\x20\x69\x64\x3d\x22\x6c\x61\x79\x65\x72\x31\x22\x0a\x20\x20\
\x20\x20\x20\x74\x72\x61\x6e\x73\x66\x6f\x72\x6d\x3d\x22\x74\x72\
\x61\x6e\x73\x6c\x61\x74\x65\x28\x30\x2c\x2d\x32\x38\x34\x2e\x32\
\x39\x39\x39\x39\x29\x22\x3e\x0a\x20\x20\x20\x20\x3c\x63\x69\x72\
\x63\x6c\x65\x0a\x20\x20\x20\x20\x20\x20\x20\x73\x74\x79\x6c\x65\
\x3d\x22\x66\x69\x6c\x6c\x3a\x23\x38\x30\x38\x30\x38\x30\x3b\x66\
\x69\x6c\x6c\x2d\x6f\x70\x61\x63\x69\x74\x79\x3a\x31\x3b\x73\x74\
\x72\x6f\x6b\x65\x3a\x6e\x6f\x6e\x65\x3b\x73\x74\x72\x6f\x6b\x65\
\x2d\x77\x69\x64\x74\x68\x3a\x32\x3b\x73\x74\x72\x6f\x6b\x65\x2d\
\x6c\x69\x6e\x65\x63\x61\x70\x3a\x72\x6f\x75\x6e\x64\x3b\x73\x74\
\x72\x6f\x6b\x65\x2d\x6c\x69\x6e\x65\x6a\x6f\x69\x6e\x3a\x72\x6f\
\x75\x6e\x64\x3b\x73\x74\x72\x6f\x6b\x65\x2d\x6d\x69\x74\x65\x72\
\x6c\x69\x6d\x69\x74\x3a\x34\x3b\x73\x74\x72\x6f\x6b\x65\x2d\x64\
\x61\x73\x68\x61\x72\x72\x61\x79\x3a\x6e\x6f\x6e\x65\x3b\x73\x74\
\x72\x6f\x6b\x65\x2d\x6f\x70\x61\x63\x69\x74\x79\x3a\x31\x22\x0a\
\x20\x20\x20\x20\x20\x20\x20\x69\x64\x3d\x22\x70\x61\x74\x68\x33\
\x37\x31\x35\x22\x0a\x20\x20\x20\x20\x20\x20\x20\x63\x78\x3d\x22\
\x32\x34\x22\x0a\x20\x20\x20\x20\x20\x20\x20\x63\x79\x3d\x22\x33\
\x30\x38\x2e\x32\x39\x39\x39\x39\x22\x0a\x20\x20\x20\x20\x20\x20\
\x20\x72\x3d\x22\x32\x34\x22\x20\x2f\x3e\x0a\x20\x20\x20\x20\x3c\
\x63\x69\x72\x63\x6c\x65\x0a\x20\x20\x20\x20\x20\x20\x20\x73\x74\
\x79\x6c\x65\x3d\x22\x66\x69\x6c\x6c\x3a\x75\x72\x6c\x28\x23\x6c\
\x69\x6e\x65\x61\x72\x47\x72\x61\x64\x69\x65\x6e\x74\x34\x35\x33\
\x30\x29\x3b\x66\x69\x6c\x6c\x2d\x6f\x70\x61\x63\x69\x74\x79\x3a\
\x31\x3b\x73\x74\x72\x6f\x6b\x65\x3a\x6e\x6f\x6e\x65\x3b\x73\x74\
\x72\x6f\x6b\x65\x2d\x77\x69\x64\x74\x68\x3a\x32\x3b\x73\x74\x72\
\x6f\x6b\x65\x2d\x6c\x69\x6e\x65\x63\x61\x70\x3a\x72\x6f\x75\x6e\
\x64\x3b\x73\x74\x72\x6f\x6b\x65\x2d\x6c\x69\x6e\x65\x6a\x6f\x69\
\x6e\x3a\x72\x6f\x75\x6e\x64\x3b\x73\x74\x72\x6f\x6b\x65\x2d\x6d\
\x69\x74\x65\x72\x6c\x69\x6d\x69\x74\x3a\x34\x3b\x73\x74\x72\x6f\
\x6b\x65\x2d\x64\x61\x73\x68\x61\x72\x72\x61\x79\x3a\x6e\x6f\x6e\
\x65\x3b\x73\x74\x72\x6f\x6b\x65\x2d\x6f\x70\x61\x63\x69\x74\x79\
\x3a\x31\x22\x0a\x20\x20\x20\x20\x20\x20\x20\x69\x64\x3d\x22\x70\
\x61\x74\x68\x34\x35\x32\x32\x22\x0a\x20\x20\x20\x20\x20\x20\x20\
\x63\x78\x3d\x22\x32\x34\x22\x0a\x20\x20\x20\x20\x20\x20\x20\x63\
\x79\x3d\x22\x33\x30\x38\x2e\x32\x39\x39\x39\x39\x22\x0a\x20\x20\
\x20\x20\x20\x20\x20\x72\x3d\x22\x32\x30\x22\x20\x2f\x3e\x0a\x20\
\x20\x20\x20\x3c\x65\x6c\x6c\x69\x70\x73\x65\x0a\x20\x20\x20\x20\
\x20\x20\x20\x73\x74\x79\x6c\x65\x3d\x22\x66\x69\x6c\x6c\x3a\x75\
\x72\x6c\x28\x23\x6c\x69\x6e\x65\x61\x72\x47\x72\x61\x64\x69\x65\
\x6e\x74\x34\x35\x34\x30\x29\x3b\x66\x69\x6c\x6c\x2d\x6f\x70\x61\
\x63\x69\x74\x79\x3a\x31\x3b\x73\x74\x72\x6f\x6b\x65\x3a\x6e\x6f\
\x6e\x65\x3b\x73\x74\x72\x6f\x6b\x65\x2d\x77\x69\x64\x74\x68\x3a\
\x31\x2e\x39\x39\x39\x39\x39\x39\x37\x36\x3b\x73\x74\x72\x6f\x6b\
\x65\x2d\x6c\x69\x6e\x65\x63\x61\x70\x3a\x72\x6f\x75\x6e\x64\x3b\
\x73\x74\x72\x6f\x6b\x65\x2d\x6c\x69\x6e\x65\x6a\x6f\x69\x6e\x3a\
\x72\x6f\x75\x6e\x64\x3b\x73\x74\x72\x6f\x6b\x65\x2d\x6d\x69\x74\
\x65\x72\x6c\x69\x6d\x69\x74\x3a\x34\x3b\x73\x74\x72\x6f\x6b\x65\
\x2d\x64\x61\x73\x68\x61\x72\x72\x61\x79\x3a\x6e\x6f\x6e\x65\x3b\
\x73\x74\x72\x6f\x6b\x65\x2d\x6f\x70\x61\x63\x69\x74\x79\x3a\x31\
\x22\x0a\x20\x20\x20\x20\x20\x20\x20\x69\x64\x3d\x22\x70\x61\x74\
\x68\x34\x35\x33\x32\x22\x0a\x20\x20\x20\x20\x20\x20\x20\x63\x78\
\x3d\x22\x2d\x32\x30\x30\x2e\x39\x38\x38\x38\x35\x22\x0a\x20\x20\
\x20\x20\x20\x20\x20\x63\x79\x3d\x22\x32\x32\x37\x2e\x37\x33\x32\
\x38\x38\x22\x0a\x20\x20\x20\x20\x20\x20\x20\x72\x78\x3d\x22\x31\
\x34\x2e\x30\x34\x36\x38\x31\x38\x22\x0a\x20\x20\x20\x20\x20\x20\
\x20\x72\x79\x3d\x22\x39\x2e\x33\x36\x34\x35\x34\x35\x38\x22\x0a\
\x20\x20\x20\x20\x20\x20\x20\x74\x72\x61\x6e\x73\x66\x6f\x72\x6d\
\x3d\x22\x72\x6f\x74\x61\x74\x65\x28\x2d\x34\x35\x29\x22\x20\x2f\
\x3e\x0a\x20\x20\x3c\x2f\x67\x3e\x0a\x3c\x2f\x73\x76\x67\x3e\x0a\
\
\x00\x00\x0f\x04\
\x3c\
\x3f\x78\x6d\x6c\x20\x76\x65\x72\x73\x69\x6f\x6e\x3d\x22\x31\x2e\
\x30\x22\x20\x65\x6e\x63\x6f\x64\x69\x6e\x67\x3d\x22\x55\x54\x46\
\x2d\x38\x22\x20\x73\x74\x61\x6e\x64\x61\x6c\x6f\x6e\x65\x3d\x22\
\x6e\x6f\x22\x3f\x3e\x0a\x3c\x21\x2d\x2d\x20\x43\x72\x65\x61\x74\
\x65\x64\x20\x77\x69\x74\x68\x20\x49\x6e\x6b\x73\x63\x61\x70\x65\
\x20\x28\x68\x74\x74\x70\x3a\x2f\x2f\x77\x77\x77\x2e\x69\x6e\x6b\
\x73\x63\x61\x70\x65\x2e\x6f\x72\x67\x2f\x29\x20\x2d\x2d\x3e\x0a\
\x0a\x3c\x73\x76\x67\x0a\x20\x20\x20\x78\x6d\x6c\x6e\x73\x3a\x64\
\x63\x3d\x22\x68\x74\x74\x70\x3a\x2f\x2f\x70\x75\x72\x6c\x2e\x6f\
\x72\x67\x2f\x64\x63\x2f\x65\x6c\x65\x6d\x65\x6e\x74\x73\x2f\x31\
\x2e\x31\x2f\x22\x0a\x20\x20\x20\x78\x6d\x6c\x6e\x73\x3a\x63\x63\
\x3d\x22\x68\x74\x74\x70\x3a\x2f\x2f\x63\x72\x65\x61\x74\x69\x76\
\x65\x63\x6f\x6d\x6d\x6f\x6e\x73\x2e\x6f\x72\x67\x2f\x6e\x73\x23\
\x22\x0a\x20\x20\x20\x78\x6d\x6c\x6e\x73\x3a\x72\x64\x66\x3d\x22\
\x68\x74\x74\x70\x3a\x2f\x2f\x77\x77\x77\x2e\x77\x33\x2e\x6f\x72\
\x67\x2f\x31\x39\x39\x39\x2f\x30\x32\x2f\x32\x32\x2d\x72\x64\x66\
\x2d\x73\x79\x6e\x74\x61\x78\x2d\x6e\x73\x23\x22\x0a\x20\x20\x20\
\x78\x6d\x6c\x6e\x73\x3a\x73\x76\x67\x3d\x22\x68\x74\x74\x70\x3a\
\x2f\x2f\x77\x77\x77\x2e\x77\x33\x2e\x6f\x72\x67\x2f\x32\x30\x30\
\x30\x2f\x73\x76\x67\x22\x0a\x20\x20\x20\x78\x6d\x6c\x6e\x73\x3d\
\x22\x68\x74\x74\x70\x3a\x2f\x2f\x77\x77\x77\x2e\x77\x33\x2e\x6f\
\x72\x67\x2f\x32\x30\x30\x30\x2f\x73\x76\x67\x22\x0a\x20\x20\x20\
\x78\x6d\x6c\x6e\x73\x3a\x78\x6c\x69\x6e\x6b\x3d\x22\x68\x74\x74\
\x70\x3a\x2f\x2f\x77\x77\x77\x2e\x77\x33\x2e\x6f\x72\x67\x2f\x31\
\x39\x39\x39\x2f\x78\x6c\x69\x6e\x6b\x22\x0a\x20\x20\x20\x78\x6d\
\x6c\x6e\x73\x3a\x73\x6f\x64\x69\x70\x6f\x64\x69\x3d\x22\x68\x74\
\x74\x70\x3a\x2f\x2f\x73\x6f\x64\x69\x70\x6f\x64\x69\x2e\x73\x6f\
\x75\x72\x63\x65\x66\x6f\x72\x67\x65\x2e\x6e\x65\x74\x2f\x44\x54\
\x44\x2f\x73\x6f\x64\x69\x70\x6f\x64\x69\x2d\x30\x2e\x64\x74\x64\
\x22\x0a\x20\x20\x20\x78\x6d\x6c\x6e\x73\x3a\x69\x6e\x6b\x73\x63\
\x61\x70\x65\x3d\x22\x68\x74\x74\x70\x3a\x2f\x2f\x77\x77\x77\x2e\
\x69\x6e\x6b\x73\x63\x61\x70\x65\x2e\x6f\x72\x67\x2f\x6e\x61\x6d\
\x65\x73\x70\x61\x63\x65\x73\x2f\x69\x6e\x6b\x73\x63\x61\x70\x65\
\x22\x0a\x20\x20\x20\x77\x69\x64\x74\x68\x3d\x22\x34\x38\x22\x0a\
\x20\x20\x20\x68\x65\x69\x67\x68\x74\x3d\x22\x34\x38\x22\x0a\x20\
\x20\x20\x76\x69\x65\x77\x42\x6f\x78\x3d\x22\x30\x20\x30\x20\x34\
\x38\x20\x34\x38\x22\x0a\x20\x20\x20\x76\x65\x72\x73\x69\x6f\x6e\
\x3d\x22\x31\x2e\x31\x22\x0a\x20\x20\x20\x69\x64\x3d\x22\x73\x76\
\x67\x38\x22\x0a\x20\x20\x20\x69\x6e\x6b\x73\x63\x61\x70\x65\x3a\
\x76\x65\x72\x73\x69\x6f\x6e\x3d\x22\x30\x2e\x39\x32\x2e\x33\x20\
\x28\x32\x34\x30\x35\x35\x34\x36\x2c\x20\x32\x30\x31\x38\x2d\x30\
\x33\x2d\x31\x31\x29\x22\x0a\x20\x20\x20\x73\x6f\x64\x69\x70\x6f\
\x64\x69\x3a\x64\x6f\x63\x6e\x61\x6d\x65\x3d\x22\x6c\x65\x64\x52\
\x6f\x75\x67\x65\x45\x74\x65\x69\x6e\x74\x65\x2e\x73\x76\x67\x22\
\x3e\x0a\x20\x20\x3c\x64\x65\x66\x73\x0a\x20\x20\x20\x20\x20\x69\
\x64\x3d\x22\x64\x65\x66\x73\x32\x22\x3e\x0a\x20\x20\x20\x20\x3c\
\x6c\x69\x6e\x65\x61\x72\x47\x72\x61\x64\x69\x65\x6e\x74\x0a\x20\
\x20\x20\x20\x20\x20\x20\x69\x6e\x6b\x73\x63\x61\x70\x65\x3a\x63\
\x6f\x6c\x6c\x65\x63\x74\x3d\x22\x61\x6c\x77\x61\x79\x73\x22\x0a\
\x20\x20\x20\x20\x20\x20\x20\x69\x64\x3d\x22\x6c\x69\x6e\x65\x61\
\x72\x47\x72\x61\x64\x69\x65\x6e\x74\x34\x35\x33\x38\x22\x3e\x0a\
\x20\x20\x20\x20\x20\x20\x3c\x73\x74\x6f\x70\x0a\x20\x20\x20\x20\
\x20\x20\x20\x20\x20\x73\x74\x79\x6c\x65\x3d\x22\x73\x74\x6f\x70\
\x2d\x63\x6f\x6c\x6f\x72\x3a\x23\x66\x66\x66\x66\x66\x66\x3b\x73\
\x74\x6f\x70\x2d\x6f\x70\x61\x63\x69\x74\x79\x3a\x31\x22\x0a\x20\
\x20\x20\x20\x20\x20\x20\x20\x20\x6f\x66\x66\x73\x65\x74\x3d\x22\
\x30\x22\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x20\x69\x64\x3d\x22\
\x73\x74\x6f\x70\x34\x35\x33\x34\x22\x20\x2f\x3e\x0a\x20\x20\x20\
\x20\x20\x20\x3c\x73\x74\x6f\x70\x0a\x20\x20\x20\x20\x20\x20\x20\
\x20\x20\x73\x74\x79\x6c\x65\x3d\x22\x73\x74\x6f\x70\x2d\x63\x6f\
\x6c\x6f\x72\x3a\x23\x38\x30\x30\x30\x30\x30\x3b\x73\x74\x6f\x70\
\x2d\x6f\x70\x61\x63\x69\x74\x79\x3a\x31\x22\x0a\x20\x20\x20\x20\
\x20\x20\x20\x20\x20\x6f\x66\x66\x73\x65\x74\x3d\x22\x31\x22\x0a\
\x20\x20\x20\x20\x20\x20\x20\x20\x20\x69\x64\x3d\x22\x73\x74\x6f\
\x70\x34\x35\x33\x36\x22\x20\x2f\x3e\x0a\x20\x20\x20\x20\x3c\x2f\
\x6c\x69\x6e\x65\x61\x72\x47\x72\x61\x64\x69\x65\x6e\x74\x3e\x0a\
\x20\x20\x20\x20\x3c\x6c\x69\x6e\x65\x61\x72\x47\x72\x61\x64\x69\
\x65\x6e\x74\x0a\x20\x20\x20\x20\x20\x20\x20\x69\x6e\x6b\x73\x63\
\x61\x70\x65\x3a\x63\x6f\x6c\x6c\x65\x63\x74\x3d\x22\x61\x6c\x77\
\x61\x79\x73\x22\x0a\x20\x20\x20\x20\x20\x20\x20\x69\x64\x3d\x22\
\x6c\x69\x6e\x65\x61\x72\x47\x72\x61\x64\x69\x65\x6e\x74\x34\x35\
\x32\x38\x22\x3e\x0a\x20\x20\x20\x20\x20\x20\x3c\x73\x74\x6f\x70\
\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x20\x73\x74\x79\x6c\x65\x3d\
\x22\x73\x74\x6f\x70\x2d\x63\x6f\x6c\x6f\x72\x3a\x23\x37\x66\x30\
\x30\x30\x30\x3b\x73\x74\x6f\x70\x2d\x6f\x70\x61\x63\x69\x74\x79\
\x3a\x31\x3b\x22\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x20\x6f\x66\
\x66\x73\x65\x74\x3d\x22\x30\x22\x0a\x20\x20\x20\x20\x20\x20\x20\
\x20\x20\x69\x64\x3d\x22\x73\x74\x6f\x70\x34\x35\x32\x34\x22\x20\
\x2f\x3e\x0a\x20\x20\x20\x20\x20\x20\x3c\x73\x74\x6f\x70\x0a\x20\
\x20\x20\x20\x20\x20\x20\x20\x20\x73\x74\x79\x6c\x65\x3d\x22\x73\
\x74\x6f\x70\x2d\x63\x6f\x6c\x6f\x72\x3a\x23\x32\x30\x30\x30\x30\
\x30\x3b\x73\x74\x6f\x70\x2d\x6f\x70\x61\x63\x69\x74\x79\x3a\x31\
\x22\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x20\x6f\x66\x66\x73\x65\
\x74\x3d\x22\x31\x22\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x20\x69\
\x64\x3d\x22\x73\x74\x6f\x70\x34\x35\x32\x36\x22\x20\x2f\x3e\x0a\
\x20\x20\x20\x20\x3c\x2f\x6c\x69\x6e\x65\x61\x72\x47\x72\x61\x64\
\x69\x65\x6e\x74\x3e\x0a\x20\x20\x20\x20\x3c\x6c\x69\x6e\x65\x61\
\x72\x47\x72\x61\x64\x69\x65\x6e\x74\x0a\x20\x20\x20\x20\x20\x20\
\x20\x69\x6e\x6b\x73\x63\x61\x70\x65\x3a\x63\x6f\x6c\x6c\x65\x63\
\x74\x3d\x22\x61\x6c\x77\x61\x79\x73\x22\x0a\x20\x20\x20\x20\x20\
\x20\x20\x78\x6c\x69\x6e\x6b\x3a\x68\x72\x65\x66\x3d\x22\x23\x6c\
\x69\x6e\x65\x61\x72\x47\x72\x61\x64\x69\x65\x6e\x74\x34\x35\x32\
\x38\x22\x0a\x20\x20\x20\x20\x20\x20\x20\x69\x64\x3d\x22\x6c\x69\
\x6e\x65\x61\x72\x47\x72\x61\x64\x69\x65\x6e\x74\x34\x35\x33\x30\
\x22\x0a\x20\x20\x20\x20\x20\x20\x20\x78\x31\x3d\x22\x38\x22\x0a\
\x20\x20\x20\x20\x20\x20\x20\x79\x31\x3d\x22\x32\x39\x35\x2e\x32\
\x39\x39\x39\x39\x22\x0a\x20\x20\x20\x20\x20\x20\x20\x78\x32\x3d\
\x22\x34\x30\x22\x0a\x20\x20\x20\x20\x20\x20\x20\x79\x32\x3d\x22\
\x33\x32\x31\x2e\x32\x39\x39\x39\x39\x22\x0a\x20\x20\x20\x20\x20\
\x20\x20\x67\x72\x61\x64\x69\x65\x6e\x74\x55\x6e\x69\x74\x73\x3d\
\x22\x75\x73\x65\x72\x53\x70\x61\x63\x65\x4f\x6e\x55\x73\x65\x22\
\x20\x2f\x3e\x0a\x20\x20\x20\x20\x3c\x6c\x69\x6e\x65\x61\x72\x47\
\x72\x61\x64\x69\x65\x6e\x74\x0a\x20\x20\x20\x20\x20\x20\x20\x69\
\x6e\x6b\x73\x63\x61\x70\x65\x3a\x63\x6f\x6c\x6c\x65\x63\x74\x3d\
\x22\x61\x6c\x77\x61\x79\x73\x22\x0a\x20\x20\x20\x20\x20\x20\x20\
\x78\x6c\x69\x6e\x6b\x3a\x68\x72\x65\x66\x3d\x22\x23\x6c\x69\x6e\
\x65\x61\x72\x47\x72\x61\x64\x69\x65\x6e\x74\x34\x35\x33\x38\x22\
\x0a\x20\x20\x20\x20\x20\x20\x20\x69\x64\x3d\x22\x6c\x69\x6e\x65\
\x61\x72\x47\x72\x61\x64\x69\x65\x6e\x74\x34\x35\x34\x30\x22\x0a\
\x20\x20\x20\x20\x20\x20\x20\x78\x31\x3d\x22\x36\x34\x22\x0a\x20\
\x20\x20\x20\x20\x20\x20\x79\x31\x3d\x22\x33\x30\x32\x2e\x32\x39\
\x39\x39\x39\x22\x0a\x20\x20\x20\x20\x20\x20\x20\x78\x32\x3d\x22\
\x36\x34\x22\x0a\x20\x20\x20\x20\x20\x20\x20\x79\x32\x3d\x22\x33\
\x31\x34\x2e\x32\x39\x39\x39\x39\x22\x0a\x20\x20\x20\x20\x20\x20\
\x20\x67\x72\x61\x64\x69\x65\x6e\x74\x55\x6e\x69\x74\x73\x3d\x22\
\x75\x73\x65\x72\x53\x70\x61\x63\x65\x4f\x6e\x55\x73\x65\x22\x0a\
\x20\x20\x20\x20\x20\x20\x20\x67\x72\x61\x64\x69\x65\x6e\x74\x54\
\x72\x61\x6e\x73\x66\x6f\x72\x6d\x3d\x22\x74\x72\x61\x6e\x73\x6c\
\x61\x74\x65\x28\x2d\x32\x36\x35\x2e\x30\x34\x33\x39\x37\x2c\x2d\
\x38\x35\x2e\x31\x31\x38\x33\x36\x31\x29\x22\x20\x2f\x3e\x0a\x20\
\x20\x3c\x2f\x64\x65\x66\x73\x3e\x0a\x20\x20\x3c\x73\x6f\x64\x69\
\x70\x6f\x64\x69\x3a\x6e\x61\x6d\x65\x64\x76\x69\x65\x77\x0a\x20\
\x20\x20\x20\x20\x69\x64\x3d\x22\x62\x61\x73\x65\x22\x0a\x20\x20\
\x20\x20\x20\x70\x61\x67\x65\x63\x6f\x6c\x6f\x72\x3d\x22\x23\x66\
\x66\x66\x66\x66\x66\x22\x0a\x20\x20\x20\x20\x20\x62\x6f\x72\x64\
\x65\x72\x63\x6f\x6c\x6f\x72\x3d\x22\x23\x36\x36\x36\x36\x36\x36\
\x22\x0a\x20\x20\x20\x20\x20\x62\x6f\x72\x64\x65\x72\x6f\x70\x61\
\x63\x69\x74\x79\x3d\x22\x31\x2e\x30\x22\x0a\x20\x20\x20\x20\x20\
\x69\x6e\x6b\x73\x63\x61\x70\x65\x3a\x70\x61\x67\x65\x6f\x70\x61\
\x63\x69\x74\x79\x3d\x22\x30\x2e\x30\x22\x0a\x20\x20\x20\x20\x20\
\x69\x6e\x6b\x73\x63\x61\x70\x65\x3a\x70\x61\x67\x65\x73\x68\x61\
\x64\x6f\x77\x3d\x22\x32\x22\x0a\x20\x20\x20\x20\x20\x69\x6e\x6b\
\x73\x63\x61\x70\x65\x3a\x7a\x6f\x6f\x6d\x3d\x22\x35\x2e\x36\x35\
\x36\x38\x35\x34\x32\x22\x0a\x20\x20\x20\x20\x20\x69\x6e\x6b\x73\
\x63\x61\x70\x65\x3a\x63\x78\x3d\x22\x32\x33\x2e\x37\x32\x32\x37\
\x32\x32\x22\x0a\x20\x20\x20\x20\x20\x69\x6e\x6b\x73\x63\x61\x70\
\x65\x3a\x63\x79\x3d\x22\x32\x38\x2e\x32\x30\x30\x37\x33\x22\x0a\
\x20\x20\x20\x20\x20\x69\x6e\x6b\x73\x63\x61\x70\x65\x3a\x64\x6f\
\x63\x75\x6d\x65\x6e\x74\x2d\x75\x6e\x69\x74\x73\x3d\x22\x70\x78\
\x22\x0a\x20\x20\x20\x20\x20\x69\x6e\x6b\x73\x63\x61\x70\x65\x3a\
\x63\x75\x72\x72\x65\x6e\x74\x2d\x6c\x61\x79\x65\x72\x3d\x22\x6c\
\x61\x79\x65\x72\x31\x22\x0a\x20\x20\x20\x20\x20\x73\x68\x6f\x77\
\x67\x72\x69\x64\x3d\x22\x74\x72\x75\x65\x22\x0a\x20\x20\x20\x20\
\x20\x75\x6e\x69\x74\x73\x3d\x22\x70\x78\x22\x0a\x20\x20\x20\x20\
\x20\x69\x6e\x6b\x73\x63\x61\x70\x65\x3a\x77\x69\x6e\x64\x6f\x77\
\x2d\x77\x69\x64\x74\x68\x3d\x22\x31\x33\x36\x36\x22\x0a\x20\x20\
\x20\x20\x20\x69\x6e\x6b\x73\x63\x61\x70\x65\x3a\x77\x69\x6e\x64\
\x6f\x77\x2d\x68\x65\x69\x67\x68\x74\x3d\x22\x37\x33\x39\x22\x0a\
\x20\x20\x20\x20\x20\x69\x6e\x6b\x73\x63\x61\x70\x65\x3a\x77\x69\
\x6e\x64\x6f\x77\x2d\x78\x3d\x22\x30\x22\x0a\x20\x20\x20\x20\x20\
\x69\x6e\x6b\x73\x63\x61\x70\x65\x3a\x77\x69\x6e\x64\x6f\x77\x2d\
\x79\x3d\x22\x30\x22\x0a\x20\x20\x20\x20\x20\x69\x6e\x6b\x73\x63\
\x61\x70\x65\x3a\x77\x69\x6e\x64\x6f\x77\x2d\x6d\x61\x78\x69\x6d\
\x69\x7a\x65\x64\x3d\x22\x31\x22\x3e\x0a\x20\x20\x20\x20\x3c\x69\
\x6e\x6b\x73\x63\x61\x70\x65\x3a\x67\x72\x69\x64\x0a\x20\x20\x20\
\x20\x20\x20\x20\x74\x79\x70\x65\x3d\x22\x78\x79\x67\x72\x69\x64\
\x22\x0a\x20\x20\x20\x20\x20\x20\x20\x69\x64\x3d\x22\x67\x72\x69\
\x64\x33\x37\x31\x33\x22\x20\x2f\x3e\x0a\x20\x20\x3c\x2f\x73\x6f\
\x64\x69\x70\x6f\x64\x69\x3a\x6e\x61\x6d\x65\x64\x76\x69\x65\x77\
\x3e\x0a\x20\x20\x3c\x6d\x65\x74\x61\x64\x61\x74\x61\x0a\x20\x20\
\x20\x20\x20\x69\x64\x3d\x22\x6d\x65\x74\x61\x64\x61\x74\x61\x35\
\x22\x3e\x0a\x20\x20\x20\x20\x3c\x72\x64\x66\x3a\x52\x44\x46\x3e\
\x0a\x20\x20\x20\x20\x20\x20\x3c\x63\x63\x3a\x57\x6f\x72\x6b\x0a\
\x20\x20\x20\x20\x20\x20\x20\x20\x20\x72\x64\x66\x3a\x61\x62\x6f\
\x75\x74\x3d\x22\x22\x3e\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x3c\
\x64\x63\x3a\x66\x6f\x72\x6d\x61\x74\x3e\x69\x6d\x61\x67\x65\x2f\
\x73\x76\x67\x2b\x78\x6d\x6c\x3c\x2f\x64\x63\x3a\x66\x6f\x72\x6d\
\x61\x74\x3e\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x3c\x64\x63\x3a\
\x74\x79\x70\x65\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\
\x72\x64\x66\x3a\x72\x65\x73\x6f\x75\x72\x63\x65\x3d\x22\x68\x74\
\x74\x70\x3a\x2f\x2f\x70\x75\x72\x6c\x2e\x6f\x72\x67\x2f\x64\x63\
\x2f\x64\x63\x6d\x69\x74\x79\x70\x65\x2f\x53\x74\x69\x6c\x6c\x49\
\x6d\x61\x67\x65\x22\x20\x2f\x3e\x0a\x20\x20\x20\x20\x20\x20\x20\
\x20\x3c\x64\x63\x3a\x74\x69\x74\x6c\x65\x20\x2f\x3e\x0a\x20\x20\
\x20\x20\x20\x20\x3c\x2f\x63\x63\x3a\x57\x6f\x72\x6b\x3e\x0a\x20\
\x20\x20\x20\x3c\x2f\x72\x64\x66\x3a\x52\x44\x46\x3e\x0a\x20\x20\
\x3c\x2f\x6d\x65\x74\x61\x64\x61\x74\x61\x3e\x0a\x20\x20\x3c\x67\
\x0a\x20\x20\x20\x20\x20\x69\x6e\x6b\x73\x63\x61\x70\x65\x3a\x6c\
\x61\x62\x65\x6c\x3d\x22\x43\x61\x6c\x71\x75\x65\x20\x31\x22\x0a\
\x20\x20\x20\x20\x20\x69\x6e\x6b\x73\x63\x61\x70\x65\x3a\x67\x72\
\x6f\x75\x70\x6d\x6f\x64\x65\x3d\x22\x6c\x61\x79\x65\x72\x22\x0a\
\x20\x20\x20\x20\x20\x69\x64\x3d\x22\x6c\x61\x79\x65\x72\x31\x22\
\x0a\x20\x20\x20\x20\x20\x74\x72\x61\x6e\x73\x66\x6f\x72\x6d\x3d\
\x22\x74\x72\x61\x6e\x73\x6c\x61\x74\x65\x28\x30\x2c\x2d\x32\x38\
\x34\x2e\x32\x39\x39\x39\x39\x29\x22\x3e\x0a\x20\x20\x20\x20\x3c\
\x63\x69\x72\x63\x6c\x65\x0a\x20\x20\x20\x20\x20\x20\x20\x73\x74\
\x79\x6c\x65\x3d\x22\x66\x69\x6c\x6c\x3a\x23\x35\x63\x35\x63\x35\
\x63\x3b\x66\x69\x6c\x6c\x2d\x6f\x70\x61\x63\x69\x74\x79\x3a\x31\
\x3b\x73\x74\x72\x6f\x6b\x65\x3a\x6e\x6f\x6e\x65\x3b\x73\x74\x72\
\x6f\x6b\x65\x2d\x77\x69\x64\x74\x68\x3a\x32\x3b\x73\x74\x72\x6f\
\x6b\x65\x2d\x6c\x69\x6e\x65\x63\x61\x70\x3a\x72\x6f\x75\x6e\x64\
\x3b\x73\x74\x72\x6f\x6b\x65\x2d\x6c\x69\x6e\x65\x6a\x6f\x69\x6e\
\x3a\x72\x6f\x75\x6e\x64\x3b\x73\x74\x72\x6f\x6b\x65\x2d\x6d\x69\
\x74\x65\x72\x6c\x69\x6d\x69\x74\x3a\x34\x3b\x73\x74\x72\x6f\x6b\
\x65\x2d\x64\x61\x73\x68\x61\x72\x72\x61\x79\x3a\x6e\x6f\x6e\x65\
\x3b\x73\x74\x72\x6f\x6b\x65\x2d\x6f\x70\x61\x63\x69\x74\x79\x3a\
\x31\x22\x0a\x20\x20\x20\x20\x20\x20\x20\x69\x64\x3d\x22\x70\x61\
\x74\x68\x33\x37\x31\x35\x22\x0a\x20\x20\x20\x20\x20\x20\x20\x63\
\x78\x3d\x22\x32\x34\x22\x0a\x20\x20\x20\x20\x20\x20\x20\x63\x79\
\x3d\x22\x33\x30\x38\x2e\x32\x39\x39\x39\x39\x22\x0a\x20\x20\x20\
\x20\x20\x20\x20\x72\x3d\x22\x32\x34\x22\x20\x2f\x3e\x0a\x20\x20\
\x20\x20\x3c\x63\x69\x72\x63\x6c\x65\x0a\x20\x20\x20\x20\x20\x20\
\x20\x73\x74\x79\x6c\x65\x3d\x22\x66\x69\x6c\x6c\x3a\x75\x72\x6c\
\x28\x23\x6c\x69\x6e\x65\x61\x72\x47\x72\x61\x64\x69\x65\x6e\x74\
\x34\x35\x33\x30\x29\x3b\x66\x69\x6c\x6c\x2d\x6f\x70\x61\x63\x69\
\x74\x79\x3a\x31\x3b\x73\x74\x72\x6f\x6b\x65\x3a\x6e\x6f\x6e\x65\
\x3b\x73\x74\x72\x6f\x6b\x65\x2d\x77\x69\x64\x74\x68\x3a\x32\x3b\
\x73\x74\x72\x6f\x6b\x65\x2d\x6c\x69\x6e\x65\x63\x61\x70\x3a\x72\
\x6f\x75\x6e\x64\x3b\x73\x74\x72\x6f\x6b\x65\x2d\x6c\x69\x6e\x65\
\x6a\x6f\x69\x6e\x3a\x72\x6f\x75\x6e\x64\x3b\x73\x74\x72\x6f\x6b\
\x65\x2d\x6d\x69\x74\x65\x72\x6c\x69\x6d\x69\x74\x3a\x34\x3b\x73\
\x74\x72\x6f\x6b\x65\x2d\x64\x61\x73\x68\x61\x72\x72\x61\x79\x3a\
\x6e\x6f\x6e\x65\x3b\x73\x74\x72\x6f\x6b\x65\x2d\x6f\x70\x61\x63\
\x69\x74\x79\x3a\x31\x22\x0a\x20\x20\x20\x20\x20\x20\x20\x69\x64\
\x3d\x22\x70\x61\x74\x68\x34\x35\x32\x32\x22\x0a\x20\x20\x20\x20\
\x20\x20\x20\x63\x78\x3d\x22\x32\x34\x22\x0a\x20\x20\x20\x20\x20\
\x20\x20\x63\x79\x3d\x22\x33\x30\x38\x2e\x32\x39\x39\x39\x39\x22\
\x0a\x20\x20\x20\x20\x20\x20\x20\x72\x3d\x22\x32\x30\x22\x20\x2f\
\x3e\x0a\x20\x20\x20\x20\x3c\x65\x6c\x6c\x69\x70\x73\x65\x0a\x20\
\x20\x20\x20\x20\x20\x20\x73\x74\x79\x6c\x65\x3d\x22\x66\x69\x6c\
\x6c\x3a\x75\x72\x6c\x28\x23\x6c\x69\x6e\x65\x61\x72\x47\x72\x61\
\x64\x69\x65\x6e\x74\x34\x35\x34\x30\x29\x3b\x66\x69\x6c\x6c\x2d\
\x6f\x70\x61\x63\x69\x74\x79\x3a\x31\x3b\x73\x74\x72\x6f\x6b\x65\
\x3a\x6e\x6f\x6e\x65\x3b\x73\x74\x72\x6f\x6b\x65\x2d\x77\x69\x64\
\x74\x68\x3a\x31\x2e\x39\x39\x39\x39\x39\x39\x37\x36\x3b\x73\x74\
\x72\x6f\x6b\x65\x2d\x6c\x69\x6e\x65\x63\x61\x70\x3a\x72\x6f\x75\
\x6e\x64\x3b\x73\x74\x72\x6f\x6b\x65\x2d\x6c\x69\x6e\x65\x6a\x6f\
\x69\x6e\x3a\x72\x6f\x75\x6e\x64\x3b\x73\x74\x72\x6f\x6b\x65\x2d\
\x6d\x69\x74\x65\x72\x6c\x69\x6d\x69\x74\x3a\x34\x3b\x73\x74\x72\
\x6f\x6b\x65\x2d\x64\x61\x73\x68\x61\x72\x72\x61\x79\x3a\x6e\x6f\
\x6e\x65\x3b\x73\x74\x72\x6f\x6b\x65\x2d\x6f\x70\x61\x63\x69\x74\
\x79\x3a\x31\x22\x0a\x20\x20\x20\x20\x20\x20\x20\x69\x64\x3d\x22\
\x70\x61\x74\x68\x34\x35\x33\x32\x22\x0a\x20\x20\x20\x20\x20\x20\
\x20\x63\x78\x3d\x22\x2d\x32\x30\x31\x2e\x30\x34\x33\x39\x38\x22\
\x0a\x20\x20\x20\x20\x20\x20\x20\x63\x79\x3d\x22\x32\x32\x33\x2e\
\x32\x32\x35\x30\x38\x22\x0a\x20\x20\x20\x20\x20\x20\x20\x72\x78\
\x3d\x22\x39\x22\x0a\x20\x20\x20\x20\x20\x20\x20\x72\x79\x3d\x22\
\x36\x22\x0a\x20\x20\x20\x20\x20\x20\x20\x74\x72\x61\x6e\x73\x66\
\x6f\x72\x6d\x3d\x22\x72\x6f\x74\x61\x74\x65\x28\x2d\x34\x35\x29\
\x22\x20\x2f\x3e\x0a\x20\x20\x3c\x2f\x67\x3e\x0a\x3c\x2f\x73\x76\
\x67\x3e\x0a\
"

qt_resource_name = b"\
\x00\x06\
\x07\x03\x7d\xc3\
\x00\x69\
\x00\x6d\x00\x61\x00\x67\x00\x65\x00\x73\
\x00\x12\
\x08\xac\xb9\xc7\
\x00\x6c\
\x00\x65\x00\x64\x00\x52\x00\x6f\x00\x75\x00\x67\x00\x65\x00\x41\x00\x6c\x00\x75\x00\x6d\x00\x65\x00\x65\x00\x2e\x00\x73\x00\x76\
\x00\x67\
\x00\x13\
\x04\x7b\x54\x27\
\x00\x6c\
\x00\x65\x00\x64\x00\x52\x00\x6f\x00\x75\x00\x67\x00\x65\x00\x45\x00\x74\x00\x65\x00\x69\x00\x6e\x00\x74\x00\x65\x00\x2e\x00\x73\
\x00\x76\x00\x67\
"

qt_resource_struct_v1 = b"\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x01\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x02\x00\x00\x00\x02\
\x00\x00\x00\x3c\x00\x00\x00\x00\x00\x01\x00\x00\x0f\x25\
\x00\x00\x00\x12\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\
"

qt_resource_struct_v2 = b"\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x01\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x02\x00\x00\x00\x02\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x3c\x00\x00\x00\x00\x00\x01\x00\x00\x0f\x25\
\x00\x00\x01\x62\xf6\xbe\x5f\xa0\
\x00\x00\x00\x12\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\
\x00\x00\x01\x62\xfb\x91\xc7\x3a\
"

qt_version = QtCore.qVersion().split('.')
if qt_version < ['5', '8', '0']:
    rcc_version = 1
    qt_resource_struct = qt_resource_struct_v1
else:
    rcc_version = 2
    qt_resource_struct = qt_resource_struct_v2

def qInitResources():
    QtCore.qRegisterResourceData(rcc_version, qt_resource_struct, qt_resource_name, qt_resource_data)

def qCleanupResources():
    QtCore.qUnregisterResourceData(rcc_version, qt_resource_struct, qt_resource_name, qt_resource_data)

qInitResources()
