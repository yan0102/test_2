#!/usr/bin/env python
# -*- coding:utf-8 -*-

# https://blog.csdn.net/it2153534/article/details/79185397

import cv2
import numpy as np
import pytesseract
import os
import PIL
import image_deal_test


image_path = '../test_data/E_frameweb.png'
img = cv2.imread(image_path)
img = image_deal.image_correction(img)
# img = cv2.fastNlMeansDenoisingColored(img, None, 10, 3, 3, 3)
# convert to gray image
# 转换成灰度图
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# edge binary abs# 边缘检测
sobel = cv2.Sobel(img_gray, cv2.CV_8U, 1, 0, ksize=3)
# 二值化
ret, binary = cv2.threshold(sobel, 40, 255, cv2.THRESH_OTSU + cv2.THRESH_BINARY)

# 设置腐蚀的核函数
element1 = cv2.getStructuringElement(cv2.MORPH_RECT, (23, 5))
# 设置膨胀的核函数
element2 = cv2.getStructuringElement(cv2.MORPH_RECT, (20, 3))
# 膨胀一次，让轮廓突出
dilation1 = cv2.dilate(binary, element2, iterations=1)
# 腐蚀一次，去掉细节，如表格线等。注意这里去掉的是竖直的线
erosion = cv2.erode(dilation1, element1, iterations=1)
# 再次膨胀，让轮廓明显一些
dilation2 = cv2.dilate(erosion, element2, iterations=3)


# text region
region = []
img2, contours, hierarchy = cv2.findContours(dilation2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# 查找轮廓,contours:轮廓本身，hierarchy：轮廓对应的属性
# 每个轮廓contours[i]对应4个hierarchy元素hierarchy[i][0] ~hierarchy[i][3]，分别表示后一个轮廓、前一个轮廓、父轮廓、内嵌轮廓的索引编号，如果没有对应项，则该值为负数。
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

	if height > width * 1.3:
		continue

	region.append(box)

for box in region:
	cv2.drawContours(img, [box], 0, (0,0,255), 2)

	x1 = min(box[:, 0])
	x2 = max(box[:, 0])
	y1 = min(box[:, 1])
	y2 = max(box[:, 1])
	tmp_img = img[y1:y2, x1:x2]
	print(x1, y1, x2 - x1, y2 - y1)
	# print(box)
	cv2.imshow('tmp_img', tmp_img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()



# print(region_text)
cv2.imshow('brg', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
