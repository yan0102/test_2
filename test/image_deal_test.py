# encoding: utf-8

import cv2
from PIL import Image
import matplotlib.pyplot as plt

import math
import random
import numpy as np
from scipy import misc, ndimage


def image_crop(Image, topX, topY, Width, Height):
    #box = (topX, topY, topX + Width, topY + Height)
    #region = Image.crop(box)
    region = Image[topY:topY+Height, topX:topX+Width]
    print(region.shape)
    return region
    
  
def image_correction(Image):    
    gray = cv2.cvtColor(Image,cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5,5),0)
    edges = cv2.Canny(blurred,50,150)
    lines = cv2.HoughLines(edges,1,np.pi/180,0)
    print(lines.shape)
    rotate_angle= 0
    for rho,theta in lines[0]:
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a*rho
        y0 = b*rho
        x1 = int(x0 + 1000*(-b))
        y1 = int(y0 + 1000*(a))
        x2 = int(x0 - 1000*(-b))
        y2 = int(y0 - 1000*(a))
        #cv2.line(Image, (x1, y1), (x2, y2), (0, 0, 255), 1)
        if x1 == x2 or y1 == y2:
            continue
        t = float(y2-y1)/(x2-x1)
        rotate_angle = math.degrees(math.atan(t))
        if rotate_angle > 45:
            rotate_angle = -90 + rotate_angle
        elif rotate_angle < -45:
            rotate_angle = 90 + rotate_angle
    rotate_img = ndimage.rotate(Image, rotate_angle)
    plt.imshow(rotate_img)
    plt.show()      
    
def image_correction_1(image):
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY) # 图像变灰
    ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV|cv2.THRESH_OTSU) # 二值化处理，像素取反，变成白字黑底
    # 计算包含了背旋转文本的最小边框
    coords = np.column_stack(np.where(thresh > 0))
    angle = cv2.minAreaRect(coords)[-1]# 给出包含整个文字区域的矩形边框， 这个边框的旋转角度和图中文本的旋转角度一直
    print(angle)
    angle = -(90 + angle) if angle < -45 else -angle # 调整角度，角度小于-45，在原来的角度上增加90度，角度大于-45，直接对角度反转
    print(angle)
    # 执行放射变换
    h, w = image.shape[:2]
    center = (w//2, h//2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(image, M, (w, h), flags = cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
    #cv2.putText(rotated, 'Angle:{:.2f} degress'.format(angle), (10,30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
    #plt.imshow(rotated)
    #plt.show()
    return rotated
    
def image_correctioin_2(image):
    img = cv2.GaussianBlur(image,(3,3),0)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray,50,250,apertureSize = 3)
    lines = cv2.HoughLinesP(edges,1,np.pi/180,50,minLineLength=90,maxLineGap=10)
    for x1,y1,x2,y2 in lines[0]:
        cv2.line(result1,(x1,y1),(x2,y2),(0,0,255),1) 
    cv2.circle(result2,(207,151),2,(0,255,0),2)
    cv2.circle(result2,(517,285),2,(0,255,0),2)
    cv2.circle(result2,(17,601),2,(0,255,0),2)
    cv2.circle(result2,(343,731),2,(0,255,0),2)
           
    cv2.imshow('edges', edges)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
if __name__ == '__main__':
    file_name = '../test_data/corr_test_4.png'
    image = cv2.imread(file_name)
    rotated = image_correctioin_1(image)
    #region = image_crop(rotated, 25, 385, 590, 220)
    plt.imshow(rotated)
    plt.show()
    
    #crop_file_path = 'test_data/E_frameweb.png'
    #image = cv2.imread(crop_file_path)
    #print(image.shape)    
    #region = image_crop(image, 25, 385, 590, 220)
    #plt.imshow(region)
    #plt.show()    