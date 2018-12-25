# encoding: utf-8
import pickle
import os
import pandas as pd
import numpy as np


class dataStructure():
    def __init__(self):
        self.input_dir = u'../key_dict_data/38个申报关键参数字典表/{}.{}'
        self.write_dir = '../key_dict_data/38_key_dict/{}.pkl'
        self.corr_dict = {'关区代码表': self._closed,
                          '运输方式代码': self._transport_mode,
                          '29、许可证类别代码（出境、出口）()': self._license_type,
                          '监管方式代码表': self._supervisor_mode,
                          '征免性质代码': self._exemption_nature,
                          '征免方式代码': self._exemption_mode,
                          '国别（地区）代码表': self._country_area,
                          '国内口岸代码表': self._domestic_port,
                          '国内地区代码5位': self._domestic_area,
                          '港口代码表': self._port,
                          '成交方式代码': self._closing_way,
                          '包装种类代码': self._packing_type,
                          '计量单位代码': self._measure_unit,
                          '币制代码表': self._currency,
                          '币别编码': self._currency_coding,
                          '原产地区代码表': self._origin_area,
                          '集装箱规格代码': self._container_spec}

    def data_structure(self, original_name, original_file_type, save_name):
        # original_name:原文件名称， original_file_type：原文件后缀， save_name：保存名称
        self.input_path = self.input_dir.format(original_name, original_file_type)
        self.write_path = self.write_dir.format(save_name)
        if os.path.exists(self.write_path):
            os.remove(self.write_path)
        self.def_name = self.corr_dict.get(original_name, None)
        if self.def_name:
            self.def_name()

    # 关区代码表
    def _closed(self):
        data = pd.read_excel(self.input_path, header=0, dtype=np.str)
        data = data.replace(np.nan, '')
        code_name = dict(zip(data.iloc[:, 0], data.iloc[:, 1]))
        code_simple = dict(zip(data.iloc[:, 0], data.iloc[:, 2]))
        with open(self.write_path, 'wb') as f:
            pickle.dump([code_name, code_simple], f)

    # 运输方式代码
    def _transport_mode(self):
        data = pd.read_excel(self.input_path, header=0, dtype=np.str)
        data = data.replace(np.nan, '')
        code_name = dict(zip(data.iloc[:, 1], data.iloc[:, 2]))
        code_chinese_name = dict(zip(data.iloc[:, 1], data.iloc[:, 3]))
        with open(self.write_path, 'wb') as f:
            pickle.dump([code_name, code_chinese_name], f)

    # 29、许可证类别代码（出境、出口）()
    def _license_type(self):
        data = pd.read_excel(self.input_path, header=0, dtype=np.str)
        data = data.replace(np.nan, '')
        code_name = dict(zip(data.iloc[:, 1], data.iloc[:, 2]))
        code_chinese_name = dict(zip(data.iloc[:, 1], data.iloc[:, 3]))
        with open(self.write_path, 'wb') as f:
            pickle.dump([code_name, code_chinese_name], f)

    # 监管方式代码表
    def _supervisor_mode(self):
        data = pd.read_excel(self.input_path, header=0, dtype=np.str)
        data = data.replace(np.nan, '')
        code_name = dict(zip(data.iloc[:, 0], data.iloc[:, 2]))
        code_simple = dict(zip(data.iloc[:, 0], data.iloc[:, 1]))
        with open(self.write_path, 'wb') as f:
            pickle.dump([code_name, code_simple], f)

    # 征免性质代码
    def _exemption_nature(self):
        data = pd.read_excel(self.input_path, header=0, dtype=np.str)
        data = data.replace(np.nan, '')
        code_name = dict(zip(data.iloc[:, 1], data.iloc[:, 3]))
        code_simple = dict(zip(data.iloc[:, 1], data.iloc[:, 2]))
        with open(self.write_path, 'wb') as f:
            pickle.dump([code_name, code_simple], f)

    # 国别（地区）代码表
    def _country_area(self):
        data = pd.read_excel(self.input_path, header=0, dtype=np.str)
        data = data.replace(np.nan, '')
        code_name = dict(zip(data.iloc[:, 0], data.iloc[:, 2]))
        code_chinese_name = dict(zip(data.iloc[:, 0], data.iloc[:, 1]))
        with open(self.write_path, 'wb') as f:
            pickle.dump([code_name, code_chinese_name], f)

    # 港口代码表
    def _port(self):
        data = pd.read_excel(self.input_path, header=0, dtype=np.str)
        data = data.replace(np.nan, '')
        code_name = dict(zip(data.iloc[:, 0], data.iloc[:, 2]))
        code_chinese_name = dict(zip(data.iloc[:, 0], data.iloc[:, 1]))
        with open(self.write_path, 'wb') as f:
            pickle.dump([code_name, code_chinese_name], f)

    # 成交方式代码
    def _closing_way(self):
        data = pd.read_excel(self.input_path, header=0, dtype=np.str)
        data = data.replace(np.nan, '')
        code_name = dict(zip(data.iloc[:, 1], data.iloc[:, 2]))
        code_chinese_name = dict(zip(data.iloc[:, 1], data.iloc[:, 3]))
        with open(self.write_path, 'wb') as f:
            pickle.dump([code_name, code_chinese_name], f)

    # 包装种类代码
    def _packing_type(self):
        data = pd.read_excel(self.input_path, header=0, dtype=np.str)
        data = data.replace(np.nan, '')
        code_name = dict(zip(data.iloc[:, 1], data.iloc[:, 2]))
        code_chinese_name = dict(zip(data.iloc[:, 1], data.iloc[:, 3]))
        with open(self.write_path, 'wb') as f:
            pickle.dump([code_name, code_chinese_name], f)

    # 国内口岸代码表
    def _domestic_port(self):
        data = pd.read_excel(self.input_path, header=1, dtype=np.str)
        data = data.replace(np.nan, '')
        code_name = dict(zip(data.iloc[:, 0], data.iloc[:, 2]))
        code_chinese_name = dict(zip(data.iloc[:, 0], data.iloc[:, 1]))
        with open(self.write_path, 'wb') as f:
            pickle.dump([code_name, code_chinese_name], f)

    # 计量单位代码
    def _measure_unit(self):
        data = pd.read_excel(self.input_path, header=0, dtype=np.str)
        data = data.replace(np.nan, '')
        code_name = dict(zip(data.iloc[:, 1], data.iloc[:, 2]))
        with open(self.write_path, 'wb') as f:
            pickle.dump(code_name, f)

    # 币制代码表
    def _currency(self):
        data = pd.read_excel(self.input_path, header=0, dtype=np.str)
        data = data.replace(np.nan, '')
        code_name = dict(zip(data.iloc[:, 0], data.iloc[:, 1]))
        with open(self.write_path, 'wb') as f:
            pickle.dump(code_name, f)

    # 币别编码
    def _currency_coding(self):
        data = pd.read_excel(self.input_path, header=0, dtype=np.str)
        data = data.replace(np.nan, '')
        code_name = dict(zip(data.iloc[:, 1], data.iloc[:, 2]))
        code_chinese_name = dict(zip(data.iloc[:, 1], data.iloc[:, 3]))
        with open(self.write_path, 'wb') as f:
            pickle.dump([code_name, code_chinese_name], f)

    # 原产地区代码表
    def _origin_area(self):
        data = pd.read_excel(self.input_path, header=1, dtype=np.str)
        data = data.replace(np.nan, '')
        code_name = dict(zip(data.iloc[:, 0], data.iloc[:, 4]))
        code_chinese_name = dict(zip(data.iloc[:, 0], data.iloc[:, 3]))
        with open(self.write_path, 'wb') as f:
            pickle.dump([code_name, code_chinese_name], f)

    # 国内地区代码5位
    def _domestic_area(self):
        data = pd.read_excel(self.input_path, header=0, dtype=np.str)
        data = data.replace(np.nan, '')
        code_name = dict(zip(data.iloc[:, 1], data.iloc[:, 2]))
        code_chinese_name = dict(zip(data.iloc[:, 1], data.iloc[:, 3]))
        with open(self.write_path, 'wb') as f:
            pickle.dump([code_name, code_chinese_name], f)

    # 征免方式代码
    def _exemption_mode(self):
        data = pd.read_excel(self.input_path, header=0, dtype=np.str)
        data = data.replace(np.nan, '')
        code_name = dict(zip(data.iloc[:, 1], data.iloc[:, 2]))
        code_chinese_name = dict(zip(data.iloc[:, 1], data.iloc[:, 3]))
        with open(self.write_path, 'wb') as f:
            pickle.dump([code_name, code_chinese_name], f)

    # 集装箱规格代码
    def _container_spec(self):
        data = pd.read_excel(self.input_path, header=0, dtype=np.str)
        data = data.replace(np.nan, '')
        code_name = dict(zip(data.iloc[:, 1], data.iloc[:, 2]))
        code_chinese_name = dict(zip(data.iloc[:, 1], data.iloc[:, 3]))
        with open(self.write_path, 'wb') as f:
            pickle.dump([code_name, code_chinese_name], f)


if __name__ == '__main__':
    ds = dataStructure()
    # ds.data_structure('港口代码表', 'xls', 'port_code')
    # ds.data_structure('国内口岸代码表', 'xls', 'domestic_port_code')
    # ds.data_structure('计量单位代码', 'xlsx', 'measure_unit_code')
    # ds.data_structure('币制代码表', 'xlsx', 'currency_code')
    # ds.data_structure('币别编码', 'xlsx', 'currency_coding_code')
    # ds.data_structure('原产地区代码表', 'xls', 'origin_area_code')
    # ds.data_structure('国内地区代码5位', 'xlsx', 'domestic_area_code')
    # ds.data_structure('征免方式代码', 'xlsx', 'exemption_mode_code')
    # ds.data_structure('集装箱规格代码', 'xlsx', 'container_spec_code')
