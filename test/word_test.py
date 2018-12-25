# -*- coding:utf-8 -*-

import cv2 as cv
import pytesseract
import numpy as np

def image_word_demo():
    image = cv.imread('../test_data/E_frameweb.png')
    print(image.shape)
    #pytesseract.pytesseract.tesseract_cmd = 'E://Program Files/Tesseract-OCR/tesseract.exe'
    text = pytesseract.image_to_string(image, lang='chi_sim')
    
    print(text)
    #cv.imshow('image', image)
    #cv.waitKey(0)
    #cv.destroyAllWindows()

  
def fill_form(DL, key_set):
    DL_stored = sorted(DL, key=lambda x: (x[2], x[1]))
    #print(DL_stored)
    form_list = []
    result = dict()
    for i, D in enumerate(DL_stored):
        content = D[0].strip().split('：')
        if content[0] in key_set:
            similar_y = [i for i in DL_stored[(i+1):] if i[2] == D[2]]# similar y-value items in the list
            right_content = sorted(similar_y, key=lambda x: x[1])[0][0]
            if right_content.strip().split(':') not in  key_set:
                result[content[0]] = right_content
            else:
                below_list = [i for i in DL_stored[(i+1):] if i[2] > D[2]]
                below_content = sorted(below_list, key=lambda x: x[2])[0][0]
                if below_content.strip().split(':') not in  key_set:
                    result[content[0]] = below_content 
            
    return result
    

if __name__ == '__main__':
    DL = [('$75,000.00',495,577,116,15),('合计金额（美元）：柒万伍仟元整',143,575,240,16),
('D2 laleli Istanbul Turkey',58,358,200,14),('2)8504409999',472,341,123,13),
('地址：',32,339,30,18),('Kemal pasa mah. Gengturk cad. No 32 Burak Apt.',62,339,300,18),
('买方：',32,323,30,15),('Sidra Kagitgilik San Ic ve Dis Tic Ltd Sti',62,323,300,15),
('海关编码：',410,321,70,15),('1)8517623300',480,321,90,15),
('地址：',32,303,50,17),('AZ4921, SaatLt rayonu, Heyder aliyev, ev D-6',62,303,300,17),
('发票号码：',410,286,70,15),('18KZ0719-A-00',480,286,100,15),
('收货方：',32,286,50,16),('OPTIK FIBER MMC VOEN:6701051671',75,286,300,16),
('发票日期：',395,268,80,15),('July.19.2018',475,268,100,15),
('合同号：',32,268,50,15),('ATR-DB-S112',80,268,100,15),('发 票',6,237,633,15),
('电话：',32,147,30,16),('(755)3363 9088',62,147,95,16),('传真：',157,147,40,16),('(755)3363 1919',197,147,100,16),
('深圳市南山区科技园高新南一道创维大厦C座1601室',30,126,313,16),('宽兆科技（深圳）有限公司',30,106,191,16)]
    
    key_set = ('地址', '买方', '海关编码', '收货方', '合同号', '传真', '电话', '发票日期', '发票号码')
    result = fill_form(DL, key_set)
    print(result)
    
