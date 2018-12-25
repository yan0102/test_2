# encoding: utf-8
import re
import pickle


class ruleCheck():
    def __init__(self):
        # 说明：self.def_dict——配置每个字段对应的内部函数，用于分流
        # self.path_dict——配置每个字段对应的code表名称
        self.path_dir = './data/key_dict_data/38_key_dict/{}.pkl'
        self.def_dict = {'申报地海关': self._closed,
                         '预制单号': self._letter_number,
                         '单证流水号': self._letter_number,
                         'TCS单据编号': self._letter_number,
                         '建议书号': self._letter_number,
                         '备案号': self._letter_number,
                         '合同协议号': self._letter_number,
                         '出境关别': self._closed,
                         '进境关别': self._closed,
                         '运输方式': self._transport_mode,
                         '许可证号': self._license_type,
                         '监管方式': self._supervisor_mode,
                         '免征性质': self._exemption_nature,
                         '启运国（地区）': self._country_area,
                         '贸易国别（地区）': self._country_area,
                         '经停港': self._port,
                         '成交方式': self._closing_way,
                         '包装种类': self._packing_type,
                         '入境口岸': self._domestic_port,
                         '启运港': self._port,
                         '成交单位': self._measure_unit,
                         '币制': self._currency_coding,
                         '法定单位': self._measure_unit,
                         '第二单位': self._measure_unit,
                         '原产国': self._country_area,
                         '最终目的国': self._country_area,
                         '原产地区': self._origin_area,
                         '境内目的地': self._domestic_area,
                         '目的地': self._domestic_area,
                         '免征方式': self._exemption_mode,
                         '规格': self._container_spec
                         }

        self.path_dict = {'申报地海关': 'closed_area_code',
                          '出境关别': 'closed_area_code',
                          '进境关别': 'closed_area_code',
                          '运输方式': 'transport_mode_code',
                          '许可证号': 'license_type_code',
                          '监管方式': 'supervisor_mode_code',
                          '免征性质': 'exemption_nature_code',
                          '启运国（地区）': 'country_area_code',
                          '贸易国别（地区）': 'country_area_code',
                          '经停港': 'port_code',
                          '成交方式': 'closing_way_code',
                          '包装种类': 'packing_type_code',
                          '入境口岸': 'domestic_port_code',
                          '启运港': 'port_code',
                          '成交单位': 'measure_unit_code',
                          '币制': 'currency_coding_code',
                          '法定单位': 'measure_unit_code',
                          '第二单位': 'measure_unit_code',
                          '原产国': 'country_area_code',
                          '最终目的国': 'country_area_code',
                          '原产地区': 'origin_area_code',
                          '境内目的地': 'domestic_area_code',
                          '目的地': 'domestic_area_code',
                          '免征方式': 'exemption_mode_code',
                          '规格': 'container_spec_code'}

    def result(self, key, content):
        self.key = key
        self.content = content.strip()
        path_name = self.path_dict.get(key, None)
        self.path = self.path_dir.format(path_name)
        self.def_name = self.def_dict.get(key, None)
        return self.def_name() if self.def_name else True

    def _closed(self):
        # 如：北京关区 0100  7910 | 蓉机快件，包含中文和四位代码，有对应的代码表，详见关区代码表
        pattern = re.compile(r'^([\u4e00-\u9fa5]*) *([0-9]*)$|^([0-9]*) *\|* *([\u4e00-\u9fa5]*)$')
        match = pattern.match(self.content)
        if match:
            name = match.group(1) if match.group(1) else match.group(4)
            code = match.group(2) if match.group(2) else match.group(3)
            return self._code_name_check(name, code, 2)
        return False

    def _letter_number(self):
        # 字母和数字的校验： CQAJ181107366， 20181107502
        pattern = re.compile(r'^[A-Za-z0-9]+$')
        match = pattern.match(self.content)
        if match:
            return True
        return False

    def _transport_mode(self):
        # 例：5 | 航空运输，详见运输工具字典表
        pattern = re.compile(r'^([0-9]*) *\|* *([\u4e00-\u9fa5]*)$')
        match = pattern.match(self.content)
        if match:
            name = match.group(2)
            code = match.group(1)
            return self._code_name_check(name, code)
        return False

    def _license_type(self):
        # 例：103 | 直通放行申请，详见许可证类别代码。
        pattern = re.compile(r'^([0-9]*) *\|* *([\u4e00-\u9fa5]*)$')
        match = pattern.match(self.content)
        if match:
            name = match.group(2)
            code = match.group(1)
            return self._code_name_check(name, code)
        return False

    def _supervisor_mode(self):
        # 例： 5015 | 区内进料加工货物，详见监管方式代码表。
        pattern = re.compile(r'^([0-9]*) *\|* *([\u4e00-\u9fa5]*)$')
        match = pattern.match(self.content)
        if match:
            name = match.group(2)
            code = match.group(1)
            return self._code_name_check(name, code, 2)
        return False

    def _exemption_nature(self):
        # 例：101  |  一般征税  ，详见免征性质字典表
        pattern = re.compile(r'^([0-9]*) *\|* *([\u4e00-\u9fa5]*)$')
        match = pattern.match(self.content)
        if match:
            name = match.group(2)
            code = match.group(1)
            return self._code_name_check(name, code, 2)
        return False

    def _country_area(self):
        # 例：MYS | 马来西亚  ，详见启运国（地区）字典表
        pattern = re.compile(r'^([A-Z]*) *\|* *([\u4e00-\u9fa5]*)$')
        match = pattern.match(self.content)
        if match:
            name = match.group(2)
            code = match.group(1)
            return self._code_name_check(name, code)
        return False

    def _port(self):
        # 例：MYS150 | 威士顿  ，  详见港口代码表
        pattern = re.compile(r'^([A-Z0-9]*) *\|* *([\u4e00-\u9fa5（）]*)$')
        match = pattern.match(self.content)
        if match:
            name = match.group(2)
            code = match.group(1)
            return self._code_name_check(name, code)
        return False

    def _closing_way(self):
        # 例：1 | CIF  详见成交方式代码表
        pattern = re.compile(r'^([0-9]*) *\|* *([\u4e00-\u9fa5A-Za-z]*)$')
        match = pattern.match(self.content)
        if match:
            name = match.group(2)
            code = match.group(1)
            return self._code_name_check(name, code)
        return False

    def _packing_type(self):
        # 例：22 | 纸质或纤维制盒/箱；详见包装种类代码表
        pattern = re.compile(r'^([0-9]*) *\|* *([\u4e00-\u9fa5\/]*)$')
        match = pattern.match(self.content)
        if match:
            name = match.group(2)
            code = match.group(1)
            return self._code_name_check(name, code)
        return False

    def _domestic_port(self):
        # 例：310703  | 上海外高桥保税区；详见国内口岸代码表
        pattern = re.compile(r'^([0-9]*) *\|* *([\u4e00-\u9fa5]*)$')
        match = pattern.match(self.content)
        if match:
            name = match.group(2)
            code = match.group(1)
            return self._code_name_check(name, code)
        return False

    def _measure_unit(self):
        # 例：007 | 个；详见计量单位代码表
        pattern = re.compile(r'^([0-9]*) *\|* *([\u4e00-\u9fa5]*)$')
        match = pattern.match(self.content)
        if match:
            name = match.group(2)
            code = match.group(1)
            return self._code_name_check_1(name, code)
        return False

    def _currency(self):
        # 例：USD | 美元  ；详见币别编码表
        pattern = re.compile(r'^([0-9]*) *\|* *([\u4e00-\u9fa5]*)$')
        match = pattern.match(self.content)
        if match:
            name = match.group(2)
            code = match.group(1)
            return self._code_name_check_1(name, code)
        return False

    def _currency_coding(self):
        # 例：USD | 美元  ；详见币别编码表
        pattern = re.compile(r'^([A-Z]*) *\|* *([\u4e00-\u9fa5]*)$')
        match = pattern.match(self.content)
        if match:
            name = match.group(2)
            code = match.group(1)
            return self._code_name_check(name, code)
        return False

    def _origin_area(self):
        # 例：840 | 美国 ；或者840001 | 亚拉巴马（美国）;详见原产地区代码表
        pattern = re.compile(r'^([0-9]*) *\|* *([\u4e00-\u9fa5]*)$')
        match = pattern.match(self.content)
        if match:
            name = match.group(2)
            code = match.group(1)
            return self._code_name_check(name, code)
        return False

    def _exemption_mode(self):
        # 例：310115 | 上海市浦东新区 ；详见国内地区代码表
        pattern = re.compile(r'^([0-9]*) *\|* *([\u4e00-\u9fa5]*)$')
        match = pattern.match(self.content)
        if match:
            name = match.group(2)
            code = match.group(1)
            return self._code_name_check(name, code)
        return False

    def _domestic_area(self):
        # 例： 3 | 全免  ；详见免征方式代码表
        pattern = re.compile(r'^([0-9]*) *\|* *([\u4e00-\u9fa5]*)$')
        match = pattern.match(self.content)
        if match:
            name = match.group(2)
            code = match.group(1)
            return self._code_name_check(name, code)
        return False

    def _container_spec(self):
        # 例：普通2*标准箱（L）；详见集装箱规格代码表
        pattern = re.compile(r'^([0-9]*) *\|* *([\u4e00-\u9fa5A-Z0-9\*（）]*)$')
        match = pattern.match(self.content)
        if match:
            name = match.group(2)
            code = match.group(1)
            return self._code_name_check(name, code)
        return False

    def _code_name_check(self, name, code, type=1):
        code_other_name = 'code_chinese_name' if type == 1 else 'code_simple'
        with open(self.path, 'rb') as f:
            code_name, code_other_name = pickle.load(f)
        if name and not code and(name in code_name.values() or name in code_other_name.values()):
            return True
        if code and not name and code in code_name:
            return True
        pkl_name = code_name.get(code, None)
        pkl_other_name = code_other_name.get(code, None)
        if pkl_name and pkl_other_name and(name == pkl_name or name == pkl_other_name):
            return True
        return False

    def _code_name_check_1(self, name, code):
        with open(self.path, 'rb') as f:
            code_name = pickle.load(f)
        if name and not code and name in code_name.values():
            return True
        if code and not name and code in code_name:
            return True
        pkl_name = code_name.get(code, None)
        if pkl_name and name == pkl_name:
            return True
        return False


if __name__ == '__main__':
    rc = ruleCheck()
    rs = rc.result('规格', '普通2*标准箱（L）')
    print(rs)
