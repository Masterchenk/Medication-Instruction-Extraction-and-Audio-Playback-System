from OCR_main_ui import *
from upload_page import *
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow,  QVBoxLayout, QMessageBox,QFileDialog
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import QThread, pyqtSignal
import display_page
import option_page
import waiting_page
import Qwen1
import os
import shutil
import sys
class Worker(QThread):
    finished = pyqtSignal(str, str)

    def __init__(self, Info):
        super().__init__()
        self.Info = Info

    def run(self):
        # 在后台线程中执行耗时操作
        ui_text, speech_text = Qwen1.get_drug_info_from_images(r'images\image.jpg', self.Info)
        self.finished.emit(ui_text, speech_text)

class MainApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.pushButton_4.clicked.connect(self.showMinimized)
        self.pushButton_5.clicked.connect(self.close)
        self.show()
        self.pushButton.clicked.connect(self.go_to_first_page)
        self.pushButton_2.clicked.connect(self.go_to_second_page)
        QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)

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

    #进入上传页面

    # 进入上传页面的第一个页面
    def go_to_first_page(self):
        self.upload_page = UploadPage()
        self.upload_page.stackedWidget.setCurrentIndex(0)  # 假设第一个页面的索引是0
        self.close()



    # 进入上传页面的第二个页面

    def go_to_second_page(self):
        self.upload_page = UploadPage()
        self.upload_page.stackedWidget.setCurrentIndex(1)  # 假设第二个页面的索引是1
        self.close()



#根据选择进入上传页面，同时也可以通过上传页面中的图标来变化选择功能
class UploadPage(QMainWindow, Ui_upload_page):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.pushButton_4.clicked.connect(self.showMinimized)
        self.pushButton_5.clicked.connect(self.close)
        self.pushButton.clicked.connect(self.switch_to_first_page)
        self.pushButton_2.clicked.connect(self.switch_to_second_page)
        self.shoot.clicked.connect(self.capture)
        self.shoot_2.clicked.connect(self.uploadFileFolder)
        self.pre_shoot.clicked.connect(self.showcamera)
        self.pushButton_3.clicked.connect(self.change_option_page)
        self.pushButton_7.clicked.connect(self.change_option_page)
        self.camera_initialized = False
        self.show()
        QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
        # 初始化摄像头相关的属性
        self.viewfinder = None
        self.camera = None
        self.capImg = None
        self.available_cameras = []
        self.camera_initialized = False
        self.shoot.hide()



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
# 切换到第一个页面
    def switch_to_first_page(self):
        self.stackedWidget.setCurrentIndex(0)

    # 切换到第二个页面
    def switch_to_second_page(self):
        self.stackedWidget.setCurrentIndex(1)

    #本地上传文件功能实现
    def uploadFileFolder(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_name, _ = QFileDialog.getOpenFileName(self, "Open Image File", "", "Image Files (*.png *.jpg *.bmp)",
                                                   options=options)
        if file_name:
            # 加载并显示选择的图片
            pixmap = QPixmap(file_name)
            self.cam_pic.setPixmap(pixmap)
            self.cam_pic.setScaledContents(True)  # 使图像适应 QLabel 的大小

            target_folder = r"images"
            name = "image.jpg"

            shutil.copy(file_name,os.path.join(target_folder,name))


  #摄影功能（打开摄像头）
    def showcamera(self):
        self.cam_pic_1.clear()

        # 创建一个QCameraViewfinder
        self.viewfinder = QCameraViewfinder(self.cam_pic_1)

        # 将QCameraViewfinder添加到QLabel的布局中
        if not isinstance(self.layout, QVBoxLayout):
            self.layout = QVBoxLayout(self.cam_pic_1)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.addWidget(self.viewfinder)

        # 创建一个摄像头实例，并将其设置为QCameraViewfinder的视图
        self.available_cameras = QCameraInfo.availableCameras()
        if not self.available_cameras:
            QMessageBox.warning(self, "警告", "摄像头不可用！")
        else:
            self.shoot.show()
            self.camera = QCamera(self.available_cameras[0])
            self.camera.setViewfinder(self.viewfinder)
            self.camera.start()

            self.capImg = QCameraImageCapture(self.camera)
            self.capImg.imageCaptured.connect(self.display_captured_image)

    def capture(self):
        if self.capImg:
            self.capImg.capture()
            self.shoot.hide()


    def display_captured_image(self, id, image):
        # 将捕获的照片转换为 QPixmap 并设置为 cam_pic_1 的显示内容
        pixmap = QPixmap.fromImage(image)
        self.cam_pic_1.setPixmap(pixmap)
        self.cam_pic_1.setScaledContents(True)  # 使图像适应 QLabel 的大小
        self.viewfinder.hide()
        # 保存pixmap
        file_path = os.path.join('images', 'image.jpg')
        # 保存 QPixmap 图像到文件
        pixmap.save(file_path)
        self.camera.stop()

    def change_option_page(self):
        # 检查images文件夹是否为空
        folder = os.listdir(r'images')
        if len(folder) == 0:
            # 弹出警告对话框
            QMessageBox.warning(self,"警告", "请先上传说明书图片！")
            return
        else:
            # 获取UploadPage实例，并关闭它
            self.close()
            # 实例化并显示option_page.Mainwindow2
            self.option_page = option_page.Mainwindow2()
            self.option_page.show()
            self.option_page.option_page.OK.clicked.connect(self.getInfo)

    def change_waiting_page(self):
        self.worker = Worker(self.Info)
        self.worker.finished.connect(self.change_display_page)
        self.waiting_page = waiting_page.Mainwindow3()
        self.waiting_page.show()

        # 启动后台线程
        self.worker.start()

    def change_display_page(self, ui_text, speech_text):
        # 在主线程中更新UI
        self.display_page = display_page.Mainwindow4(ui_text, speech_text)
        self.waiting_page.close()
        self.display_page.show()

    def getInfo(self):
        if not self.option_page.allNone():
            self.Info = self.option_page.Info
            self.option_page.close()
            self.change_waiting_page()

if __name__ == "__main__":
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    mainWindow = MainApp()
    mainWindow.show()
    sys.exit(app.exec_())