from PyQt5.QtWidgets import QMainWindow, QWidget, QRadioButton, QCheckBox, QMessageBox
from PyQt5 import uic
from PyQt5 import QtCore
from PyQt5.QtGui import QIcon
import sys

class Mainwindow2(QMainWindow):
    def __init__(self):
        super().__init__()
        # 加载UI文件并设置为中心窗口
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.central_widget = QWidget()
        self.option_page = uic.loadUi('ui/option.ui', self.central_widget)  # 加载UI文件
        self.setCentralWidget(self.central_widget)
        self.option_page.lineEdit.hide()
        self.option_page.minimized.clicked.connect(self.showMinimized)
        self.option_page.closed.clicked.connect(self.close)
        self.setupInfo(self)
        self.center()  # 新增：使窗口居中显示
        QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)

        # 设置鼠标事件监听
        self.m_flag = False
        self.m_Position = None

    def center(self):
        """将窗口置于屏幕中心"""
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def setupInfo(self, MainWindow):
        self.resize(800, 600)
        self.option_page.OK.clicked.connect(self.OK)
        self.option_page.others.clicked.connect(self.others)

    def OK(self):
        if self.allNone():
            QMessageBox.warning(self.option_page, "警告", "至少选择一项查询信息！")
            self.option_page.basic.setChecked(True)
            if self.option_page.others.isChecked():
                self.option_page.others.setChecked(False)
                self.option_page.lineEdit.hide()
        else:
            self.Info = {}
            self.checkAgeButton()
            self.optionalInfoButton()

    def others(self):
        if self.option_page.others.isChecked():
            self.option_page.lineEdit.show()
        else:
            self.option_page.lineEdit.hide()
            self.option_page.lineEdit.clear()

    def allNone(self):
        for radio_button in self.option_page.findChildren(QRadioButton):
            if radio_button.isChecked():
                return 0

        for checkbox in self.option_page.findChildren(QCheckBox):
            if checkbox.isChecked():
                if checkbox == self.option_page.others and not self.option_page.lineEdit.text():
                    continue
                return 0
        return 1

    def checkAgeButton(self):
        for radio_button in self.option_page.findChildren(QRadioButton):
            if radio_button.isChecked():
                age = radio_button.text()
                self.Info['age'] = age

    def optionalInfoButton(self):
        optionInfo = []
        for checkbox in self.option_page.findChildren(QCheckBox):
            if checkbox.isChecked():
                if checkbox == self.option_page.others and self.option_page.lineEdit.text():
                    self.Info['others'] = self.option_page.lineEdit.text()
                else:
                    optionInfo.append(checkbox.text())
        if '基本信息（通用）' in optionInfo:
            for info in ['用法用量', '使用禁忌']:
                if info not in optionInfo:
                    optionInfo.append(info)
            optionInfo.remove('基本信息（通用）')
        self.Info['optionInfo'] = optionInfo

    #可拖动实现
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