import pytesseract
from PIL import Image
import cv2
import pytesseract
from PIL import Image

image_path = "/home/group37/group37_Lab13/thirty-seven.png"
# 開啟圖片
image = Image.open(image_path)

text = pytesseract.image_to_string(image, lang='chi_tra', config='--psm 10')

print("OCR 辨識結果:")
print("-" * 40)
print(text)
