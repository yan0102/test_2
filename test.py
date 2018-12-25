# encoding: utf-8
import re
import pickle


def rule_check(key, content):
    content = content.strip()
    if key in ('进出口类型', '报关单类型', '报关转关类型', '产品类型', '海关编号',
               '进口日期', '申报日期', '运输工具', '航次号', '提运单号', '商品名称'):
        return True
    elif key == '申报地海关':
        # 如：北京关区 0100，包含中文和四位代码，有对应的代码表，详见关区代码表
        # 校验：1、只能由中文、数字和空格构成；2、判断中文和数字是否在关区代码表内，且是否相对应
        pattern = re.compile(r'^([\u4e00-\u9fa5]+) *([0-9]+)$')
        match = pattern.match(content)
        if match:
            name = match.group(1)
            code = match.group(2)
            path = './data/key_dict_data/38_key_dict/closed_area_code.pkl'
            with open(path, 'rb') as f:
                code_name, code_simple = pickle.load(f)
            pkl_name = code_name.get(code, None)
            pkl_simple = code_simple.get(code, None)
            if name == pkl_name or name == pkl_simple
            return True
        else:
            return False
    elif key in ('预制单号', '单证流水号', 'TCS单据编号', '建议书号', '备案号', '合同协议号'):
        # 字母和数字： CQAJ181107366， 20181107502
        pass
    elif key == '出境关别':
        # 7910 | 蓉机快件，详见关区字典表
        pass
    elif key in ('境内发货人', '境外发货人'):
        # 例：5012640001 | 重庆超体科技有限公司 | 913302007588959361
        pass
    elif key in ('消费使用单位', '申报单位'):
        # 例：5012640001 | 重庆超体科技有限公司
        pass
    elif key == '运输方式':
        # 例：5 | 航空运输，详见运输工具字典表
        pass
    elif key == '许可证号':
        # 例：103 | 直通方向申请，详见许可证类别代码。
        pass
    elif key == '监管方式':
        # 例： 5015 | 区内进料加工货物，详见监管方式代码表。
        pass
    elif key == '免征性质':
        # 例：101  |  一般征税  ，详见免征性质字典表
        pass
    elif key == '启运国（地区）':
        # 例：MYS | 马来西亚  ，详见启运国（地区）字典表
        pass
    elif key == '贸易国别（地区）':
        # 例：TWN | 台湾  ，详见贸易国别（地区）字典表
        pass
    elif key == '经停港':
        # 例：MYS150 | 威士顿  ，  详见港口代码表
        pass
    elif key == '成交方式':
        # 例：1 | CIF  详见成交方式代码表
        pass
    elif key in ('运费', '保费', '杂费'):
        # 例：2单价  | 2数量   |  USD使用货币
        pass
    elif key in ('件数', '毛重（kg）', '净重（kg）', '单价', '总价'):
        # 阿拉伯数字
        pass
    elif key == '包装种类':
        # 例：22 | 纸质或纤维制盒/箱；详见包装种类代码表
        pass
    elif key == '货物存放地点':
        # 例：上海高桥保税区
        pass
    elif key == '入境口岸':
        # 例：310703  | 上海外高桥保税区；详见国内口岸代码表
        pass
    elif key == '启运港':
        # 例：993107  |  上海外高桥保税区；详见港口代码表
        pass
    elif key == '报关单类型':
        # 例：005 | 通关无纸化
        pass
    elif key == '其他事项确认':
        # 特殊关系确认【1】是；价格影响【0】否；支付特许权使用【0】否；
        pass
    elif key == '备注':
        # /1401/1401O201808241320110/
        pass
    elif key == '标记唛码':
        # N/M
        pass
    elif key == '商品编号':
        # 例：3002150090；详见商品编码表；
        pass
    elif key == '检验检疫编码':
        # 例：999；详见检验检疫名称参数表；是和商品编号对应的类别码
        pass
    elif key == '规格型号':
        pass
    elif key == '成交数量':
        # 阿拉伯数字，大于等于1
        pass
    elif key == '成交单位':
        # 例：007 | 个；详见计量单位代码表
        pass
    elif key == '币制':
        # 例：USD | 美元  ；详见币别编码表 --> 法定数量
        pass


if __name__ == '__main__':
    result = rule_check('申报地海关', '北京关区 0100')
    print(result)
