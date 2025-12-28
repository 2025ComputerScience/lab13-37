import pytesseract
from PIL import Image
import cv2
import pytesseract
from PIL import Image

image_path = "/home/group37/group37_Lab13/plus.png"
# 開啟圖片
image = Image.open(image_path)

text = pytesseract.image_to_string(image, lang='eng+chi_tra', config=r'--psm 11')

print("OCR 辨識結果:")
print("-" * 40)
print(text)