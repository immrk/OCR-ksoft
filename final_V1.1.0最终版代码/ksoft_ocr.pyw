#  前端


from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import os
import webbrowser
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QInputDialog, QFileDialog
from aip import AipOcr
from PIL import Image
import pytesseract as pt
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import threading
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import QGraphicsPixmapItem, QGraphicsScene


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 1000)
        MainWindow.setMinimumSize(QtCore.QSize(600, 600))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ksoft.ico"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setObjectName("graphicsView")
        self.gridLayout.addWidget(self.graphicsView, 3, 6, 2, 5)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setStyleSheet("font: 11pt \"Adobe Arabic\";")
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 11)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setStyleSheet("font: 14pt \"Adobe Arabic\";")
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)
        self.text_baidu = QtWidgets.QPushButton(self.centralwidget)
        self.text_baidu.setStyleSheet("font: 11pt \"Adobe Arabic\";")
        self.text_baidu.setObjectName("text_baidu")
        self.gridLayout.addWidget(self.text_baidu, 9, 0, 1, 1)
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setMinimumSize(QtCore.QSize(0, 230))
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout.addWidget(self.textBrowser, 7, 0, 1, 11)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 10, 7, 1, 4)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setStyleSheet("font: 11pt \"Adobe Arabic\";")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 8, 1, 1, 1)
        self.text_ksoft = QtWidgets.QPushButton(self.centralwidget)
        self.text_ksoft.setStyleSheet("font: 11pt \"Adobe Arabic\";")
        self.text_ksoft.setObjectName("text_ksoft")
        self.gridLayout.addWidget(self.text_ksoft, 9, 5, 1, 1)
        self.handwriting_ksoft = QtWidgets.QPushButton(self.centralwidget)
        self.handwriting_ksoft.setStyleSheet("font: 11pt \"Adobe Arabic\";")
        self.handwriting_ksoft.setObjectName("handwriting_ksoft")
        self.gridLayout.addWidget(self.handwriting_ksoft, 9, 6, 1, 2)
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.gridLayout.addWidget(self.line_4, 1, 0, 1, 11)
        self.link = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.link.setObjectName("link")
        self.gridLayout.addWidget(self.link, 5, 6, 1, 5)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 8, 4, 2, 1)
        self.imagechoose = QtWidgets.QPushButton(self.centralwidget)
        self.imagechoose.setStyleSheet("font: 11pt \"Adobe Arabic\";")
        self.imagechoose.setObjectName("imagechoose")
        self.gridLayout.addWidget(self.imagechoose, 0, 10, 1, 1)
        self.appid = QtWidgets.QLineEdit(self.centralwidget)
        self.appid.setText("")
        self.appid.setObjectName("appid")
        self.gridLayout.addWidget(self.appid, 3, 1, 1, 5)
        self.handwriting_baidu = QtWidgets.QPushButton(self.centralwidget)
        self.handwriting_baidu.setStyleSheet("font: 11pt \"Adobe Arabic\";")
        self.handwriting_baidu.setObjectName("handwriting_baidu")
        self.gridLayout.addWidget(self.handwriting_baidu, 9, 1, 1, 2)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 8, 3, 2, 1)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setStyleSheet("font: 14pt \"Adobe Arabic\";")
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setStyleSheet("font: 11pt \"Adobe Arabic\";")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 8, 5, 1, 2)
        self.secretkey = QtWidgets.QTextEdit(self.centralwidget)
        self.secretkey.setMaximumSize(QtCore.QSize(16777215, 148))
        self.secretkey.setObjectName("secretkey")
        self.gridLayout.addWidget(self.secretkey, 5, 1, 1, 5)
        self.apikey = QtWidgets.QTextEdit(self.centralwidget)
        self.apikey.setMaximumSize(QtCore.QSize(16777215, 126))
        self.apikey.setObjectName("apikey")
        self.gridLayout.addWidget(self.apikey, 4, 1, 1, 5)
        self.clearall = QtWidgets.QPushButton(self.centralwidget)
        self.clearall.setStyleSheet("font: 11pt \"Adobe Arabic\";")
        self.clearall.setObjectName("clearall")
        self.gridLayout.addWidget(self.clearall, 9, 9, 1, 2)
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout.addWidget(self.line_3, 8, 8, 2, 1)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setStyleSheet("font: 11pt \"Adobe Arabic\";")
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 6, 0, 1, 2)
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setMinimumSize(QtCore.QSize(550, 0))
        self.textBrowser_2.setMaximumSize(QtCore.QSize(16777215, 20))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.gridLayout.addWidget(self.textBrowser_2, 0, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setStyleSheet("font: 14pt \"Adobe Arabic\";")
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.savebutton = QtWidgets.QPushButton(self.centralwidget)
        self.savebutton.setObjectName("savebutton")
        self.gridLayout.addWidget(self.savebutton, 6, 2, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 6, 5, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.clearall.released.connect(self.textBrowser.clear)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "KSOFT-OCR"))
        self.label_3.setText(_translate(
            "MainWindow", "使用百度云智能API识别需要填写以下信息，使用本地算法识别请忽略："))
        self.label_6.setText(_translate("MainWindow", "SECRET_KEY："))
        self.text_baidu.setText(_translate("MainWindow", "文本识别"))
        self.label_8.setText(_translate(
            "MainWindow", "使用问题请联系：keyajian@gmail.com"))
        self.label.setText(_translate("MainWindow", "百度云智能API识别"))
        self.text_ksoft.setText(_translate("MainWindow", "文本识别"))
        self.handwriting_ksoft.setText(_translate("MainWindow", "手写(数字)识别"))
        self.link.setText(_translate("MainWindow", "百度云智能API_key免费获取教程"))
        self.imagechoose.setText(_translate("MainWindow", "选择图片"))
        self.handwriting_baidu.setText(_translate("MainWindow", "手写识别"))
        self.label_5.setText(_translate("MainWindow", "API_KEY："))
        self.label_2.setText(_translate("MainWindow", "本地算法识别"))
        self.clearall.setText(_translate("MainWindow", "清空文本"))
        self.label_7.setText(_translate("MainWindow", "文本信息："))
        self.label_4.setText(_translate("MainWindow", "AppID："))
        self.savebutton.setText(_translate("MainWindow", "确定保存"))
        self.pushButton_2.setText(_translate("MainWindow", "自动填充"))
        #  各个按钮与函数关系建立，并命名函数
        self.imagechoose.released.connect(self.imagechoose1)
        self.link.released.connect(self.link1)
        self.text_baidu.released.connect(self.text_baidu1)
        self.handwriting_baidu.released.connect(self.handwriting_baidu1)
        self.text_ksoft.released.connect(self.text_ksoft1)
        self.handwriting_ksoft.released.connect(self.handwriting_ksoft1)
        self.savebutton.released.connect(self.remember1)
        self.pushButton_2.released.connect(self.autoset1)

    #  主要功能：函数定义部分，也是核心功能代码部分
    # 保存API信息

    def remember1(self):
        settings = QSettings("config.ini", QSettings.IniFormat)  # 方法1：使用配置文件
        settings.setValue("AppID", self.appid.text())
        settings.setValue("apikey", self.apikey.toPlainText())
        settings.setValue("secretkey", self.secretkey.toPlainText())

    # 输入API信息

    def autoset1(self):
        try:
            settings = QSettings(
                "config.ini", QSettings.IniFormat)  # 方法1：使用配置文件
            the_AppID = settings.value("AppID")
            the_apikey = settings.value("apikey")
            the_secretkey = settings.value("secretkey")
            self.appid.setText(the_AppID)
            self.apikey.setText(the_apikey)
            self.secretkey.setText(the_secretkey)
        except Exception as e:
            self.textBrowser.setText(
                "错误代码"+str(e)+"请确认之前保存过信息或者config.ini文件是否被你删除，如果是请重新保存")

    #  选取文件功能

    def imagechoose1(self):
        fileName, fileType = QtWidgets.QFileDialog.getOpenFileName(None, "选取文件", os.getcwd(),
                                                                   "All Files(*);;Text Files(*.txt)")
        self.textBrowser_2.setText(fileName)
        try:
            frame = QImage(self.textBrowser_2.toPlainText())
            pix = QPixmap.fromImage(frame)
            item = QGraphicsPixmapItem(pix)
            scene = QGraphicsScene()
            scene.addItem(item)
            self.graphicsView.setScene(scene)
        except Exception as e:
            self.textBrowser.setText("错误代码"+str(e)+"图片错误")

    def link1(self):
        webbrowser.open(
            "https://docs.qq.com/doc/p/7e87eed9e4419bb45eef990c9ff23dc0ae8802f7?dver=2.1.27455847", new=0, autoraise=True)

    def text_baidu1(self):
        try:
            """ 你的 APPID AK SK """
            APP_ID = self.appid.text()
            API_KEY = self.apikey.toPlainText()
            SECRET_KEY = self.secretkey.toPlainText()

            client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

            """ 读取文件 """

            def get_file_content(filePath):
                with open(filePath, "rb") as fp:
                    return fp.read()

            image = get_file_content(self.textBrowser_2.toPlainText())

            #  调用通用文字识别（高精度版）
            res_image = client.basicAccurate(image)

            #  如果有可选参数
            options = {}
            options["detect_direction"] = "true"
            options["probability"] = "true"
            res_image = client.basicAccurate(image, options)

            #  结果输出
            result = res_image['words_result']
            wordss = []
            for i in result:
                word = i['words']
                wordss.append(word)
                self.textBrowser.setText(str(wordss))
        except Exception as e:
            self.textBrowser.setText(
                "运行发生了错误，错误代码为："+str(e)+"\n若错误代码为No such file or directory: ''请检查文件路径是否选择正确\
                \n若错误代码为words_results请检查如下内容：\
                \n1.请检查文件格式是否为图片\
                \n2.请确认正确输入了上方APIid三个信息框\
                \n3.请确认您的百度智能云账号已经领取了教程中提到的两个资源\
                \n4.若之前可以使用，请检查百度智能云平台是否完成实名认证，未实名认证会被限制短时间内的刷新次数无法连续识别\
                \n5.若仍然无法解决，请邮件询问keyajian@gmail.com,以OCRQA为标题并描述错误代码以及功能名称")
#  百度云API手写识别：

    def handwriting_baidu1(self):
        try:
            """ 你的 APPID AK SK """
            APP_ID = self.appid.text()
            API_KEY = self.apikey.toPlainText()
            SECRET_KEY = self.secretkey.toPlainText()

            client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

            """ 读取文件 """

            def get_file_content(filePath):
                with open(filePath, "rb") as fp:
                    return fp.read()

            image = get_file_content(self.textBrowser_2.toPlainText())

            #  调用手写文字识别
            res_image = client.handwriting(image)

            #  可选参数
            options = {}
            options["recognize_granularity"] = "true"
            options["detect_direction"] = "true"
            options["probability"] = "true"
            res_image = client.handwriting(image, options)

            #  结果输出
            result = res_image['words_result']
            for i in result:
                word = i['words']
                self.textBrowser.setText(word)
        except Exception as e:
            self.textBrowser.setText(
                "运行发生了错误，错误代码为："+str(e)+"\n若错误代码为No such file or directory: ''请检查文件路径是否选择正确\
                \n若错误代码为words_results请检查如下内容：\
                \n1.请检查文件格式是否为图片\
                \n2.请确认正确输入了上方APIid三个信息框\
                \n3.请确认您的百度智能云账号已经领取了教程中提到的两个资源\
                \n4.若之前可以使用，请检查百度智能云平台是否完成实名认证，未实名认证会被限制短时间内的刷新次数无法连续识别\
                \n5.若仍然无法解决，请邮件询问keyajian@gmail.com,以OCRQA为标题并描述错误代码以及功能名称")
#  本地文字识别：

    def text_ksoft1(self):
        try:
            pt.pytesseract.tesseract_cmd = r"tesseract_ocr\tesseract.exe"
            img = Image.open(self.textBrowser_2.toPlainText())
            text = pt.image_to_string(img, lang="chi_sim")
            self.textBrowser.setText(text)
        except Exception as e:
            self.textBrowser.setText("运行发生了错误，错误代码为："+str(e)+"\
            \n若错误代码为No such file or directory: ''或'str' object has no attribute 'read'或cannot identify image file\
            \n    请检查文件路径是否选择正确\
            \n若错误代码为tesseract_ocr\tesseract.exe is not installed or it's not in your PATH. See README file for more information.\
            \n    请检查tesseract_ocr文件夹是否与本程序在同一文件夹中\
            \n若错误代码为：Unsupported image format/type：\
            \n    请检查所选文件类型是否为图片\
            \n若仍然无法解决，请邮件询问keyajian@gmail.com,以OCRQA为标题并描述错误代码以及功能名称")
#  本地手写数字识别：

    def handwriting_ksoft1(self):
        try:
            pt.pytesseract.tesseract_cmd = r"tesseract_ocr\tesseract.exe"
            img = Image.open(self.textBrowser_2.toPlainText())
            text = pt.image_to_string(img, lang="num")
            self.textBrowser.setText(text)
        except Exception as e:
            self.textBrowser.setText("运行发生了错误，错误代码为："+str(e)+"\
            \n若错误代码为No such file or directory: ''或'str' object has no attribute 'read'或cannot identify image file\
            \n    请检查文件路径是否选择正确\
            \n若错误代码为tesseract_ocr\tesseract.exe is not installed or it's not in your PATH. See README file for more information.\
            \n    请检查tesseract_ocr文件夹是否与本程序在同一文件夹中\
            \n若错误代码为：Unsupported image format/type：\
            \n    请检查所选文件类型是否为图片\
            \n若仍然无法解决，请邮件询问keyajian@gmail.com,以OCRQA为标题并描述错误代码以及功能名称")


#  显示界面
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())  # 死循环，保证页面始终显示不退出
