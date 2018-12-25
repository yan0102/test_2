# encoding: utf-8

import cv2
import pytesseract
from PIL import Image
import matplotlib.pyplot as plt

def image_crop(Image, topX, topY, Height, Width):
    box = (topX, topY, topX + Height, topY + Width)
    region = Image.crop(box)
    print(region)
    plt.imshow(region)
    plt.show()    


# E:/Program Files/Anaconda3/Lib/site-packages/pytesseract/test.png
image = Image.open('test_data/test.png')
print(image.size)
#plt.imshow(image)
#plt.show()
#code = pytesseract.image_to_string(image, lang='chi_sim')
#print(code)
#image_crop(image, 100, 100, 400, 400)

