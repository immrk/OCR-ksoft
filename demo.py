import pytesseract as pt
from PIL import Image


path = r"D:\tesseract_ocr\tesseract.exe"  # 输入你的tesseract.exe文件路径

pt.pytesseract.tesseract_cmd = path

img = Image.open("test/1.jpg")  # 打开图片

text = pt.image_to_string(img, lang="num")  # lang="chi_sim"表示语言为简体中文

print(text)
