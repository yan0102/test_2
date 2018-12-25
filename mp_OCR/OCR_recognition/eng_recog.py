#!/usr/bin/env python
import sys
sys.path.append('../')
import pytesseract
import json
from OCR_detection import ocr_cv
from OCR_table_filling import ocr_form


# from region detected, recognize its content
# this can work on english images, but not good enough
def box2word(image, region):
    result = []
    for box in region:
        Xs = [i[0] for i in box]
        Ys = [i[1] for i in box]
        x1 = min(Xs)
        x2 = max(Xs)
        y1 = min(Ys)
        y2 = max(Ys)
        hight = y2 - y1
        width = x2 - x1
        tmp = [x1, y1, hight, width]
        tmp_img = image[y1:y1 + hight, x1:x1 + width]
        # pytesseract does not work on chinese characters very well
        # tmp_content = pytesseract.image_to_string(tmp_img, lang='chi_sim')
        tmp_content = pytesseract.image_to_string(tmp_img)
        tmp_content = tmp_content.strip()
        tmp_content = tmp_content.replace('\n', '')
        if len(tmp_content) > 0:
            tmp.insert(0, tmp_content)
            result.append(tmp)

    return result


if __name__ == '__main__':
    image_path = './english_test.png'
    region, image = ocr_cv.detect_word(image_path)
    # print(len(region))
    result = box2word(image, region)
    # print(result)
    form_filed_path = '../OCR_table_filling/ocr_form_filed.pkl'
    form_result = ocr_form.fill_form(result, 'test', form_filed_path)
    result_json = json.dumps(form_result)
    print(result_json)
