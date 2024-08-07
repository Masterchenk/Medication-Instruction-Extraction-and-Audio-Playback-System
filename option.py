# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'option.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(619, 417)
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(30, 110, 561, 291))
        self.groupBox.setStyleSheet("font: 25pt \"华文琥珀\";\n"
"\n"
"color: rgb(54, 179, 152);")
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName("groupBox")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(10, 72, 111, 41))
        font = QtGui.QFont()
        font.setFamily("华文琥珀")
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("\n"
"font: 25pt \"华文琥珀\";\n"
"color: rgb(54, 179, 152);")
        self.label_3.setObjectName("label_3")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(10, 140, 111, 41))
        font = QtGui.QFont()
        font.setFamily("华文琥珀")
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("\n"
"font: 25pt \"华文琥珀\";\n"
"color: rgb(54, 179, 152);")
        self.label_6.setObjectName("label_6")
        self.basic = QtWidgets.QCheckBox(self.groupBox)
        self.basic.setGeometry(QtCore.QRect(280, -10, 221, 71))
        font = QtGui.QFont()
        font.setFamily("华文琥珀")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.basic.setFont(font)
        self.basic.setStyleSheet("font: 20pt \"华文琥珀\";\n"
"color: rgb(54, 179, 152);")
        self.basic.setChecked(True)
        self.basic.setObjectName("basic")
        self.kid = QtWidgets.QRadioButton(self.groupBox)
        self.kid.setGeometry(QtCore.QRect(260, 70, 141, 41))
        font = QtGui.QFont()
        font.setFamily("华文琥珀")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.kid.setFont(font)
        self.kid.setStyleSheet("font: 20pt \"华文琥珀\";\n"
"color: rgb(54, 179, 152);")
        self.kid.setObjectName("kid")
        self.adult = QtWidgets.QRadioButton(self.groupBox)
        self.adult.setGeometry(QtCore.QRect(390, 70, 151, 41))
        font = QtGui.QFont()
        font.setFamily("华文琥珀")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.adult.setFont(font)
        self.adult.setStyleSheet("font: 20pt \"华文琥珀\";\n"
"color: rgb(54, 179, 152);")
        self.adult.setObjectName("adult")
        self.elderly = QtWidgets.QRadioButton(self.groupBox)
        self.elderly.setGeometry(QtCore.QRect(100, 70, 151, 41))
        font = QtGui.QFont()
        font.setFamily("华文琥珀")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.elderly.setFont(font)
        self.elderly.setStyleSheet("font: 20pt \"华文琥珀\";\n"
"color: rgb(54, 179, 152);")
        self.elderly.setObjectName("elderly")
        self.others = QtWidgets.QCheckBox(self.groupBox)
        self.others.setGeometry(QtCore.QRect(100, 210, 241, 51))
        font = QtGui.QFont()
        font.setFamily("华文琥珀")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.others.setFont(font)
        self.others.setStyleSheet("font: 20pt \"华文琥珀\";\n"
"color: rgb(54, 179, 152);")
        self.others.setObjectName("others")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(330, 214, 211, 41))
        self.lineEdit.setStyleSheet("font: 20pt \"华文琥珀\";")
        self.lineEdit.setText("")
        self.lineEdit.setMaxLength(18)
        self.lineEdit.setObjectName("lineEdit")
        self.dosage = QtWidgets.QCheckBox(self.groupBox)
        self.dosage.setGeometry(QtCore.QRect(100, 140, 171, 41))
        font = QtGui.QFont()
        font.setFamily("华文琥珀")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.dosage.setFont(font)
        self.dosage.setStyleSheet("font: 20pt \"华文琥珀\";\n"
"color: rgb(54, 179, 152);")
        self.dosage.setObjectName("dosage")
        self.taboo = QtWidgets.QCheckBox(self.groupBox)
        self.taboo.setGeometry(QtCore.QRect(390, 140, 171, 41))
        font = QtGui.QFont()
        font.setFamily("华文琥珀")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.taboo.setFont(font)
        self.taboo.setStyleSheet("font: 20pt \"华文琥珀\";\n"
"color: rgb(54, 179, 152);")
        self.taboo.setObjectName("taboo")
        self.shelfLife = QtWidgets.QCheckBox(self.groupBox)
        self.shelfLife.setGeometry(QtCore.QRect(260, 140, 111, 41))
        font = QtGui.QFont()
        font.setFamily("华文琥珀")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.shelfLife.setFont(font)
        self.shelfLife.setStyleSheet("font: 20pt \"华文琥珀\";\n"
"color: rgb(54, 179, 152);")
        self.shelfLife.setObjectName("shelfLife")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(147, 32, 41, 41))
        self.label_4.setStyleSheet("image: url(:/icons/icons/药品说明书.png);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(20, 20, 60, 60))
        self.label_5.setStyleSheet("image: url(:/icons/icons/AI.png);")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(80, 30, 71, 51))
        font = QtGui.QFont()
        font.setFamily("华文琥珀")
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("\n"
"font: 25pt \"华文琥珀\";\n"
"color: rgb(54, 179, 152);")
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 10, 591, 391))
        self.label.setStyleSheet("border-image: url(:/images/images/背景图片.png);\n"
"border-radius:30px")
        self.label.setText("")
        self.label.setObjectName("label")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(520, 10, 30, 41))
        self.pushButton_4.setStyleSheet("\n"
"QPushButton{\n"
"border:none;}\n"
"\n"
"QPushButton:pressed{\n"
"padding-top:5px;}")
        self.pushButton_4.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/minus-circle-fill.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon)
        self.pushButton_4.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(560, 10, 30, 41))
        self.pushButton_5.setStyleSheet("\n"
"QPushButton{\n"
"border:none;}\n"
"\n"
"QPushButton:pressed{\n"
"\n"
"padding-top:5px}\n"
"")
        self.pushButton_5.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/close-circle-fill.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_5.setIcon(icon1)
        self.pushButton_5.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_11 = QtWidgets.QLabel(Form)
        self.label_11.setGeometry(QtCore.QRect(430, 10, 61, 71))
        self.label_11.setStyleSheet("image: url(:/icons/icons/粮食监管.png);")
        self.label_11.setText("")
        self.label_11.setObjectName("label_11")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(300, 10, 91, 61))
        self.label_7.setStyleSheet("image: url(:/icons/icons/花草.png);")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(320, 70, 41, 41))
        self.label_9.setStyleSheet("image: url(:/icons/icons/花.png);")
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.OK = QtWidgets.QPushButton(Form)
        self.OK.setGeometry(QtCore.QRect(340, 40, 121, 61))
        font = QtGui.QFont()
        font.setFamily("华文琥珀")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.OK.setFont(font)
        self.OK.setStyleSheet("QPushButton{\n"
"    \n"
"    \n"
"    \n"
"    font: 20pt \"华文琥珀\";\n"
"    color: rgb(54, 179, 152);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius:20px;\n"
"    background-color: rgb(54,179,152);}\n"
"QPushButton:hover {\n"
"    \n"
"    background-color:rgb(133, 218, 201) ;\n"
"}\n"
"QPushButton:pressed {\n"
"    \n"
"    background-color: rgb(54,179,152);\n"
"}\n"
"")
        self.OK.setObjectName("OK")
        self.label.raise_()
        self.groupBox.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_2.raise_()
        self.pushButton_4.raise_()
        self.pushButton_5.raise_()
        self.label_11.raise_()
        self.label_7.raise_()
        self.label_9.raise_()
        self.OK.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox.setTitle(_translate("Form", "请勾选所需信息"))
        self.label_3.setText(_translate("Form", "单选："))
        self.label_6.setText(_translate("Form", "多选："))
        self.basic.setText(_translate("Form", "基本信息（通用）"))
        self.kid.setText(_translate("Form", "儿童"))
        self.adult.setText(_translate("Form", "成人"))
        self.elderly.setText(_translate("Form", "中老年"))
        self.others.setText(_translate("Form", "其它（可以补充）"))
        self.dosage.setText(_translate("Form", "用法用量"))
        self.taboo.setText(_translate("Form", "使用禁忌"))
        self.shelfLife.setText(_translate("Form", "保质期"))
        self.label_2.setText(_translate("Form", "智问"))
        self.OK.setText(_translate("Form", "确认"))
import OCR_res_rc
