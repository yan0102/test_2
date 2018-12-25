# encoding: utf-8

import json
import pickle
import re


def key_set_content(content, key_set):
    content = content.strip().lower()
    key = [i for i in key_set if i.lower() in content]
    return key[0] if key else None


def intercept_content(content, key_name):
    content_tmp = content.strip().lower()
    pattern = re.compile(r'^{}: *'.format(key_name.lower()))
    match = pattern.match(content_tmp)
    result_content = content[match.end():] if match else None
    return result_content


def fill_form(DL, image_name, path='ocr_form_filed.pkl'):
    with open(path, 'rb') as f:
        key_set, table_filed_name = pickle.load(f)
    DL_stored = sorted(DL, key=lambda x: (x[2], x[1]))
    result = dict()
    for i, D in enumerate(DL_stored):
        key_name = key_set_content(D[0], key_set)
        if key_name:
            result_key = table_filed_name.get(key_name, None)
            result_content = intercept_content(D[0], key_name)
            result_position = list(map(int, D[1:])) if result_content else ''
            if not result_content:
                # similar y-value items in the list;Allow 3 pixel deviations
                similar_y = [i for i in DL_stored if i[2] in range((D[2] - 3), (D[2] + 3)) and i[1] > D[1]]
                # The nearest one on the right
                right = sorted(similar_y, key=lambda x: x[1])[0] if similar_y else None
                if right and not key_set_content(right[0], key_set) and result_key:
                    result_content = right[0]
                    result_position = list(map(int, right[1:]))
                else:
                    below_list = [i for i in DL_stored[(i + 1):] if i[2] > D[2]]
                    # The nearest one on the below
                    below = sorted(below_list, key=lambda x: x[2])[0]
                    if not key_set_content(below[0], key_set) and result_key:
                        result_content = below[0]
                        result_position = list(map(int, below[1:]))

            result[result_key] = {'name': key_name,
                                  'content': result_content,
                                  'position': result_position}

    return {image_name: result}


if __name__ == '__main__':
        DL = [['Report output', 42, 42, 17, 151],
              ['P828 2 of Z', 908, 45, 16, 125],
              ['soId-To»rarcy', 134, 158, 15, 136],
              ['yumua 1cwv.,nangn~.x mane:omminq 401131, (a R. Chum', 620, 174, 32, 273],
              ['Ans ASIA PACIFIC LIMITED', 132, 206, 14, 240],
              ['Tel:«as‘zlem so we', 657, 223, 14, 211],
              ["Uns: 1617'1619. 15K, Town 3", 133, 237, 15, 273],
              ['ms-zl-zan Em 5-39', 647, 255, 14, 212],
              ['wwwnrs .NET', 672, 271, 14, 119],
              ['33 Canton Road', 136, 286, 13, 141],
              ['Tsim 5m', 135, 304, 12, 91],
              ['rm ,90012911105. 08 ZOJEPaga 21/ \\2 M. _ Our ref', 415, 306, 38, 511],
              ['- HONG KONG', 137, 318, 14, 116],
              ['HONG KONG', 133, 334, 15, 102],
              ['Weight (gross/net)', 140, 350, 14, 177],
              ['235.300 KG', 596, 366, 15, 108],
              ['319.000 KG', 316, 367, 14, 107],
              ['Gross weight', 141, 368, 13, 134],
              ['Net weight', 441, 369, 12, 116],
              ['Colli: 3', 140, 382, 14, 93],
              ['Country of Delivery: CN', 141, 399, 15, 222]]

        # path = 'ocr_form_filed.xlsx'
        result = fill_form(DL, 'test')
        result_json = json.dumps(result)
        print(result_json)
