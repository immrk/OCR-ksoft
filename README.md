## 使用说明：普通用户请直接点击右侧releases下载最终版V1.1.0压缩包即可使用；本页面教程与代码仅为支持开发爱好者编程使用
# 说明——————关于python实现ocr文本以及简单手写识别的教程以及基础代码开源

-------
> 注意：以下教程与代码均使用开源ocr功能软件tesseract-ocr（tesseract-ocr安装使用以及代码视频教程见： https://www.bilibili.com/video/BV1tK411V7Qu?spm_id_from=333.1007.top_right_bar_window_history.content.click） 以下代码与教程均要求电脑安装有python编译环境

## 准备步骤：

### 1.下载安装开源软件tesseract-ocr

当前最新windows版本下载页面(截至2022/3/24的最新版本5.1.0，若之后有更新版本请前往官网或者tesseract-ocr github页面查看，建议使用稳定版本）

tesseract-ocr官网链接：https://tesseract-ocr.github.io/docs/

tesseract-ocr官方文档：https://github.com/UB-Mannheim/tesseract/wiki



### 2.安装过程中选择安装内容勾选时需要注意选择aditional language data 中的chinese开头的语言包(用于识别中文语言)

### 3.准备python 虚拟环境：（用于防止不同项目使用的包之间的冲突）

```shell
pip install virtualenv
virtualenv venv [path]
#你的虚拟环境路径\venv\Scrips\activate 例如：C:\Users\keyajian\venv\Scripts\activate    #进入虚拟环境
#退出python虚拟环境：
```

## 机器学习训练：

### 方法一：直接下载训练好的库(可能正确率不高)

官方训练数据下载(无手写数据)https://github.com/tesseract-ocr/tessdata
本人自制简易手写数据见代码库num.traineddata，将其放入tesseract-ocr安装目录tessdata文件夹内即可

### 方法二：自己进行机器学习，识别手写(需要大量机器训练，并进行人工标注才能提升正确率)

#### 1.下载安装jTessBoxEditorFX软件(该软件需要预先安装好java运行环境，若无法打开可自行google或百度安装方法)进行自己的训练数据创建。中文教程见：https://blog.csdn.net/qq_40147863/article/details/82290015
#### 2.合并训练好的库教程https://www.cnblogs.com/c2soft/articles/10415236.html
-------
### Python代码部分 注意：
需要预先安装两个库Pillow与pytesseract

```shell
pip install Pillow
pip install pytesseract
```

代码见demo.py与ocr.py(demo为本地测试文件，ocr为包括前端的代码）
tesseract-ocr安装使用以及代码视频教程见：
https://www.bilibili.com/video/BV1tK411V7Qu?spm_id_from=333.1007.top_right_bar_window_history.content.click
注意：本项目代码部分基于该视频博主代码改造。此视频教程不包含手写识别教程，手写识别数据库为本人训练制作
### 关于code\handwriting\中jpg/tif图片的说明：
该部分图片是本人进行机器学习过程中使用的图片，若各位想要进行自己的机器学习，图片格式需要先转码为tif/tiff格式才能在jTessBoxEditorFX中使用
