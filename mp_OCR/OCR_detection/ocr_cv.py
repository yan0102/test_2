#!/usr/bin/env python
# -*- coding:utf-8 -*-
import cv2
import matplotlib.pyplot as plt
import numpy as np


# detect where words are in a certain image
# return their region
def detect_word(image_path):
    img = cv2.imread(image_path)
    # img = cv2.fastNlMeansDenoisingColored(img, None, 10, 3, 3, 3)
    # convert to gray image
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # edge binary
    sobel = cv2.Sobel(img_gray, cv2.CV_8U, 1, 0, ksize=3)
    ret, binary = cv2.threshold(sobel, 40, 255,
                                cv2.THRESH_OTSU+cv2.THRESH_BINARY)

    element1 = cv2.getStructuringElement(cv2.MORPH_RECT, (50, 5))  # 23, 5 | 50
    element2 = cv2.getStructuringElement(cv2.MORPH_RECT, (20, 3))  # 20, 3

    dilation1 = cv2.dilate(binary, element2, iterations=1)
    erosion = cv2.erode(dilation1, element1, iterations=1)

    dilation2 = cv2.dilate(erosion, element2, iterations=3)

    # text region
    region = []
    img2, contours, hierarchy = cv2.findContours(dilation2, cv2.RETR_TREE,
                                                 cv2.CHAIN_APPROX_SIMPLE)
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

    return region, img_gray
    # draw rectangles to show detection result
    # for box in region:
    #     cv2.drawContours(img, [box], 0, (0, 255, 0), 2)

    # plt.imshow(img, 'brg')
    # plt.show()
    # cv2.imshow('brg', img)
    # cv2.waitKey()
    # cv2.destroyAllWindows()


if __name__ == '__main__':
    detect_word('test_1.png')
