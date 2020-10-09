import pytesseract
import sys

pytesseract.pytesseract.tesseract_cmd=r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def  img_to_text(img):
    read=pytesseract.image_to_string(img)
    with open('text1.txt','w') as f:
        f.write(read)

img_to_text('101941112_2653908791554923_1367787215766933386_n.jpg')

   

