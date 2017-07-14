#Vol2X-QT5 Copyright (c) 2017 JJ Posti <techtimejourney.net> 
#Vol2X-QT5  comes with ABSOLUTELY NO WARRANTY; 
#for details see: http://www.gnu.org/copyleft/gpl.html. 
#This is free software, and you are welcome to redistribute it under 
#GPL Version 2, June 1991"
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QApplication, QDialog, QWidget, QVBoxLayout, QSplitter, QToolButton, QSlider, QLCDNumber
import os, sys, subprocess
from subprocess import Popen 
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QApplication.translate(context, text, disambig)
 
class Ui_Dialog(QDialog):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(621, 104)
        Dialog.setMinimumSize(QtCore.QSize(621, 104))
        Dialog.setMaximumSize(QtCore.QSize(621, 104))
        Dialog.setWindowOpacity(1.0)
        Dialog.setStyleSheet(_fromUtf8("QDialog#Dialog{\n"
"color:#9d9c9c;\n"
"}"))
        Dialog.setSizeGripEnabled(True)
#Slider        
        self.slider = QSlider(Dialog)
        self.slider.setGeometry(QtCore.QRect(50, 20, 521, 41))
        self.slider.setMinimumSize(QtCore.QSize(521, 41))
        self.slider.setMaximumSize(QtCore.QSize(16777215, 41))
        self.slider.setAutoFillBackground(False)
        self.slider.setStyleSheet(_fromUtf8(""))
        self.slider.setOrientation(QtCore.Qt.Horizontal)
        self.slider.setTickPosition(QSlider.TicksBelow)
        self.slider.setTickInterval(5)
        self.slider.setObjectName(_fromUtf8("slider"))
        self.slider.valueChanged[int].connect(self.change)

#Sound button

        self.sound = QToolButton(Dialog)
        self.sound.setGeometry(QtCore.QRect(0, 70, 51, 31))
        icon3 = QIcon()
        icon3.addPixmap(QPixmap(_fromUtf8(":/newPrefix/multimedia-volume-control.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.sound.setIcon(icon3)
        self.sound.setObjectName(_fromUtf8("sound"))
        self.sound.clicked.connect(self.pavu)
        self.sound.setToolTip('Sound settings')
        
#Lcd

        self.lcd = QLCDNumber(Dialog)
        self.lcd.setGeometry(QtCore.QRect(570, 70, 51, 31))
        self.lcd.setStyleSheet(_fromUtf8("QLCDNumber#lcd{\n"
"background-color:#5f5c5c;\n"
"}\n"
""))
        self.lcd.setToolTip('Volume level')
        self.lcd.setObjectName(_fromUtf8("lcd"))
        self.slider.valueChanged.connect(self.lcd.display)
        



#High        
        self.high = QToolButton(Dialog)
        self.high.setGeometry(QtCore.QRect(570, 20, 51, 31))
        icon = QIcon()
        icon.addPixmap(QPixmap(_fromUtf8(":/newPrefix/audio-volume-high.png")), QIcon.Normal, QIcon.Off)
        self.high.setIcon(icon)
        self.high.setObjectName(_fromUtf8("high"))
        self.high.clicked.connect(self.highs)
        self.high.setToolTip('Caution:Volume to max')


#Mute        
        self.mute = QToolButton(Dialog)
        self.mute.setGeometry(QtCore.QRect(0, 20, 51, 31))
        icon1 = QIcon()
        icon1.addPixmap(QPixmap(_fromUtf8(":/newPrefix/audio-volume-muted.png")), QIcon.Normal, QIcon.Off)
        self.mute.setIcon(icon1)
        self.mute.setObjectName(_fromUtf8("mute"))
        self.mute.clicked.connect(self.zero)
        self.mute.setToolTip('Mute')


#Medium        
        self.medium = QToolButton(Dialog)
        self.medium.setGeometry(QtCore.QRect(280, 70, 51, 31))
        icon2 = QIcon()
        icon2.addPixmap(QPixmap(_fromUtf8(":/newPrefix/audio-volume-medium.png")), QIcon.Normal, QIcon.Off)
        self.medium.setIcon(icon2)
        self.medium.setObjectName(_fromUtf8("medium"))
        self.medium.clicked.connect(self.mediums)
        self.medium.setToolTip('Volume to 50%')

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Vol2X-QT5", None))
        self.high.setText(_translate("Dialog", "...", None))
        self.mute.setText(_translate("Dialog", "...", None))
        self.medium.setText(_translate("Dialog", "...", None))
#########VOLUME
   
    def zero(self,widget):
        subprocess.Popen(['pactl', 'set-sink-mute', '0', '1'])
        subprocess.Popen(['pactl', 'set-sink-mute', '1', '1'])
        subprocess.Popen(['pactl', 'set-sink-mute', '2', '1'])
        subprocess.Popen(['pactl', 'set-sink-mute', '3', '1'])
        subprocess.Popen(['pactl', 'set-sink-mute', '4', '1'])
        self.slider.setValue(self.slider.value() - 100)
        self.slider.setValue(self.slider.value() + 0)
    
    def highs(self,widget):
        subprocess.Popen(['pactl', 'set-sink-volume', '0', '100%'])
        subprocess.Popen(['pactl', 'set-sink-volume', '1', '100%'])
        subprocess.Popen(['pactl', 'set-sink-volume', '2', '100%'])
        subprocess.Popen(['pactl', 'set-sink-volume', '3', '100%'])
        subprocess.Popen(['pactl', 'set-sink-volume', '4', '100%'])
        subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
        subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
        subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
        subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
        subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
        self.slider.setValue(self.slider.value() - 100)
        self.slider.setValue(self.slider.value() + 100)
            
    def mediums(self,widget):
        subprocess.Popen(['pactl', 'set-sink-volume', '0', '50%'])
        subprocess.Popen(['pactl', 'set-sink-volume', '1', '50%'])
        subprocess.Popen(['pactl', 'set-sink-volume', '2', '50%'])
        subprocess.Popen(['pactl', 'set-sink-volume', '3', '50%'])
        subprocess.Popen(['pactl', 'set-sink-volume', '4', '50%'])
        subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
        subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
        subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
        subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
        subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
        self.slider.setValue(self.slider.value() - 100)
        self.slider.setValue(self.slider.value() + 50)
#Pavucontrol function
    def pavu(self,widget):
        subprocess.Popen(['pavucontrol'])
 
#Volume changing 
    def change(self,value):
        if value == 0:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '0%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '0%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '0%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '0%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '0%'])

            
        elif value == 1:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '1%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '1%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '1%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '1%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '1%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
            
        elif value == 2:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '2%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '2%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '2%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '2%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '2%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
            
        elif value == 3:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '3%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '3%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '3%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '3%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '3%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
            
        elif value == 4:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '4%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '4%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '4%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '4%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '4%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
            
        elif value == 5:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '5%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '5%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '5%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '5%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '5%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
            
        elif value == 6:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '6%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '6' , '6%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '6%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '6%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '6%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
            
        elif value == 7:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '7%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '7%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '7%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '7%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '7%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
            
        elif value == 8:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '8%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '8%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '8%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '8%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '8%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
            
        elif value == 9:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '9%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '9%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '9%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '9%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '9%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
            
        elif value == 10:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '10%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '10%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '10%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '10%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '10%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
            
        elif value == 11:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '11%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '11%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '11%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '11%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '11%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
            
        elif value == 12:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '12%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '12%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '12%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '12%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '12%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
            
        elif value == 13:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '13%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '13%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '13%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '13%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '13%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
            
        elif value == 14:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '14%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '14%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '14%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '14%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '14%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
            
        elif value == 15:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '15%'])	
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '15%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '15%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '15%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '15%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
            
        elif value == 16:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '16%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '16%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '16%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '16%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '16%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
            
        elif value == 17:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '17%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '17%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '17%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '17%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '17%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
            	
        elif value == 18:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '18%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '18%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '18%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '18%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '18%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
            
        elif value == 19:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '19%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '19%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '19%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '19%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '19%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
            
        elif value == 20:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '20%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '20%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '20%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '20%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '20%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
            
        elif value == 21:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '21%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '21%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '21%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '21%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '21%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
            
        elif value == 22:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '22%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '22%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '22%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '22%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '22%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
            
        elif value == 23:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '23%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '23%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '23%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '23%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '23%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
            
        elif value == 24:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '24%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '24%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '24%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '24%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '24%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
            
        elif value == 25:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '25%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '25%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '25%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '25%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '25%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
            
        elif value == 26:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '26%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '26%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '26%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '26%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '26%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
            
        elif value == 27:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '27%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '27%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '27%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '27%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '27%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
            
        elif value == 28:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '28%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '28%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '28%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '28%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '28%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
            
        elif value == 29:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '29%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '29%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '29%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '29%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '29%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
            
        elif value == 30:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '30%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '30%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '30%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '30%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '30%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
            
        elif value == 31:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '31%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '31%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '31%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '31%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '31%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
            
        elif value == 32:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '32%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '32%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '32%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '32%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '32%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
            
        elif value == 33:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '33%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '33%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '33%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '33%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '33%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
                 
        elif value == 34:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '34%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '34%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '34%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '34%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '34%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
            
        elif value == 35:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '35%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '35%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '35%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '35%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '35%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
            
        elif value == 36:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '36%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '36%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '36%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '36%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '36%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
            
        elif value == 37:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '37%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '37%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '37%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '37%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '37%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
            
        elif value == 38:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '38%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '38%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '38%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '38%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '38%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
            
        elif value == 39:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '39%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '39%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '39%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '39%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '39%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
                        
        elif value == 40:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '40%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '40%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '40%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '40%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '40%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
                        
        elif value == 41:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '41%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '41%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '41%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '41%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '41%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
                        
        elif value == 42:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '42%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '42%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '42%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '42%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '42%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
                        
        elif value == 43:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '43%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '43%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '43%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '43%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '43%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
                        
        elif value == 44:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '44%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '44%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '44%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '44%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '44%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
                        
        elif value == 45:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '45%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '45%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '45%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '45%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '45%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
                        
        elif value == 46:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '46%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '46%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '46%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '46%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '46%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
                        
        elif value == 47:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '47%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '47%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '47%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '47%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '47%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
                        
        elif value == 48:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '48%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '48%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '48%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '48%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '48%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
                        
        elif value == 49:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '49%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '49%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '49%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '49%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '49%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
                        
        elif value == 50:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '50%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '50%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '50%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '50%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '50%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
                                   
        elif value == 51:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '51%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '51%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '51%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '51%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '51%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
                        
        elif value == 52:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '52%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '52%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '52%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '52%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '52%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
                                    
        elif value == 53:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '53%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '53%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '53%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '53%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '53%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
                        
        elif value == 54:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '54%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '54%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '54%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '54%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '54%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
                        
        elif value == 55:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '55%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '55%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '55%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '55%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '55%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
                        
        elif value == 56:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '56%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '56%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '56%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '56%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '56%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
                        
        elif value == 57:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '57%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '57%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '57%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '57%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '57%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
                        
        elif value == 58:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '58%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '58%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '58%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '58%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '58%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
            
        elif value == 59:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '59%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '59%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '59%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '59%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '59%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
            
        elif value == 60:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '60%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '60%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '60%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '60%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '60%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
            
        elif value == 61:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '61%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '61%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '61%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '61%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '61%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
            
        elif value == 62:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '62%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '62%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '62%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '62%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '62%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
                        
        elif value == 63:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '63%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '63%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '63%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '63%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '63%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
                        
        elif value == 64:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '64%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '64%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '64%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '64%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '64%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
            
        elif value == 65:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '65%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '65%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '65%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '65%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '65%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
            
        elif value == 66:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '66%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '66%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '66%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '66%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '66%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
            
        elif value == 67:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '67%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '67%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '67%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '67%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '67%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
            
        elif value == 68:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '68%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '68%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '68%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '68%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '68%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
            
        elif value == 69:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '69%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '69%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '69%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '69%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '69%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
            
        elif value == 70:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '70%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '70%'])	           
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '70%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '70%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '70%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
            
        elif value == 71:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '71%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '71%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '71%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '71%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '71%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
            
        elif value == 72:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '72%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '72%'])	
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '72%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '72%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '72%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
            
        elif value == 73:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '73%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '73%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '73%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '73%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '73%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
            
        elif value == 74:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '74%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '74%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '74%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '74%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '74%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
            
        elif value == 75:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '75%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '75%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '75%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '75%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '75%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
            
        elif value == 76:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '76%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '76%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '76%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '76%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '76%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
            
        elif value == 77:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '77%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '77%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '77%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '77%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '77%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
            
        elif value == 78:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '78%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '78%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '78%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '78%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '78%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
                 
        elif value == 79:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '79%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '79%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '79%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '79%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '79%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
            
        elif value == 80:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '80%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '80%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '80%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '80%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '80%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
                 
        elif value == 81:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '81%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '81%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '81%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '81%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '81%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
            
        elif value == 82:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '82%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '82%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '82%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '82%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '82%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
                 
        elif value == 83:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '83%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '83%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '83%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '83%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '83%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
                 
        elif value == 84:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '84%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '84%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '84%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '84%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '84%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
                 
        elif value == 85:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '85%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '85%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '85%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '85%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '85%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
                        
        elif value == 86:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '86%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '86%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '86%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '86%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '86%'])    
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
            
        elif value == 87:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '87%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '87%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '87%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '87%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '87%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
                                    
        elif value == 88:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '88%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '88%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '88%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '88%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '88%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
            
        elif value == 89:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '89%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '89%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '89%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '89%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '89%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
                            
        elif value == 90:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '90%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '90%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '90%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '90%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '90%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
            
        elif value == 91:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '91%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '91%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '91%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '91%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '91%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
                 
        elif value == 92:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '92%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '92%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '92%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '92%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '92%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
            
        elif value == 93:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '93%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '93%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '93%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '93%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '93%'])    
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
            
        elif value == 94:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '94%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '94%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '94%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '94%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '94%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
                                                                      
        elif value == 95:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '95%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '95%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '95%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '95%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '95%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
                        
        elif value == 96:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '96%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '96%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '96%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '96%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '96%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
            
        elif value == 97:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '97%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '97%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '97%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '97%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '97%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
            
        elif value == 98:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '98%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '98%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '98%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '98%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '98%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
            
        elif value == 99:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '99%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '99%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '99%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '99%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '99%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])
                 
        elif value == 100:
            subprocess.Popen(['pactl', 'set-sink-volume', '0' , '100%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '1' , '100%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '2' , '100%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '3' , '100%'])
            subprocess.Popen(['pactl', 'set-sink-volume', '4' , '100%'])
            subprocess.Popen(['pactl', 'set-sink-mute', '0', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '1', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '2', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '3', '0'])
            subprocess.Popen(['pactl', 'set-sink-mute', '4', '0'])            
############ICONS
qt_resource_data = "\
\x00\x00\x04\x84\
\x89\
\x50\x4e\x47\x0d\x0a\x1a\x0a\x00\x00\x00\x0d\x49\x48\x44\x52\x00\
\x00\x00\x18\x00\x00\x00\x18\x08\x06\x00\x00\x00\xe0\x77\x3d\xf8\
\x00\x00\x00\x06\x62\x4b\x47\x44\x00\xfe\x00\xfe\x00\xfe\xeb\x18\
\xd4\x82\x00\x00\x00\x09\x70\x48\x59\x73\x00\x00\x0d\xd6\x00\x00\
\x0d\xd6\x01\x90\x6f\x79\x9c\x00\x00\x00\x09\x76\x70\x41\x67\x00\
\x00\x00\x18\x00\x00\x00\x18\x00\x78\x4c\xa5\xa6\x00\x00\x03\x88\
\x49\x44\x41\x54\x48\xc7\xed\x55\x5b\x6f\x54\x55\x14\xfe\xf6\xe5\
\x9c\xb9\x77\xa6\xd3\x76\x0a\x29\x89\xb4\x25\x75\x08\x97\x9a\x18\
\x13\x7d\xc1\x18\x79\x92\x86\xdf\x20\x3e\x10\x9b\xe8\x43\x23\x84\
\x4a\xc0\x14\x79\x60\xc4\x3a\xb1\x6a\x10\x8d\x49\xf5\xc1\x44\xaa\
\xa5\xa1\x11\x2b\x35\xd1\x44\x8a\x81\x1a\x6a\x48\x28\x8d\xa6\xb6\
\x16\xa8\x9d\x76\x3a\x0c\x33\x9d\x39\x33\xe7\x9c\x7d\xf1\x01\x68\
\x1c\x2e\xad\xe8\x8b\x0f\x7c\xc9\x4a\xf6\x5a\x7b\xe7\xfb\xb2\xd6\
\xb7\x92\x0d\x3c\xc2\x2a\x20\x2b\x5d\x1e\x39\xf2\xe6\x93\x05\xcb\
\xda\x2d\x84\x68\xd2\x4a\x45\x09\xa1\x37\x29\xa5\xf9\x5c\x3e\x3f\
\x76\xec\x83\xe3\x87\xff\x93\xc0\x81\x37\xf6\x27\xaa\xaa\x42\xbb\
\xb6\x6c\xd9\x1a\x8a\xb7\xc4\xbd\xdc\x34\x88\x74\xa5\x5e\x58\x58\
\x28\xcd\xce\x5d\xb7\xc7\xc7\x2f\x67\x01\x40\x28\x35\xdc\x75\xe0\
\x50\xfb\x43\x09\x74\x76\xee\x1d\xac\xad\xab\xdb\xd1\xfe\x72\x3b\
\x15\x42\x00\x00\x28\x65\x50\x4a\x02\x00\x38\x37\xe0\x38\x0e\x1c\
\xd7\xc6\x47\x1f\x1f\x4f\x59\xb6\xdd\x96\x38\x9c\xb8\x78\x3f\x2e\
\x7e\x77\x61\xdf\xeb\x7b\x4e\x34\x34\xac\xdb\xb1\xeb\xc5\x97\xa8\
\x6d\xdb\xcb\x75\x29\xe5\x3d\x67\xc6\x18\x28\xa5\x41\x02\x12\x7c\
\x50\x07\xf4\xef\xc9\xab\xef\x7d\x53\x25\x84\xda\xd9\xd6\xb6\x93\
\x3a\x8e\x8d\xd5\x20\xa4\x80\xe9\xf1\x04\x27\x67\xcb\xdf\xef\x7d\
\xf7\x64\xb2\xab\xb7\xd7\xfb\x40\x81\x7d\xc9\xaf\x36\x95\xe7\x27\
\xbb\x6b\x6a\xa2\xa6\xe3\x38\xff\xc4\x3f\x58\x56\x11\x75\xb1\x3a\
\x34\xae\x31\x29\x80\x8e\x62\x2e\x3c\xd3\x99\x3c\xb5\xe1\x1e\x81\
\xae\xae\x3e\x53\x51\xfa\xa5\xc7\x9a\xd2\xcd\x4d\xcd\x08\x87\x43\
\x20\x94\xae\x48\x4e\x29\x45\x6e\xe9\x26\x6a\x6b\xa3\x42\x0a\xe1\
\x48\xe1\x02\x40\x4c\x31\x79\xba\x23\xd9\x17\xad\x10\xb0\x22\xc6\
\x6e\x80\xfc\x52\x15\xf0\xe9\xfa\xfa\x35\xd4\x11\x36\xd2\x99\x14\
\x34\x34\x28\x65\x60\x8c\x83\x10\x0a\xce\x39\x28\x63\x10\x4a\xe0\
\xf7\xab\x93\x28\x94\x0a\x88\x44\xc2\x5c\x09\x91\xca\x67\xd3\x13\
\xae\x63\x43\x6b\xb4\x18\x94\x27\x2a\x4c\x56\x44\x3f\x3b\x3e\xf6\
\x43\xe7\xc6\x18\xef\x5b\xbf\xbe\x11\xb9\x7c\x16\x00\xf0\xe7\xfc\
\x75\x30\xc6\x60\x1a\x1e\x78\x4c\x0f\x0a\xc5\x25\x2c\x15\xf3\xb0\
\x4a\x45\x08\x21\xe0\x0a\x17\xd5\x91\x1a\x68\x28\x5c\xb9\x38\x72\
\x74\xeb\xd3\xcf\xf7\x32\xce\x41\x29\x7b\xa2\xd2\x03\xa9\xc9\xd0\
\x67\xef\x17\x08\x94\xdf\xe7\xf5\x54\x8c\x42\x4a\x09\xab\x54\x44\
\x3a\x33\x8f\x7c\x21\x07\xd7\xad\xf4\x87\x00\x20\x20\x6c\x6c\xe4\
\xeb\x19\xc7\x2e\x95\xdd\x5b\xcb\xf1\x54\x85\x80\x70\xed\x19\x00\
\x86\x52\xba\x51\x28\x89\x7f\x01\xb3\x5c\x28\x90\xd4\xec\xaf\xad\
\xa5\xb2\xf5\x38\xd3\xba\xb9\x62\x44\x20\x64\xaa\x29\xde\xea\x97\
\x42\xba\x80\xf2\x3c\x0c\xb3\xcf\x1b\x80\x6d\xdb\x7a\x5b\x8d\x2f\
\xd2\x73\x6d\xf0\x0b\x75\x75\xf0\x92\x41\x71\x29\x01\xec\x59\xee\
\x40\x7a\xc3\x9f\xb4\x3e\xf3\xc2\xda\xc5\xcc\x8d\xa1\xfe\xfe\x01\
\x61\x70\x73\x55\x62\x83\x1b\x58\x1b\x6b\xc0\xc0\xc9\x01\xd7\xef\
\xf7\x7d\xdb\x1a\x36\x7c\x14\x24\x68\x52\xb2\x9d\x80\xbc\x76\xe7\
\x1d\x03\x80\xd1\xa1\xcf\x65\x80\x55\xa7\x87\xcf\xf4\xff\xb8\x69\
\xf3\xc6\x75\x94\xd0\x78\x75\x24\x4a\x83\xc1\x20\xb4\x52\x50\x5a\
\x41\xa9\x5b\xe1\xf3\x06\x60\x9a\x5e\x40\x12\x0c\x9f\xf9\xce\xce\
\x66\xb3\xa7\xdf\xe9\xee\x39\x36\x9a\xb5\xa7\x5e\x79\x2c\xf4\x1c\
\xa3\xc4\x0b\xc0\xdb\x33\x9d\x3b\xb4\x2c\x00\x00\x73\x73\xbf\xb9\
\x00\xec\x9f\xce\x9d\x3f\xd7\x12\x6f\x49\x8d\x5e\xb8\x10\x5f\x5c\
\xcc\xf8\x63\xb1\x7a\xc6\x99\x01\xbf\xcf\x0f\x93\x7b\x90\x4e\xa7\
\x31\x7a\xfe\x67\x77\xe4\xec\xd9\x69\xa5\xf5\x87\x6f\xbf\x95\xfc\
\x14\x40\x06\xc0\xb5\x8e\x0d\x91\x1b\xd0\x64\x82\x10\xf2\x47\xcf\
\x74\xee\xd4\x9d\x25\xb8\x1b\x04\x40\x08\x40\xf4\xe0\xc1\xfd\xdb\
\xad\x92\xb5\xcd\x75\xc5\x66\x10\x04\xa0\x51\xe4\x06\x9b\xe0\xdc\
\x98\x3d\x9a\xe8\x3e\x01\xa0\x00\x20\x0d\x20\x07\xe0\xbe\xdb\xb1\
\xd2\x7f\x40\x00\x18\x00\x4c\x00\x9e\xdb\xa1\x01\xb8\x00\x1c\x00\
\xf6\xed\x78\x84\xff\x39\xfe\x02\xdd\xa9\x85\x69\x1e\x0a\xea\xe4\
\x00\x00\x00\x25\x74\x45\x58\x74\x64\x61\x74\x65\x3a\x63\x72\x65\
\x61\x74\x65\x00\x32\x30\x31\x36\x2d\x30\x39\x2d\x32\x31\x54\x31\
\x32\x3a\x35\x37\x3a\x34\x30\x2d\x30\x30\x3a\x30\x30\x90\x54\x97\
\x25\x00\x00\x00\x25\x74\x45\x58\x74\x64\x61\x74\x65\x3a\x6d\x6f\
\x64\x69\x66\x79\x00\x32\x30\x31\x36\x2d\x30\x39\x2d\x32\x31\x54\
\x31\x32\x3a\x35\x37\x3a\x34\x30\x2d\x30\x30\x3a\x30\x30\xe1\x09\
\x2f\x99\x00\x00\x00\x19\x74\x45\x58\x74\x53\x6f\x66\x74\x77\x61\
\x72\x65\x00\x77\x77\x77\x2e\x69\x6e\x6b\x73\x63\x61\x70\x65\x2e\
\x6f\x72\x67\x9b\xee\x3c\x1a\x00\x00\x00\x00\x49\x45\x4e\x44\xae\
\x42\x60\x82\
\x00\x00\x04\x89\
\x89\
\x50\x4e\x47\x0d\x0a\x1a\x0a\x00\x00\x00\x0d\x49\x48\x44\x52\x00\
\x00\x00\x18\x00\x00\x00\x18\x08\x06\x00\x00\x00\xe0\x77\x3d\xf8\
\x00\x00\x00\x06\x62\x4b\x47\x44\x00\xfe\x00\xfe\x00\xfe\xeb\x18\
\xd4\x82\x00\x00\x00\x09\x70\x48\x59\x73\x00\x00\x0d\xd6\x00\x00\
\x0d\xd6\x01\x90\x6f\x79\x9c\x00\x00\x00\x09\x76\x70\x41\x67\x00\
\x00\x00\x18\x00\x00\x00\x18\x00\x78\x4c\xa5\xa6\x00\x00\x03\x8d\
\x49\x44\x41\x54\x48\xc7\xd5\x95\x5f\x6c\xd3\x55\x14\xc7\xbf\xf7\
\xd7\x5f\xff\xcd\xb5\x74\x9d\x23\x65\x86\xd0\xd1\x91\xc1\x5c\x66\
\xd4\x29\x33\xdd\x0c\x60\x8c\xc0\x44\x30\x71\x0d\x90\x18\x12\x1e\
\x0c\xc6\x8c\xf0\xd0\x2c\xe0\xd3\x9e\x46\x08\x61\x31\xf2\x6c\x8c\
\x89\x0f\x22\x89\x46\x74\x19\x98\x68\xba\x49\xad\x14\xa3\x04\x70\
\x85\x07\xa4\x0c\x5b\x06\x88\x76\xdd\xed\xaf\xbf\x3f\xf7\xdc\x9f\
\x0f\x8e\x30\xc6\xca\xda\x17\x13\x4f\x72\x73\x1f\xee\xb9\xe7\x93\
\xf3\x3d\xf7\xdc\x03\xfc\xdf\xcd\x51\xa5\x1f\x3b\x10\xdf\xb7\x61\
\xe5\x53\x2d\x37\x27\x27\x27\xed\x5a\x00\xac\x1a\xa7\xf8\xc1\xfd\
\xbf\x28\x8a\xb2\x56\x12\xfd\x51\xef\x6d\x6c\x1f\x1a\x1a\x12\xd5\
\x02\x94\x6a\x9c\x48\x88\x67\xb6\xf7\xf5\x7b\x05\x89\xd5\x59\x64\
\xd5\x5a\x32\x58\x12\x30\x38\xb8\xd7\x47\x92\x94\x70\x38\x0c\x22\
\x59\x4b\xec\xa5\x01\x83\x83\x7b\x7d\xb6\xc3\x37\x26\x48\xe2\xde\
\xbd\x3f\x21\x04\x01\xd9\x87\x7d\xc2\xdb\x86\xd7\xb6\x6c\x1d\x7e\
\xbb\x66\x40\x3c\xbe\x6f\xb9\x74\x3c\xf1\x73\x47\x47\xe7\x0b\x92\
\x24\x54\xd5\xb9\x78\x06\x16\xd3\x6d\xb0\x23\xab\xb6\x1c\xde\xb4\
\x58\x9c\x87\xf4\x8c\x1f\xdc\x7f\x4a\x4a\x7a\xd5\xa1\x38\x12\x00\
\x3a\xba\xd7\x47\x43\x2f\xbd\xd8\xab\xa6\x52\x29\xb8\x5c\x2e\x10\
\x11\x16\xbe\x8b\xec\xe9\x43\xd9\x75\xb1\x0f\x76\xaa\x8a\x72\xe2\
\xd9\x9d\xc7\x9f\xff\xf5\xb3\x81\x7c\xc5\x0c\x66\x39\xdf\xb6\xe3\
\xf5\x98\x67\xb6\x54\x7a\x6d\xf3\xe6\xbe\xe6\xde\xe8\x46\x35\x14\
\x0a\x41\x4a\x09\xb7\xdb\x0d\x22\x39\x2f\xba\xcd\x5a\xfa\x86\xe3\
\x6d\x6f\x1c\xf1\x65\x3e\x3f\x30\xb1\xac\xc1\x3f\xea\x0f\xfa\x77\
\x54\x94\x68\xd7\xae\xd8\x1e\xbd\x6c\xa2\xa9\x69\x39\x0c\xdd\x62\
\x5d\xcf\x75\x2b\x8d\xc1\x46\x14\x8b\x45\x98\x86\x80\xa6\x69\x10\
\x44\x4a\xc3\x93\x0d\x5f\xfe\x7b\x83\xd9\x8c\x39\x22\x04\x1c\x03\
\x80\x86\xc0\xb2\xf1\x40\x30\xd0\x5b\x11\x60\x33\x1c\xd5\x75\x03\
\xcd\xcd\x2b\x20\x2c\x82\xcb\xe5\xc2\xf5\x1b\xbf\x23\x75\x2e\x09\
\xd3\x32\xc1\x39\x07\x09\xc2\xcd\xdc\xad\x0d\xfd\xfd\xfd\x2d\x00\
\xb0\x7a\x4d\xeb\xd1\xb6\x75\xad\x5b\x01\x20\x10\xac\x3b\x1b\x08\
\xf8\x7b\x2a\xd6\x80\x88\x9a\x0c\x61\x21\x93\xb9\x02\xae\x69\xb8\
\x72\x35\x83\xb2\xa6\xc1\x34\x2d\x08\x22\xf0\x12\x87\x10\x84\xa9\
\xa9\xdb\xd0\x2d\x03\x00\xb0\x22\x14\x0c\xfa\xfd\x75\x45\x00\x70\
\x3b\xbd\x3e\x6f\x9d\x57\xab\x08\x60\x4c\xc9\xeb\xba\xd9\x3c\x3d\
\x3d\x8d\x72\xd9\x80\xc2\x14\x98\xa6\x89\xb2\xa6\x41\x58\x02\x25\
\x5e\x02\x09\x09\x29\x65\xe2\x62\x3a\x7d\x7d\xcb\xc0\x87\xee\x7c\
\xee\xd6\xc8\x9d\x3b\x8e\x4f\x01\xc0\x30\xac\x4d\x42\xd8\xdf\x57\
\x96\x88\xe8\x5d\xbd\x6c\x20\x9f\xcf\xa3\xac\xe9\x76\x3a\x9d\x96\
\xb0\x19\x74\xdd\x80\x20\x09\xce\x39\x2c\x12\xb2\xbe\xcd\xf9\x26\
\x00\x8c\x1d\x1f\x30\xaf\x5d\xcb\x7e\x74\xe6\x58\xec\x30\x00\xcc\
\x14\xf9\x2b\x33\x7f\x17\x2a\x03\x4e\x9e\xfc\xe2\x54\x59\x37\x91\
\xcb\xe5\x50\xd6\x4d\xfa\x6a\xf4\x9b\x7c\x32\x95\x14\xaa\xaa\x82\
\x04\xdd\xaf\x81\xfd\xa0\xd1\x98\x9d\x1d\x7d\xff\x13\x80\xd9\x3d\
\xef\x7c\xbc\xbb\xf0\xd7\x4c\xbb\x5e\x9c\x3d\xf3\xd8\x3e\x10\x16\
\xfd\xf8\xf5\xe9\x6f\xbb\x1d\x8a\x23\x69\x96\xf4\xd8\x77\xe3\xe3\
\x3f\xac\x89\x44\x56\x09\x22\x37\x2f\x95\x20\x88\x1e\x69\xa4\xf6\
\xb7\x46\x7a\x0b\x85\xe2\x08\x98\xba\x71\xe2\xc4\x7b\xc5\xc7\x02\
\x5a\xc3\x2b\x5f\x3e\x7f\xf7\xae\x33\x9b\x48\x98\x00\x64\x34\x1a\
\xed\xba\xfc\xdb\xe4\x98\xc7\xed\x8e\x96\x38\x5f\xb4\x93\x35\xcd\
\x88\xd8\x36\x76\xdf\x18\x3b\x94\xc1\x22\xb6\xe4\x77\xdd\x16\x8d\
\xfa\x42\x5e\x4f\xb1\x67\x7d\x37\xce\x9e\xfb\x89\x98\xa0\xfa\x44\
\x22\xa1\x2f\x75\xef\x91\x1a\x2c\xc8\xca\x03\xa0\x0e\x40\xfd\xd5\
\x64\xd2\x16\x24\x24\xe7\x7c\xee\xab\xa8\xcd\xe6\x4b\xe4\x9a\x5b\
\xee\xb9\xdd\x79\xff\x5c\x58\x94\x39\x7f\xe1\x42\xc4\x96\x32\x7f\
\xf9\xd2\x25\x0f\x00\x02\x60\x55\x03\x98\x2f\x91\xb2\x00\xa0\xe2\
\xc1\x48\x95\x4f\x77\x76\x76\xe5\xa6\xa6\x26\x0a\x85\x82\x36\x17\
\xbc\xaa\xd1\xc9\xaa\x3c\xab\x69\x0e\xff\xa7\xf6\x0f\x24\x75\xb4\
\xf8\xb8\x38\xde\x1d\x00\x00\x00\x25\x74\x45\x58\x74\x64\x61\x74\
\x65\x3a\x63\x72\x65\x61\x74\x65\x00\x32\x30\x31\x36\x2d\x30\x39\
\x2d\x32\x31\x54\x31\x32\x3a\x35\x37\x3a\x34\x30\x2d\x30\x30\x3a\
\x30\x30\x90\x54\x97\x25\x00\x00\x00\x25\x74\x45\x58\x74\x64\x61\
\x74\x65\x3a\x6d\x6f\x64\x69\x66\x79\x00\x32\x30\x31\x36\x2d\x30\
\x39\x2d\x32\x31\x54\x31\x32\x3a\x35\x37\x3a\x34\x30\x2d\x30\x30\
\x3a\x30\x30\xe1\x09\x2f\x99\x00\x00\x00\x19\x74\x45\x58\x74\x53\
\x6f\x66\x74\x77\x61\x72\x65\x00\x77\x77\x77\x2e\x69\x6e\x6b\x73\
\x63\x61\x70\x65\x2e\x6f\x72\x67\x9b\xee\x3c\x1a\x00\x00\x00\x00\
\x49\x45\x4e\x44\xae\x42\x60\x82\
\x00\x00\x05\x58\
\x89\
\x50\x4e\x47\x0d\x0a\x1a\x0a\x00\x00\x00\x0d\x49\x48\x44\x52\x00\
\x00\x00\x18\x00\x00\x00\x18\x08\x06\x00\x00\x00\xe0\x77\x3d\xf8\
\x00\x00\x00\x06\x62\x4b\x47\x44\x00\xfe\x00\xfe\x00\xfe\xeb\x18\
\xd4\x82\x00\x00\x00\x09\x70\x48\x59\x73\x00\x00\x0d\xd6\x00\x00\
\x0d\xd6\x01\x90\x6f\x79\x9c\x00\x00\x00\x09\x76\x70\x41\x67\x00\
\x00\x00\x18\x00\x00\x00\x18\x00\x78\x4c\xa5\xa6\x00\x00\x04\x5c\
\x49\x44\x41\x54\x48\xc7\xd5\x95\x7f\x4c\x55\x65\x18\xc7\xbf\xe7\
\xdc\x73\x7f\x9c\xfb\x8b\x0b\x88\x43\x98\x03\x44\x40\xc9\xd1\x6c\
\x34\x69\x17\x1a\xa8\x2d\x11\x28\xdc\x04\x91\x55\x6b\xfe\xa1\x4e\
\x26\x99\x23\x06\xf5\x0f\x7f\x34\xc8\xcd\xb0\x72\xad\x1f\x5b\x6b\
\xb6\x5a\x89\x96\xab\x24\xd4\x4d\x07\x28\x91\xa8\xcd\x25\x71\x65\
\xcb\xb8\x60\x10\x8e\xa4\xcb\xe5\xfc\xba\xe7\xbc\xef\x7b\xfa\x03\
\x50\x7e\x35\xe1\x9f\xb6\xbe\xdb\xd9\xd9\xde\xf7\x7b\x9e\xcf\x7b\
\x9e\xf3\x3c\xe7\x01\xfe\xef\xb2\x2c\xd1\xc7\x1d\xaa\xd9\x9f\xbf\
\x3a\x31\xe5\x6e\x5f\x5f\x9f\xb9\x1c\x00\xb7\x14\x53\x4d\x5d\xf5\
\xcf\x3c\xcf\xaf\x63\x94\xfe\xe1\x16\x63\x33\x1b\x1a\x1a\xc8\x7c\
\x4f\x52\x51\xd3\x01\xde\xe4\x7a\x07\x7e\xa8\xeb\x9c\xbd\xce\x2f\
\x05\x40\x09\x79\xfc\xf9\xa2\x32\x91\x50\xb2\x26\x88\xa0\xb0\x98\
\x87\x67\xf8\x8d\xc1\xfc\x3a\xb9\xb8\x29\x7f\x59\x80\xda\xda\x3d\
\x1e\xca\x28\x9f\x9c\x9c\x0c\x4a\xd9\xbf\xfa\x06\xda\xea\x2f\xb8\
\x9c\xce\x0a\xd1\xe1\xf8\x2a\x7d\xf7\xd1\x15\x4b\x02\xd4\xd6\xee\
\xf1\x98\x16\x4f\x1b\xa1\x0c\xf7\xef\xff\x05\x42\x28\x10\x9c\xeb\
\x49\x2e\x69\x5c\x97\xb2\xbd\xf1\x45\x00\xe8\x3b\xfd\xca\x45\x97\
\x53\xfc\xcc\x6b\xf3\x1c\x7b\x24\xa0\xa6\x66\xff\x4a\x66\x71\x5d\
\xdf\xb0\x21\xeb\x49\x46\x19\x04\xc1\xba\xf8\x1b\x18\x9c\x66\x82\
\x3b\x92\x54\xd8\xb4\x19\x00\x4c\x07\xd7\xe0\x74\x3a\xb6\xe4\x56\
\x9d\x48\x5f\x00\xa8\xa9\xab\xfe\xee\x70\x6d\x95\xfa\x5a\x5d\x75\
\x1b\x27\xd8\x6e\x3c\xb5\x29\x77\xcd\x33\x05\x85\x36\x80\x83\xcd\
\x66\x03\xa5\x74\x41\xfc\xe0\xb9\xfa\xa0\xe8\x16\x2b\xbc\x51\xae\
\x2f\x36\x56\x1c\x4f\xb8\xf1\xf1\x3e\xc5\xe5\x16\x5b\xdc\x0e\x67\
\xf9\x02\xc0\xa4\x24\x95\x94\x16\x97\x3b\x26\x65\xf9\xd9\x6d\xdb\
\x8a\x12\xf2\xfc\x05\x42\x7c\x7c\x3c\x18\x63\xb0\xdb\xed\xa0\x94\
\xcd\xaa\x3a\x93\x4b\x29\x6a\xac\xc9\x78\xee\x88\x27\xd0\x72\xa8\
\x33\x2a\xda\xdb\xea\x8d\xf1\x96\x02\x80\xe8\x72\x7d\xe3\xf2\x88\
\xc5\x73\x00\xbb\x2a\x77\xbd\xa4\xa9\x3a\xe2\xe2\x56\x22\xa2\x19\
\x5c\xf6\x13\x39\x7c\x6c\x4c\x2c\xc2\xe1\x30\xf4\x08\x81\xa2\x28\
\x20\x94\xf2\xd1\x2b\xa2\xcf\x4c\x3d\xc1\x99\xe0\x2d\x69\x14\x78\
\x1b\x00\xa2\x7d\x51\x1d\xbe\x18\x5f\x1e\x00\xd8\xad\xf6\x7e\xa7\
\x28\xa6\xce\x01\x70\x30\x8f\x6a\x5a\x04\x09\x09\xab\x40\x0c\x0a\
\x9b\xcd\x86\x81\xc1\xdf\xd1\x7d\xb5\x0b\xba\xa1\x43\x92\x24\x50\
\x42\x71\x77\xf8\xcf\xfc\xb2\xb2\xb2\x14\x00\x48\xcb\x48\x79\x2b\
\x63\xfd\xda\xed\x00\xe0\x8b\x71\x5e\xf1\xf9\xbc\xb9\x00\xf0\xe5\
\x1b\x5b\xef\x39\x5d\x0e\x37\x00\x3c\xa8\x69\x4a\x69\x5c\x84\x18\
\x08\x04\x6e\x43\x52\x14\xdc\xee\x0f\x40\x55\x14\xe8\xba\x01\x42\
\x29\x24\x59\x02\x21\x14\x43\x43\xf7\xa0\x19\x11\x00\x40\xfc\xaa\
\x68\x9f\x47\xf4\xca\x53\xa7\x16\x3d\xa2\x53\x54\x00\x60\xef\x47\
\xd7\xad\x0e\xcb\xd4\xe1\x1f\x00\x38\x8e\x1f\xd1\x34\x3d\x61\x74\
\x74\x14\xaa\x1a\x01\xcf\xf1\xd0\x75\x1d\xaa\xa2\x80\x18\x04\xb2\
\x24\x83\x12\x06\xc6\x58\xfb\x2f\x3d\x3d\x03\x85\x07\xdf\xb3\x0f\
\x0f\x8e\xbd\x2b\x08\xe3\x9f\x03\x40\x24\x62\x6c\x26\xc4\xbc\x04\
\x00\xbc\x62\x24\x6a\x56\x36\x3a\x27\x45\xcc\x24\xfb\x34\x35\x82\
\x91\x91\x11\xa8\x8a\x66\xf6\xf4\xf4\x30\x98\x1c\x34\x2d\x02\x42\
\x19\x24\x49\x82\x41\x09\x73\x67\x58\x77\x00\x40\xdb\xf1\x83\xfa\
\x9d\x3b\xc1\x4f\xce\x37\x97\xbf\x09\x00\x13\x61\x69\xcb\xc4\xdf\
\xa1\x4b\x00\x30\xa9\xcb\xd9\x8a\xac\x06\xe6\x00\x4e\x9f\x3c\x73\
\x56\xd5\x74\x0c\x0f\x0f\x43\xd5\x74\xfa\x6d\xeb\xd9\x91\xae\xee\
\x2e\x22\x08\x02\x28\xa1\x33\xdf\xc0\x7c\xd8\x68\x9c\x19\x6c\x7d\
\xfd\x04\xc0\x99\xb9\x7b\x3f\xad\x0c\x8d\x4f\x64\x6a\xe1\xc9\xf3\
\x00\xa0\xca\xea\x4e\x59\xd6\x4e\xcd\x49\x11\x00\x10\x83\xfe\xf8\
\xfd\xb9\x0b\x39\x16\xde\xd2\xa5\xcb\x5a\xf9\xc5\x8e\x8e\xcb\x69\
\xa9\xa9\x49\x84\x52\xbb\x24\xcb\x20\x8b\xf4\x41\xe6\xce\xe6\xbc\
\x50\x28\xdc\x0c\x4e\x28\xe8\x3c\x59\x15\x2e\x7e\xb5\x25\x51\x51\
\xd4\xad\x26\xc5\x81\x05\x80\xb5\xc9\xab\x9f\xbe\x36\x36\x66\x0d\
\xb6\xb7\xeb\x00\x98\xdf\xef\xcf\xee\xfd\xb5\xaf\xcd\x61\xb7\xfb\
\x65\x49\x5a\xb4\x93\x15\x25\x92\x6a\x9a\xa8\x1c\x6c\xab\x0f\x00\
\x40\x48\x55\x9b\x39\xce\x7c\xff\xf2\x07\x2f\x8f\x4f\x55\xe7\x23\
\x94\xe1\xf7\x7b\xe2\x45\x47\x38\x77\x53\x0e\xae\x5c\xfd\x89\x72\
\x84\xba\xdb\xdb\xdb\xb5\xc5\xbc\x1b\x5f\xf8\x70\x37\xcf\x73\x4d\
\x36\x55\x5e\xdf\x7d\xea\xb0\xba\xa0\x93\xa7\x25\x00\x70\x00\x70\
\x02\x70\xf7\x77\x75\x99\x84\x12\x26\x49\xd2\xa2\xbf\x8a\x19\xa5\
\x97\x1e\x2b\x54\x55\xe5\x1d\x59\x95\x4b\x66\x82\xcf\x4f\x91\x6d\
\xfa\xb2\x4f\xdf\xad\x33\xfb\xc4\xa0\x81\x6b\x37\x6f\xa6\x9a\x8c\
\x8d\xf4\xde\xba\xe5\x00\x40\x01\x18\xb3\x01\x7a\x44\xcd\x31\x79\
\x7e\xc7\x60\x6b\xdd\xad\xd9\xeb\xb3\x53\xc4\xcf\x03\x08\x78\x38\
\x52\xd9\x63\x59\x59\xd9\xc3\x43\x43\x9d\xa1\x50\x48\x99\x0e\xbe\
\xa4\xd1\xc9\x2d\x71\x6f\x59\x73\xf8\x3f\xd5\x3f\x55\x81\x0c\xb0\
\x89\xd2\x85\x45\x00\x00\x00\x25\x74\x45\x58\x74\x64\x61\x74\x65\
\x3a\x63\x72\x65\x61\x74\x65\x00\x32\x30\x31\x36\x2d\x30\x39\x2d\
\x32\x31\x54\x31\x32\x3a\x35\x37\x3a\x34\x30\x2d\x30\x30\x3a\x30\
\x30\x90\x54\x97\x25\x00\x00\x00\x25\x74\x45\x58\x74\x64\x61\x74\
\x65\x3a\x6d\x6f\x64\x69\x66\x79\x00\x32\x30\x31\x36\x2d\x30\x39\
\x2d\x32\x31\x54\x31\x32\x3a\x35\x37\x3a\x34\x30\x2d\x30\x30\x3a\
\x30\x30\xe1\x09\x2f\x99\x00\x00\x00\x19\x74\x45\x58\x74\x53\x6f\
\x66\x74\x77\x61\x72\x65\x00\x77\x77\x77\x2e\x69\x6e\x6b\x73\x63\
\x61\x70\x65\x2e\x6f\x72\x67\x9b\xee\x3c\x1a\x00\x00\x00\x00\x49\
\x45\x4e\x44\xae\x42\x60\x82\
\x00\x00\x03\xe6\
\x89\
\x50\x4e\x47\x0d\x0a\x1a\x0a\x00\x00\x00\x0d\x49\x48\x44\x52\x00\
\x00\x00\x18\x00\x00\x00\x18\x08\x06\x00\x00\x00\xe0\x77\x3d\xf8\
\x00\x00\x00\x06\x62\x4b\x47\x44\x00\xfe\x00\xfe\x00\xfe\xeb\x18\
\xd4\x82\x00\x00\x00\x09\x70\x48\x59\x73\x00\x00\x0d\xd6\x00\x00\
\x0d\xd6\x01\x90\x6f\x79\x9c\x00\x00\x00\x09\x76\x70\x41\x67\x00\
\x00\x00\x18\x00\x00\x00\x18\x00\x78\x4c\xa5\xa6\x00\x00\x02\xea\
\x49\x44\x41\x54\x48\xc7\xd5\x95\x4d\x48\x54\x51\x14\xc7\xff\xef\
\xcd\x73\x46\xcb\x89\xcc\x94\xd1\x10\xb4\x94\xe9\x43\x0c\xca\xca\
\x18\x8c\x5a\x44\x9a\x7d\x2e\x54\x68\xd1\xc2\x4d\x6e\x94\x16\x83\
\x48\x2b\x17\x11\x05\x15\x54\xeb\x16\x41\x9b\x30\x90\xca\xb0\x82\
\xc0\x8a\xe7\xd0\x14\x11\x7d\x68\x2e\xd2\x51\x9b\xc9\x30\x43\xf4\
\xbe\xef\x7b\xee\x6b\xe1\x98\x15\x81\x6f\x2a\x82\x0e\x5c\xee\xe2\
\x9e\x7b\x7e\xf7\x7f\xcf\x3d\xf7\x00\xff\xbb\xf9\x3c\xfa\x49\x27\
\xa3\xad\xbb\x4b\xd6\x94\x4d\x0c\x0e\x0e\xba\x99\x00\x24\x2f\x4e\
\xd1\xce\xf6\x17\xb2\x2c\xaf\x17\x44\x1f\x72\x73\xf2\x37\x76\x75\
\x75\x71\xaf\x00\xd9\x8b\x13\x71\xbe\xf9\x70\x43\x63\x0e\x27\xbe\
\x36\x81\x84\x92\x89\x82\x25\x01\x1d\x1d\x2d\x41\x12\x24\x97\x96\
\x96\x82\x48\x64\x12\x7b\x69\x40\x47\x47\x4b\xd0\xf5\x05\xfb\x38\
\x09\x4c\x4f\x7f\x06\xe7\x04\x24\xfe\x12\x20\x1a\x6d\x2d\x14\xbe\
\xe5\xcf\x2b\x2b\xab\xb6\x09\x12\x50\x94\xac\xdf\x52\xf0\xc3\x7d\
\x46\x3b\xdb\x6f\x0b\x41\x7b\x7d\xb2\xaf\x1f\x40\x65\xcd\x8e\x48\
\x68\xe7\xf6\x5a\x25\x16\x8b\xc1\xef\xf7\x83\x88\xe0\xf1\x5d\xfc\
\x5a\xc1\x1c\x63\x07\x8f\x1c\x68\xca\x9e\xd3\xb4\x7d\x75\x75\x0d\
\xc5\xb5\x91\x3d\x4a\x28\x14\x82\x10\x02\x81\x40\x00\x44\xe2\xbb\
\xe8\xae\x54\xd6\x70\x26\x1a\x3e\x74\x2e\xe8\x09\xd0\x7c\xac\xf9\
\xb8\x69\xd8\x28\x28\x28\x84\x65\x3a\x52\xf5\x96\x1a\x39\x7f\x55\
\x3e\x66\x67\x67\x61\x5b\x1c\xba\xae\x83\x13\xc9\x79\xab\xf3\x7a\
\xe6\x77\x48\x2e\x64\x5f\x05\x01\x17\x3c\x01\x24\xb8\xe7\x4d\xd3\
\x42\x71\x71\x11\xb8\x43\xf0\xfb\xfd\x18\x1d\x1b\x41\xec\xa9\x0a\
\xdb\xb1\xc1\x18\x03\x71\xc2\x44\xf2\xe3\xee\xc6\xc6\xc6\x32\x00\
\xa8\x08\x97\x9d\x0d\x6f\x28\xdf\xef\x29\x07\x44\x54\x60\x71\x07\
\x43\x43\xef\xc0\x74\x1d\xef\x86\x87\x60\xe8\x3a\x6c\xdb\x01\x27\
\x02\xd3\x18\x38\x27\x8c\x8f\x7f\x82\xe9\x58\x00\x80\x50\x51\xde\
\xca\x60\xce\x0a\xcd\x13\x40\x92\xe4\x94\x69\xda\xc5\x93\x93\x93\
\x30\x0c\x0b\xb2\x24\xc3\xb6\x6d\x18\xba\x0e\xee\x70\x68\x4c\x03\
\x71\x01\x21\x44\xff\xab\x78\x7c\xb4\xbe\xed\x72\x20\x39\x36\x75\
\x49\x51\xbe\x5c\xf7\x74\x45\xc2\xe5\x27\x4c\xc3\x42\x2a\x95\x82\
\xa1\x9b\x6e\x3c\x1e\x17\x70\x25\x98\xa6\x05\x4e\x02\x8c\x31\x38\
\xc4\x45\x6e\x38\xeb\x28\x00\xf4\x5d\x69\xb3\xdf\xbf\x4f\x5c\xbd\
\x7f\xb1\xe9\xb4\x27\xc0\xcd\x1b\x3d\xbd\x86\x69\x23\x99\x4c\xc2\
\x30\x6d\xba\x75\xb7\x37\xa5\xc6\x54\xae\x28\x0a\x88\xd3\x42\x0e\
\xdc\xc5\x42\x93\xdc\xc4\xdd\x53\xd7\x00\xc9\xf5\x04\x00\x00\xee\
\xd0\xc0\x9d\x7b\x0f\x84\x63\x73\xd5\xd6\xcc\xad\x0f\x1f\x3d\x1a\
\x79\x32\xa0\x5a\xf3\x39\xd0\xc0\x89\x90\xa9\xfd\x50\x68\xe5\xa5\
\x25\xbb\x9e\x4d\x4d\x65\x25\xfa\xfb\x6d\x00\x22\x12\x89\x54\xbf\
\x79\x3b\xd8\x97\x1d\x08\x44\x34\xc6\xfe\xbc\x92\xbb\xbb\xbb\x09\
\xc0\xb7\x63\xaa\xaa\x3a\x17\x8e\x44\xea\x43\x8a\x98\x65\x6c\xfe\
\x15\x65\x56\xc7\xbf\xfe\x8b\x14\x00\xd9\x00\x96\x01\xc8\x1d\x56\
\x55\x97\x13\x17\x8c\xb1\xf4\x57\xf1\xfb\x0a\xfc\xe9\x11\x48\xcf\
\x59\x0b\xeb\xdc\xa1\xa1\x67\x2f\x5f\xae\x73\x85\x48\xbd\x79\xfd\
\x3a\x3b\xad\xd2\xf1\x02\xf8\x5e\xb1\xfc\x13\x40\xc1\x62\x4b\x15\
\x9b\xaa\xaa\xaa\x93\xe3\xe3\x8f\x67\x66\x66\xf4\x74\x70\x4f\xad\
\x53\xf2\xb8\x96\x51\x1f\xfe\xa7\xf6\x15\xc3\x26\x81\x85\x5c\x34\
\x41\x84\x00\x00\x00\x25\x74\x45\x58\x74\x64\x61\x74\x65\x3a\x63\
\x72\x65\x61\x74\x65\x00\x32\x30\x31\x36\x2d\x30\x39\x2d\x32\x31\
\x54\x31\x32\x3a\x35\x37\x3a\x34\x30\x2d\x30\x30\x3a\x30\x30\x90\
\x54\x97\x25\x00\x00\x00\x25\x74\x45\x58\x74\x64\x61\x74\x65\x3a\
\x6d\x6f\x64\x69\x66\x79\x00\x32\x30\x31\x36\x2d\x30\x39\x2d\x32\
\x31\x54\x31\x32\x3a\x35\x37\x3a\x34\x30\x2d\x30\x30\x3a\x30\x30\
\xe1\x09\x2f\x99\x00\x00\x00\x19\x74\x45\x58\x74\x53\x6f\x66\x74\
\x77\x61\x72\x65\x00\x77\x77\x77\x2e\x69\x6e\x6b\x73\x63\x61\x70\
\x65\x2e\x6f\x72\x67\x9b\xee\x3c\x1a\x00\x00\x00\x00\x49\x45\x4e\
\x44\xae\x42\x60\x82\
\x00\x00\x04\x63\
\x89\
\x50\x4e\x47\x0d\x0a\x1a\x0a\x00\x00\x00\x0d\x49\x48\x44\x52\x00\
\x00\x00\x18\x00\x00\x00\x18\x08\x06\x00\x00\x00\xe0\x77\x3d\xf8\
\x00\x00\x00\x06\x62\x4b\x47\x44\x00\xfe\x00\xfe\x00\xfe\xeb\x18\
\xd4\x82\x00\x00\x00\x09\x70\x48\x59\x73\x00\x00\x0d\xd6\x00\x00\
\x0d\xd6\x01\x90\x6f\x79\x9c\x00\x00\x00\x09\x76\x70\x41\x67\x00\
\x00\x00\x18\x00\x00\x00\x18\x00\x78\x4c\xa5\xa6\x00\x00\x03\x67\
\x49\x44\x41\x54\x48\xc7\xd5\x55\xdf\x6b\x5b\x65\x18\x7e\xce\x8f\
\xfc\xa8\x4b\xaf\xd6\x8e\x3a\xd1\x76\x16\x99\xb8\x5a\x59\xd9\x6a\
\x67\x10\x8a\x28\x32\x46\x29\x22\xa9\x66\x65\x1d\xec\x6a\xde\x0c\
\x2f\x42\x28\xbd\xb1\xde\xf4\x42\xbd\x9d\x7f\xc0\x44\x87\x04\xd4\
\x6e\xca\x44\x14\x53\x25\x16\x32\x91\xe1\xa4\x4d\x1d\xb8\xb6\x33\
\x59\xb7\x39\x28\xdd\xc9\xc9\xf9\xbe\xf3\xbe\xef\xf1\xa2\x49\xda\
\x54\x65\xc9\x10\xc1\x17\x0e\xe7\xe2\x7d\x79\x9e\xef\x79\x7f\x02\
\xff\x77\xb3\x9a\x8c\x33\xde\x4c\x9d\x1e\x7e\xf4\x91\x7d\x37\x16\
\x16\x16\x82\x56\x08\x8c\x66\x82\x52\x93\x67\x7e\x32\x4d\xf3\x49\
\x61\xfe\x3d\xd6\xb6\xfb\xa9\xe9\xe9\x69\x6a\x96\xc0\x6c\x26\x88\
\x89\x9e\x19\x3d\x96\x68\x23\xa6\xc7\x97\xb1\x6c\xb7\xa2\xe0\xbe\
\x04\xe9\xf4\xa9\x76\x16\x36\x7b\x7a\x7a\xc0\x2c\xad\x60\xdf\x9f\
\x20\x9d\x3e\xd5\x1e\x58\xed\x97\x88\x05\x77\xef\xfe\x01\x22\x06\
\x96\xff\x25\x82\x54\xea\xf4\x1e\xb1\x76\xfd\xd8\xd7\xd7\x7f\x58\
\x58\x60\xdb\xa1\x07\x52\xd0\x90\xcf\xd4\xe4\x99\x0b\x22\xfc\x92\
\x65\x5a\x59\x00\x7d\x43\xcf\xc6\xbb\x8e\x0c\x3e\x6f\xcf\xcf\xcf\
\x23\x1c\x0e\x83\x99\x51\xeb\x8b\x77\xde\x9b\x79\x5b\x24\x98\xda\
\x89\x51\x35\x02\x8c\x99\xc9\xf4\xd4\x5b\x0d\xce\x7b\x8e\x33\x32\
\x3e\x76\x12\x1f\x65\xce\xbd\x9c\x78\x75\x2c\x78\xfa\xc0\x41\xb3\
\x63\x77\x07\x44\x04\x91\x48\x04\xcc\x62\xd4\x3a\x9b\x88\xa7\x0e\
\x0e\x0c\xd8\x6d\xd1\x28\x0c\xc3\x80\x88\x80\x88\xe0\x13\xc1\xab\
\x54\xec\x42\xa1\x30\x05\x60\x8b\x20\x99\x1c\x3b\xe9\x55\x34\x3a\
\x3b\xf7\x40\x79\xbe\x71\x68\x60\xc8\x88\xed\x8a\x61\x63\x63\x03\
\x5a\x11\x5c\xd7\x05\x31\x9b\x9d\x1d\x1d\x9f\x02\x38\xaa\xb5\xb6\
\x23\xe1\x30\xce\x9e\x7d\x1f\x00\x70\x62\x62\x1c\x1f\x9c\xfb\x10\
\x00\x30\x31\x71\x02\x5a\x6b\xbb\x21\x45\x81\x81\x77\x3d\x4f\x61\
\xef\xde\x87\x41\x3e\x23\x1c\x0e\xe3\xfa\xca\x6f\xb8\x76\xed\x57\
\x68\x5f\xc3\x71\x1c\x30\x31\x6e\x14\x6f\x0e\x27\x12\x89\x7d\x4a\
\x29\x04\xd8\x9a\xb9\x1a\x78\xcd\x94\x52\x8d\x45\x66\xe6\xce\x8a\
\xa7\xb0\xb8\x58\x80\xe3\xba\x28\x2c\x2d\xe2\xf6\xad\x5b\xd0\xda\
\x07\x31\xc3\x29\x3b\x20\x62\xac\xae\x16\xb1\xb4\xb2\x02\xa5\x34\
\x84\x05\xc9\xe4\x6b\x0d\xc0\xa3\xa3\x23\x10\x11\x28\xa5\x1b\x09\
\x0c\xc3\x2c\x79\x9e\xc6\xda\xda\x1a\x2a\x15\x05\xd3\x30\xa1\xb5\
\x46\xc5\x75\x41\x3e\xa1\xec\x94\xc1\x24\x10\x91\xec\xcf\xf9\xfc\
\x75\xad\x15\x88\x18\xe7\xcf\x7f\xdc\x40\x30\x3b\x7b\x11\x22\x01\
\xb4\xde\xa1\x20\x60\x7e\xc3\xab\x28\x94\x4a\x25\x54\x5c\x2f\xc8\
\xe7\xf3\x82\xc0\x80\xe7\x29\x10\x0b\x1c\xc7\x81\xcf\x24\xb1\xfd\
\xa1\x57\x36\x53\xa0\x41\xe4\xd7\x81\x47\x46\x8e\x61\x2b\x1b\x54\
\x57\x50\xaf\x41\x26\xf3\xc9\x85\xc3\xcf\xc5\x51\x2c\x16\x51\xf1\
\x34\xcf\x7e\xf1\xf9\xda\x91\xc1\xc1\xae\xee\xc7\xba\x6d\x26\xae\
\xd5\x20\xa8\x0d\x9a\xd2\x8a\xca\x4e\xd9\x1e\x3f\x7e\x7c\xb3\x73\
\x03\x20\x99\x7c\x1d\xc2\x02\xd7\x75\xa1\xb4\xa2\xbf\xcc\x01\xf9\
\xfc\xc3\xc5\x2f\xbf\x1a\xb2\x4c\x2b\xa7\xcb\xde\xd8\x37\x73\x73\
\xdf\x3f\xd1\xdb\xdb\x4d\xcc\x11\xa7\x5c\x06\x31\xd7\x63\x03\x09\
\x66\x3e\x9b\x9d\xfd\xc7\x39\xb0\x2c\x6b\x06\xd8\xb1\x4d\x13\x89\
\x84\x75\xf9\xce\x9d\xd0\x72\x36\xab\x01\x48\x3c\x1e\x6f\x47\xc8\
\xba\x14\x8d\x44\xe2\x2f\x0e\xbf\x80\xaf\xe7\xbe\x65\xf6\x74\x2c\
\x9b\xcd\x7a\x0f\x34\xc9\x99\x4c\x86\x01\xd4\x9f\x99\xcb\xe5\xee\
\xed\x8f\xc7\x8f\x76\xd9\xb2\xe1\x38\x9b\x5d\xd4\xd4\x7e\xdf\x66\
\x7f\xb7\x8b\x6c\x00\x51\x00\x0f\x01\x88\x2d\xe5\x72\x01\x31\x89\
\xe3\x38\xd5\x55\xd1\x9a\x6d\x57\x10\xae\x7e\x91\xea\x3f\x54\xf3\
\x93\xcf\x8b\x97\xaf\x5c\xe9\x0d\x44\x4a\xbf\x5c\xbd\x1a\xad\xaa\
\xf4\x9b\x21\xd8\xae\xd8\xdc\x41\x60\x63\xeb\xa4\xca\x81\xfe\xfe\
\x43\xc5\xd5\xd5\xef\xd6\xd7\xd7\xdd\x2a\x78\x53\xa7\xd3\x68\xd2\
\xd7\xd2\x1d\xfe\x4f\xed\x4f\x93\x7f\xd3\xf8\x62\xa4\xf6\x59\x00\
\x00\x00\x25\x74\x45\x58\x74\x64\x61\x74\x65\x3a\x63\x72\x65\x61\
\x74\x65\x00\x32\x30\x31\x36\x2d\x30\x39\x2d\x32\x31\x54\x31\x32\
\x3a\x35\x37\x3a\x34\x30\x2d\x30\x30\x3a\x30\x30\x90\x54\x97\x25\
\x00\x00\x00\x25\x74\x45\x58\x74\x64\x61\x74\x65\x3a\x6d\x6f\x64\
\x69\x66\x79\x00\x32\x30\x31\x36\x2d\x30\x39\x2d\x32\x31\x54\x31\
\x32\x3a\x35\x37\x3a\x34\x30\x2d\x30\x30\x3a\x30\x30\xe1\x09\x2f\
\x99\x00\x00\x00\x19\x74\x45\x58\x74\x53\x6f\x66\x74\x77\x61\x72\
\x65\x00\x77\x77\x77\x2e\x69\x6e\x6b\x73\x63\x61\x70\x65\x2e\x6f\
\x72\x67\x9b\xee\x3c\x1a\x00\x00\x00\x00\x49\x45\x4e\x44\xae\x42\
\x60\x82\
"

qt_resource_name = "\
\x00\x09\
\x0c\x78\x54\x88\
\x00\x6e\
\x00\x65\x00\x77\x00\x50\x00\x72\x00\x65\x00\x66\x00\x69\x00\x78\
\x00\x1d\
\x04\xe2\x2f\xc7\
\x00\x6d\
\x00\x75\x00\x6c\x00\x74\x00\x69\x00\x6d\x00\x65\x00\x64\x00\x69\x00\x61\x00\x2d\x00\x76\x00\x6f\x00\x6c\x00\x75\x00\x6d\x00\x65\
\x00\x2d\x00\x63\x00\x6f\x00\x6e\x00\x74\x00\x72\x00\x6f\x00\x6c\x00\x2e\x00\x70\x00\x6e\x00\x67\
\x00\x17\
\x0c\x49\x77\x27\
\x00\x61\
\x00\x75\x00\x64\x00\x69\x00\x6f\x00\x2d\x00\x76\x00\x6f\x00\x6c\x00\x75\x00\x6d\x00\x65\x00\x2d\x00\x6d\x00\x65\x00\x64\x00\x69\
\x00\x75\x00\x6d\x00\x2e\x00\x70\x00\x6e\x00\x67\
\x00\x15\
\x04\x57\xa1\xc7\
\x00\x61\
\x00\x75\x00\x64\x00\x69\x00\x6f\x00\x2d\x00\x76\x00\x6f\x00\x6c\x00\x75\x00\x6d\x00\x65\x00\x2d\x00\x68\x00\x69\x00\x67\x00\x68\
\x00\x2e\x00\x70\x00\x6e\x00\x67\
\x00\x14\
\x09\xd2\x98\xc7\
\x00\x61\
\x00\x75\x00\x64\x00\x69\x00\x6f\x00\x2d\x00\x76\x00\x6f\x00\x6c\x00\x75\x00\x6d\x00\x65\x00\x2d\x00\x6c\x00\x6f\x00\x77\x00\x2e\
\x00\x70\x00\x6e\x00\x67\
\x00\x16\
\x02\x78\xcb\xa7\
\x00\x61\
\x00\x75\x00\x64\x00\x69\x00\x6f\x00\x2d\x00\x76\x00\x6f\x00\x6c\x00\x75\x00\x6d\x00\x65\x00\x2d\x00\x6d\x00\x75\x00\x74\x00\x65\
\x00\x64\x00\x2e\x00\x70\x00\x6e\x00\x67\
"

qt_resource_struct = "\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x01\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x05\x00\x00\x00\x02\
\x00\x00\x00\xea\x00\x00\x00\x00\x00\x01\x00\x00\x12\x5b\
\x00\x00\x00\x8c\x00\x00\x00\x00\x00\x01\x00\x00\x09\x15\
\x00\x00\x00\x18\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\
\x00\x00\x00\xbc\x00\x00\x00\x00\x00\x01\x00\x00\x0e\x71\
\x00\x00\x00\x58\x00\x00\x00\x00\x00\x01\x00\x00\x04\x88\
"

def qInitResources():
    QtCore.qRegisterResourceData(0x01, qt_resource_struct, qt_resource_name, qt_resource_data)

def qCleanupResources():
    QtCore.qUnregisterResourceData(0x01, qt_resource_struct, qt_resource_name, qt_resource_data)

qInitResources()

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    Dialog = QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
