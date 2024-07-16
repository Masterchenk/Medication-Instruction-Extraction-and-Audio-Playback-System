from PyQt5.QtWidgets import QApplication, QMainWindow,  QVBoxLayout, QMessageBox,QFileDialog
from PyQt5.QtWidgets import  QWidget
from PyQt5.QtGui import QMovie
from PyQt5 import uic
from PyQt5 import QtCore
import sys
class Mainwindow3(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(800, 600)
        # 加载UI文件并设置为中心窗口
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
        self.central_widget = QWidget()
        self.waiting_page = uic.loadUi('ui/waiting_page.ui', self.central_widget)  # 加载UI文件
        self.setCentralWidget(self.central_widget)
        self.waiting_page.minimized.clicked.connect(self.showMinimized)
        self.waiting_page.closed.clicked.connect(self.close)
        self.movie = QMovie(r"ui\loading.gif")
        self.waiting_page.loading.setMovie(self.movie)
        self.waiting_page.loading.setScaledContents(True)  # 使图像适应 QLabel 的大小

        self.movie.start()
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

