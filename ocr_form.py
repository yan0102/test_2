# encoding: utf-8

import json
import pandas as pd
import numpy as np


def form_key_set(path):
    key_set_df = pd.read_excel(path, header=0)
    key_set_df = key_set_df.replace(np.nan, '')
    key_set = []
    table_filed_name = {}
    for i, row in key_set_df.iterrows():
        key_set.append(row[1])
        table_filed_name[row[1]] = row[0]
        if row[2]:
            tmp_row = row[2].split('|')
            for tmp in tmp_row:
                key_set.append(tmp)
                table_filed_name[tmp] = row[0]

    return key_set, table_filed_name


def key_set_content(content, key_set):
    content = content.strip()
    key = [i for i in key_set if i in content]
    return key[0] if key else None


def fill_form(DL, key_set, table_filed_name):
    DL_stored = sorted(DL, key=lambda x: (x[2], x[1]))
    # print(DL_stored)
    result = dict()
    for i, D in enumerate(DL_stored):
        key_name = key_set_content(D[0], key_set)
        if key_name:
            result_key = table_filed_name.get(key_name, None)
            # similar y-value items in the list
            # similar_y = [i for i in DL_stored[(i + 1):] if i[2] == D[2]]
            similar_y = list(filter(lambda i: i[2] in range((D[2] - 3), (D[2] + 3)) and i[1] > D[1], DL_stored))
            # The nearest one on the right
            right = sorted(similar_y, key=lambda x: x[1])[0]
            if not key_set_content(right[0], key_set) and result_key:
                result[result_key] = {'name': key_name,
                                      'content': right[0],
                                      'position': right[1:]}
            else:
                below_list = [i for i in DL_stored[(i + 1):] if i[2] > D[2]]
                # The nearest one on the below
                below = sorted(below_list, key=lambda x: x[2])[0]
                if not key_set_content(below[0], key_set) and result_key:
                    result[result_key] = {'name': key_name,
                                          'content': below[0],
                                          'position': below[1:]}

    return result


if __name__ == '__main__':
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

        path = 'data/ocr_form_filed.xlsx'
        key_set, table_filed_name = form_key_set(path)
        key_set = ['地址', '买方', '海关编码', '收货方', '合同号', '传真', '电话', '发票日期', '发票号码']
        result = fill_form(DL, key_set, table_filed_name)
        result_json = json.dumps(result)
        print(result_json)
        print(key_set)
