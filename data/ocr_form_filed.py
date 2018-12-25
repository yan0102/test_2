# encoding: utf-8
import pickle
import pandas as pd
import numpy as np
import os


def form_key_set(path, write_path):
    if os.path.exists(write_path):
        os.remove(write_path)
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

    with open(write_path, 'wb') as f:
        pickle.dump([key_set, table_filed_name], f)


form_key_set('ocr_form_filed.xlsx', '../mp_OCR/OCR_table_filling/ocr_form_filed.pkl')
