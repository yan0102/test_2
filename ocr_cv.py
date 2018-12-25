#!/usr/bin/env python
# -*- coding:utf-8 -*-

import cv2
import matplotlib.pyplot as plt
import numpy as np
import pytesseract
import os

image_path = 'test_data/test.png'
img = cv2.imread(image_path)
# img = cv2.fastNlMeansDenoisingColored(img, None, 10, 3, 3, 3)
# convert to gray image
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# edge binary
sobel = cv2.Sobel(img_gray, cv2.CV_8U, 1, 0, ksize=3)
ret, binary = cv2.threshold(sobel, 40, 255, cv2.THRESH_OTSU+cv2.THRESH_BINARY)


element1 = cv2.getStructuringElement(cv2.MORPH_RECT, (23, 5))
element2 = cv2.getStructuringElement(cv2.MORPH_RECT, (20, 3))

dilation1 = cv2.dilate(binary, element2, iterations=1)
erosion = cv2.erode(dilation1, element1, iterations=1)

dilation2 = cv2.dilate(erosion, element2, iterations=3)


# text region
region = []
img2, contours, hierarchy = cv2.findContours(dilation2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
for cont in contours:
	area = cv2.contourArea(cont)
	if area < 800:
		continue
	rect = cv2.minAreaRect(cont)

	# box to store a single text rectangle
	box = cv2.boxPoints(rect)
	box = np.int0(box)

	height = abs(box[0][1] - box[2][1])
	width = abs(box[0][0] - box[2][0])

	if height > width*1.3:
		continue

	region.append(box)

for box in region:
	# Xs = [i[0] for i in box]
	# Ys = [i[1] for i in box]
	# x1 = min(Xs)
	# x2 = max(Xs)
	# y1 = min(Ys)
	# y2 = max(Ys)
	# hight = y2 - y1
	# width = x2 - x1
	# tmp_img= img_gray[y1:y1+hight, x1:x1+width]
	# tmp_content = pytesseract.image_to_string(tmp_img, lang='chi_sim')
	# tmp_content = tmp_content.strip()
	# tmp_content = tmp_content.replace('\n', '')
	# if len(tmp_content) > 0:
	# 	print(tmp_content)
	cv2.drawContours(img, [box], 0, (0,255,0), 2)


plt.imshow(img, 'brg')
plt.show()
