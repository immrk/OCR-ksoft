#  前端


from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import os
import webbrowser
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QInputDialog, QFileDialog
from aip import AipOcr
from PIL import Image
import pytesseract as pt


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 1000)
        MainWindow.setMinimumSize(QtCore.QSize(600, 600))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ksoft.ico"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.appid = QtWidgets.QLineEdit(self.centralwidget)
        self.appid.setText("")
        self.appid.setObjectName("appid")
        self.gridLayout.addWidget(self.appid, 3, 1, 1, 6)
        self.text_baidu = QtWidgets.QPushButton(self.centralwidget)
        self.text_baidu.setStyleSheet("font: 11pt \"Adobe Arabic\";")
        self.text_baidu.setObjectName("text_baidu")
        self.gridLayout.addWidget(self.text_baidu, 10, 0, 1, 2)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setStyleSheet("font: 14pt \"Adobe Arabic\";")
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setStyleSheet("font: 11pt \"Adobe Arabic\";")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 9, 7, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 9, 5, 2, 1)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setStyleSheet("font: 14pt \"Adobe Arabic\";")
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.gridLayout.addWidget(self.line_4, 1, 0, 1, 12)
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setMinimumSize(QtCore.QSize(0, 230))
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout.addWidget(self.textBrowser, 8, 0, 1, 12)
        self.link = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.link.setObjectName("link")
        self.gridLayout.addWidget(self.link, 5, 7, 1, 5)
        self.apikey = QtWidgets.QTextEdit(self.centralwidget)
        self.apikey.setMaximumSize(QtCore.QSize(16777215, 126))
        self.apikey.setObjectName("apikey")
        self.gridLayout.addWidget(self.apikey, 4, 1, 1, 6)
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.gridLayout.addWidget(self.line_5, 6, 0, 1, 12)
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout.addWidget(self.line_3, 9, 9, 2, 1)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setStyleSheet("font: 14pt \"Adobe Arabic\";")
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 9, 4, 2, 1)
        self.clearall = QtWidgets.QPushButton(self.centralwidget)
        self.clearall.setStyleSheet("font: 11pt \"Adobe Arabic\";")
        self.clearall.setObjectName("clearall")
        self.gridLayout.addWidget(self.clearall, 10, 10, 1, 2)
        self.secretkey = QtWidgets.QTextEdit(self.centralwidget)
        self.secretkey.setMaximumSize(QtCore.QSize(16777215, 148))
        self.secretkey.setObjectName("secretkey")
        self.gridLayout.addWidget(self.secretkey, 5, 1, 1, 6)
        self.handwriting_ksoft = QtWidgets.QPushButton(self.centralwidget)
        self.handwriting_ksoft.setStyleSheet("font: 11pt \"Adobe Arabic\";")
        self.handwriting_ksoft.setObjectName("handwriting_ksoft")
        self.gridLayout.addWidget(self.handwriting_ksoft, 10, 7, 1, 2)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setStyleSheet("font: 11pt \"Adobe Arabic\";")
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 12)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 11, 8, 1, 4)
        self.handwriting_baidu = QtWidgets.QPushButton(self.centralwidget)
        self.handwriting_baidu.setStyleSheet("font: 11pt \"Adobe Arabic\";")
        self.handwriting_baidu.setObjectName("handwriting_baidu")
        self.gridLayout.addWidget(self.handwriting_baidu, 10, 2, 1, 2)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setStyleSheet("font: 11pt \"Adobe Arabic\";")
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 7, 0, 1, 2)
        self.imagechoose = QtWidgets.QPushButton(self.centralwidget)
        self.imagechoose.setStyleSheet("font: 11pt \"Adobe Arabic\";")
        self.imagechoose.setObjectName("imagechoose")
        self.gridLayout.addWidget(self.imagechoose, 0, 11, 1, 1)
        self.text_ksoft = QtWidgets.QPushButton(self.centralwidget)
        self.text_ksoft.setStyleSheet("font: 11pt \"Adobe Arabic\";")
        self.text_ksoft.setObjectName("text_ksoft")
        self.gridLayout.addWidget(self.text_ksoft, 10, 6, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setStyleSheet("font: 11pt \"Adobe Arabic\";")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 9, 1, 1, 2)
        self.path = QtWidgets.QTextBrowser(self.centralwidget)
        self.path.setMinimumSize(QtCore.QSize(550, 35))
        self.path.setMaximumSize(QtCore.QSize(16777215, 20))
        self.path.setObjectName("path")
        self.gridLayout.addWidget(self.path, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.clearall.released.connect(self.textBrowser.clear)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "KSOFT-OCR文本识别工具"))
        self.text_baidu.setText(_translate("MainWindow", "文本识别"))
        self.label_4.setText(_translate("MainWindow", "AppID："))
        self.label_2.setText(_translate("MainWindow", "本地算法识别"))
        self.label_5.setText(_translate("MainWindow", "API_KEY："))
        self.link.setText(_translate("MainWindow", "百度云智能API_key免费获取教程"))
        self.label_6.setText(_translate("MainWindow", "SECRET_KEY："))
        self.clearall.setText(_translate("MainWindow", "清空文本"))
        self.handwriting_ksoft.setText(_translate("MainWindow", "手写(数字)识别"))
        self.label_3.setText(_translate(
            "MainWindow", "使用百度云智能API识别需要填写以下信息，使用本地算法识别请忽略："))
        self.label_8.setText(_translate(
            "MainWindow", "使用问题请联系：keyajian@gmail.com"))
        self.handwriting_baidu.setText(_translate("MainWindow", "手写识别"))
        self.label_7.setText(_translate("MainWindow", "文本信息："))
        self.imagechoose.setText(_translate("MainWindow", "选择图片"))
        self.text_ksoft.setText(_translate("MainWindow", "文本识别"))
        self.label.setText(_translate("MainWindow", "百度云智能API识别"))
        #  各个按钮与函数关系建立，并命名函数
        self.imagechoose.released.connect(self.imagechoose1)
        self.link.released.connect(self.link1)
        self.text_baidu.released.connect(self.text_baidu1)
        self.handwriting_baidu.released.connect(self.handwriting_baidu1)
        self.text_ksoft.released.connect(self.text_ksoft1)
        self.handwriting_ksoft.released.connect(self.handwriting_ksoft1)

    #  主要功能：函数定义部分，也是核心功能代码部分
    #  选取文件功能
    def imagechoose1(self):
        fileName, fileType = QtWidgets.QFileDialog.getOpenFileName(None, "选取文件", os.getcwd(),
                                                                   "All Files(*);;Text Files(*.txt)")
        self.path.setText(fileName)

    def link1(self):
        webbrowser.open(
            "https://docs.qq.com/doc/p/7e87eed9e4419bb45eef990c9ff23dc0ae8802f7?dver=2.1.27455847", new=0, autoraise=True)

    def text_baidu1(self):
        """ 你的 APPID AK SK """
        APP_ID = self.appid.text()
        API_KEY = self.apikey.toPlainText()
        SECRET_KEY = self.secretkey.toPlainText()

        client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

        """ 读取文件 """

        def get_file_content(filePath):
            with open(filePath, "rb") as fp:
                return fp.read()

        image = get_file_content(self.path.toPlainText())

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
#  百度云API手写识别：

    def handwriting_baidu1(self):
        """ 你的 APPID AK SK """
        APP_ID = self.appid.text()
        API_KEY = self.apikey.toPlainText()
        SECRET_KEY = self.secretkey.toPlainText()

        client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

        """ 读取文件 """

        def get_file_content(filePath):
            with open(filePath, "rb") as fp:
                return fp.read()

        image = get_file_content(self.path.toPlainText())

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
#  本地文字识别：

    def text_ksoft1(self):
        pt.pytesseract.tesseract_cmd = r"tesseract_ocr\tesseract.exe"
        img = Image.open(self.path.toPlainText())
        text = pt.image_to_string(img, lang="chi_sim")
        self.textBrowser.setText(text)
#  本地手写数字识别：

    def handwriting_ksoft1(self):
        pt.pytesseract.tesseract_cmd = r"tesseract_ocr\tesseract.exe"
        img = Image.open(self.path.toPlainText())
        text = pt.image_to_string(img, lang="num")
        self.textBrowser.setText(text)


#  显示界面
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())  # 死循环，保证页面始终显示不退出
