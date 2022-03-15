# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 10:43:06 2022

@author: Benjamin
"""
import sys
import download_yt

import os
import pygame
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel, QWidget
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QListWidget
from PyQt5.QtCore import QSettings
import playsound

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.settings = QSettings('MyQtApp', 'App1')
        self.setWindowTitle('QDialog')

        layout = QGridLayout()
        
        layout.addWidget(QLabel('Directory:'), 0,0)
        self.line = QLineEdit(self.settings.value('path'), self)
        layout.addWidget(self.line, 0, 1)
        self.btn = QPushButton("Enter")
        layout.addWidget(self.btn, 0, 2)
        
        
        
        layout.addWidget(QLabel('Download'), 1,0)
        self.link = QLineEdit(self)
        layout.addWidget(self.link, 1, 1)
        self.down = QPushButton("Download")
        layout.addWidget(self.down, 1, 2)
        
        self.info = QListWidget()
        
        self.btn.clicked.connect(self.enterDir)
        self.down.clicked.connect(self.download)
        self.files = QListWidget()
        layout.addWidget(self.files, 3, 0)
        layout.addWidget(self.info, 3, 1)
        self.files.itemDoubleClicked.connect(self.play)
        
        
        try:
            self.setValue(self.settings.value('path'))
            self.resize(self.settings.value('window size'))
            self.move(self.settings.value('window position'))
        except:
            pass
        
        self.setLayout(layout)
            
        
    def play(self, poop):
        
        deez = self.settings.value('path')+ "\\" + poop.text()
        os.system(deez)
         

        
    def download(self, event):
        download_yt.download_link(self.link.text(), self.settings.value('path'))
        print("downloaded")
        self.listFiles(self.settings.value('path'))
        
    def listFiles(self, path):
        file_list = os.listdir(path)
        self.files.clear()
        for i in range(len(file_list)):
            self.files.addItem(file_list[i])
        return file_list
        
    def enterDir(self, event):
        self.settings.setValue('path', self.line.text())
        
        self.listFiles(self.settings.value('path'))
    
    def closeEvent(self, event):
        self.settings.setValue('path', self.line.text())
        self.settings.setValue('window size', self.size())
        self.settings.setValue('window position', self.pos())
        
        
        
        
app = QApplication(sys.argv)
demo =  MyApp()
demo.show()
sys.exit(app.exec_())
