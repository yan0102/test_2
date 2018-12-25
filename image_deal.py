# encoding: utf-8

import numpy as np
import cv2
import json
import argparse

parser = argparse.ArgumentParser(description='ll')
parser.add_argument('--test_type', default='corr_crop')
args = parser.parse_args()


def image_crop(Image, topX, topY, Width, Height):
    region = Image[topY:topY + Height, topX:topX + Width]
    return region


def image_correction(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
    coords = np.column_stack(np.where(thresh > 0))
    angle = cv2.minAreaRect(coords)[-1]
    # print(angle)
    angle = -(90 + angle) if angle < -45 else -angle
    print(angle)
    h, w = image.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(image, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
    return rotated


def fill_form(DL, key_set):
    DL_stored = sorted(DL, key=lambda x: (x[2], x[1]))
    # print(DL_stored)
    result = dict()
    for i, D in enumerate(DL_stored):
        content = D[0].strip().split('：')
        if content[0] in key_set:
            # similar y-value items in the list
            similar_y = [i for i in DL_stored[(i + 1):] if i[2] == D[2]]
            right = sorted(similar_y, key=lambda x: x[1])[0]
            if right[0].strip().split(':') not in key_set:
                result[content[0]] = {'content': right[0], 'position': right[1:]}
            else:
                below_list = [i for i in DL_stored[(i + 1):] if i[2] > D[2]]
                below = sorted(below_list, key=lambda x: x[2])[0]
                if below[0].strip().split(':') not in key_set:
                    result[content[0]] = {'content': below[0], 'position': below[1:]}

    return result


if __name__ == '__main__':
    if args.test_type == 'corr_crop':
        file_name = 'test_data/corr_test_6.jpg'
        image = cv2.imread(file_name)
        # 图片校正
        rotated = image_correction(image)
        cv2.imshow('rotated', rotated)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        # 提取表格
        region = image_crop(rotated, 25, 385, 590, 220)
        cv2.imshow('region', region)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        DL = [('$75, 000.00', 495, 577, 116, 15),
              ('合计金额（美元）：柒万伍仟元整', 143, 575, 240, 16),
              ('D2 laleli Istanbul Turkey', 58, 358, 200, 14),
              ('2)8504409999', 472, 341, 123, 13),
              ('地址：', 32, 339, 30, 18),
              ('Kemal pasa mah. Gengturk cad. No 32 Burak Apt.', 62, 339, 300, 18),
              ('买方：', 32, 323, 30, 15),
              ('Sidra Kagitgilik San Ic ve Dis Tic Ltd Sti', 62, 323, 300, 15),
              ('海关编码：', 410, 321, 70, 15), ('1)8517623300', 480, 321, 90, 15),
              ('地址：', 32, 303, 50, 17),
              ('AZ4921,  SaatLt rayonu,  Heyder aliyev,  ev D-6', 62, 303, 300, 17),
              ('发票号码：', 410, 286, 70, 15), ('18KZ0719-A-00', 480, 286, 100, 15),
              ('收货方：', 32, 286, 50, 16),
              ('OPTIK FIBER MMC VOEN:6701051671', 75, 286, 300, 16),
              ('发票日期：', 395, 268, 80, 15),
              ('July.19.2018', 475, 268, 100, 15),
              ('合同号：', 32, 268, 50, 15),
              ('ATR-DB-S112', 80, 268, 100, 15), ('发 票', 6, 237, 633, 15),
              ('电话：', 32, 147, 30, 16), ('(755)3363 9088', 62, 147, 95, 16),
              ('传真：', 157, 147, 40, 16),
              ('(755)3363 1919', 197, 147, 100, 16),
              ('深圳市南山区科技园高新南一道创维大厦C座1601室', 30, 126, 313, 16),
              ('宽兆科技（深圳）有限公司', 30, 106, 191, 16)]

        key_set = ('地址', '买方', '海关编码', '收货方', '合同号', '传真', '电话', '发票日期', '发票号码')
        result = fill_form(DL, key_set)
        result_json = json.dumps(result)
        print(result_json)
