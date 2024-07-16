import sys
from PyQt5.QtWidgets import QApplication,QTextBrowser, QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout
from PyQt5.QtGui import QFont
import pyttsx3
from PyQt5 import uic
import threading
from PyQt5.QtGui import QFont, QColor
from PyQt5.QtWidgets import QLabel, QVBoxLayout
from PyQt5 import QtCore

class Mainwindow4(QMainWindow):
    def __init__(self, text_ui, speech_ui):
        super().__init__()
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
        self.resize(800, 600)
        self.central_widget = QWidget()
        self.display_page = uic.loadUi('ui/display_page.ui', self.central_widget)
        self.setCentralWidget(self.central_widget)
        self.display_page.minimized.clicked.connect(self.showMinimized)
        self.display_page.closed.clicked.connect(self.close)
        self.display_page.closed.clicked.connect(self.closeEvent)


        self.display_layout = self.findChild(QVBoxLayout, 'display_layout')


        self.speech_text = speech_ui
        self.display_text(text_ui)
        self.display_page.sound.clicked.connect(self.play_speech)

    def display_text(self, text):
        # 设置字体大小
        font = QFont()
        font.setPointSize(25)  # 调整字体大小，单位为点（pt）
        font.setBold(True)  # 设置为粗体
        font.setFamily("Microsoft YaHei")#设为微软雅黑

        text = text.replace(" ","")

        self.display_page.textBrowser.setText(text)
        self.display_page.textBrowser.setFont(font)

    def play_speech(self):
        # 使用线程播放语音
        threading.Thread(target=self.speak_text).start()

    def speak_text(self):
        # 初始化语音合成引擎
        engine = pyttsx3.init()
        engine.setProperty('rate', 150)  # 设置语速
        # 设置要播报的文本
        engine.say(self.speech_text)
        # 运行语音合成引擎
        engine.runAndWait()

   # 拖拽窗口功能实现

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()
            event.accept()

    def mouseMoveEvent(self, event):
        if self.m_flag:
            self.move(event.globalPos() - self.m_Position)
            event.accept()

    def mouseReleaseEvent(self, event):
        self.m_flag = False



