# coding=utf-8
from fishbase.fish_data import *


# 2018.12.10 v1.1.3 create by Jia ChunYing
# 2018.12.13 12.16 v1.1.4 edit by David Yi
class TestData(object):

    def test_get_idcard_checkcode(self):
        # id number <= 17
        id1 = '32012419870101'
        assert get_idcard_checkcode(id1)[0] is False
        id1 = '320124198701010012'
        assert get_idcard_checkcode(id1)[0] is False

        # id number checkcode
        id1 = '22068119870103456'
        assert get_idcard_checkcode(id1)[1] == '0'

        id1 = '62010519941220163'
        assert get_idcard_checkcode(id1)[1] != '2'  # is 9

    def test_is_valid_id_number(self):
        # id number false
        id1 = '320124198701010012'
        assert is_valid_id_number(id1)[0] is False

        # id number true
        id2 = '130522198407316471'
        assert is_valid_id_number(id2)[0] is True

        # id number irregularity
        id3 = '030522198407316471'
        assert is_valid_id_number(id3)[0] is False

        # id number is int
        id3 = 130522198407316471
        assert is_valid_id_number(id3)[0] is True

    # 2018.12.16 edit by David Yi
    def test_get_zonecode_by_area(self):
        # area_str，基本测试
        values = [('110000', '北京市')]
        assert get_zonecode_by_area('北京市') == values

        # area_str，显示设定参数
        result = get_zonecode_by_area(area_str='上海市')
        values = [('310000', '上海市')]
        assert result == values

        # area_str, match_type = EXACT 精确
        result = get_zonecode_by_area(area_str='北京市', match_type='EXACT')
        values = [('110000', '北京市')]
        assert result == values

        # area_str, match_type = FUZZY 模糊
        result = get_zonecode_by_area(area_str='北京市', match_type='FUZZY')
        values = [('110000', '北京市'), ('110100', '北京市市辖区'), ('110101', '北京市东城区'), ('110102', '北京市西城区'), ('110103', '北京市崇文区'), ('110104', '北京市宣武区'), ('110105', '北京市朝阳区'), ('110106', '北京市丰台区'), ('110107', '北京市石景山区'), ('110108', '北京市海淀区'), ('110109', '北京市门头沟区'), ('110111', '北京市房山区'), ('110112', '北京市通州区'), ('110113', '北京市顺义区'), ('110114', '北京市昌平区'), ('110115', '北京市大兴区'), ('110116', '北京市怀柔区'), ('110117', '北京市平谷区'), ('110200', '北京市市辖县'), ('110221', '北京市昌平县')]
        assert result == values

        # area_str, match_type 模糊, result_type=LIST 列表
        result = get_zonecode_by_area(area_str='西安市', match_type='FUZZY', result_type='LIST')
        values = [('610100', '陕西省西安市'), ('610101', '陕西省西安市市辖区'), ('610102', '陕西省西安市新城区'), ('610103', '陕西省西安市碑林区'), ('610104', '陕西省西安市莲湖区'), ('610111', '陕西省西安市灞桥区'), ('610112', '陕西省西安市未央区'), ('610113', '陕西省西安市雁塔区'), ('610114', '陕西省西安市阎良区'), ('610115', '陕西省西安市临潼区'), ('610116', '陕西省西安市长安区')]
        assert result == values

        # area_str, match_type 精确, result_type=LIST 列表
        result = get_zonecode_by_area(area_str='北京市', match_type='EXACT', result_type='LIST')
        values = [('110000', '北京市')]
        assert result == values

        # area_str, match_type 精确, result_type=SINGLE_STR 字符串
        result = get_zonecode_by_area(area_str='北京市', match_type='EXACT', result_type='SINGLE_STR')
        values = '110000'
        assert result == values

        # area_str, 结果大于20个，返回20个
        result = len(get_zonecode_by_area(area_str='市', match_type='FUZZY'))
        assert result == 20

        # area_str, match_type 精确, result_type=SINGLE_STR 字符串, 无结果返回
        result = get_zonecode_by_area(area_str='美国', match_type='EXACT', result_type='SINGLE_STR')
        values = ''
        assert result == values




