# coding=utf-8
import pytest
from fishbase.fish_data import *


# 2018.12.10 v1.1.3 create by Jia ChunYing
# 2018.12.13 12.16 12.17 12.18 12.19 v1.1.4 edit by David Yi
# 2019.1.6 edit by David Yi, #187 #188 修改 IdCard 和 CardBin 两个类，对这里有修改
class TestData(object):

    def test_get_idcard_checkcode(self):
        # id number <= 17
        id1 = '32012419870101'
        assert IdCard.get_checkcode(id1)[0] is False
        id1 = '320124198701010012'
        assert IdCard.get_checkcode(id1)[0] is False

        # id number checkcode
        id1 = '22068119870103456'
        assert IdCard.get_checkcode(id1)[1] == '0'

        id1 = '62010519941220163'
        assert IdCard.get_checkcode(id1)[1] != '2'  # is 9

    def test_is_valid_id_number(self):
        # id number false
        id1 = '320124198701010012'
        assert IdCard.check_number(id1)[0] is False

        # id number true
        id2 = '130522198407316471'
        assert IdCard.check_number(id2)[0] is True

        # id number irregularity
        id3 = '030522198407316471'
        assert IdCard.check_number(id3)[0] is False

        # id number is int
        id3 = 130522198407316471
        assert IdCard.check_number(id3)[0] is True

    # 2018.12.16 edit by David Yi
    def test_get_zonecode_by_area(self):
        # area_str，基本测试
        values = [('110000', '北京市')]
        assert IdCard.get_zone_info('北京市') == values

        # area_str，显示设定参数
        result = IdCard.get_zone_info(area_str='上海市')
        values = [('310000', '上海市')]
        assert result == values

        # area_str, match_type = EXACT 精确
        result = IdCard.get_zone_info(area_str='北京市', match_type='EXACT')
        values = [('110000', '北京市')]
        assert result == values

        # area_str, match_type = FUZZY 模糊
        result = IdCard.get_zone_info(area_str='北京市', match_type='FUZZY')
        values = [('110000', '北京市'), ('110100', '北京市市辖区'), ('110101', '北京市东城区'), ('110102', '北京市西城区'),
                  ('110103', '北京市崇文区'), ('110104', '北京市宣武区'), ('110105', '北京市朝阳区'), ('110106', '北京市丰台区'),
                  ('110107', '北京市石景山区'), ('110108', '北京市海淀区'), ('110109', '北京市门头沟区'), ('110111', '北京市房山区'),
                  ('110112', '北京市通州区'), ('110113', '北京市顺义区'), ('110114', '北京市昌平区'), ('110115', '北京市大兴区'),
                  ('110116', '北京市怀柔区'), ('110117', '北京市平谷区'), ('110200', '北京市市辖县'), ('110221', '北京市昌平县')]
        assert result == values

        # area_str, match_type 模糊, result_type=LIST 列表
        result = IdCard.get_zone_info(area_str='西安市', match_type='FUZZY', result_type='LIST')
        values = [('610100', '陕西省西安市'), ('610101', '陕西省西安市市辖区'), ('610102', '陕西省西安市新城区'),
                  ('610103', '陕西省西安市碑林区'), ('610104', '陕西省西安市莲湖区'), ('610111', '陕西省西安市灞桥区'),
                  ('610112', '陕西省西安市未央区'), ('610113', '陕西省西安市雁塔区'), ('610114', '陕西省西安市阎良区'),
                  ('610115', '陕西省西安市临潼区'), ('610116', '陕西省西安市长安区')]
        assert result == values

        # area_str, match_type 精确, result_type=LIST 列表
        result = IdCard.get_zone_info(area_str='北京市', match_type='EXACT', result_type='LIST')
        values = [('110000', '北京市')]
        assert result == values

        # area_str, match_type 精确, result_type=SINGLE_STR 字符串
        result = IdCard.get_zone_info(area_str='北京市', match_type='EXACT', result_type='SINGLE_STR')
        values = '110000'
        assert result == values

        # area_str, 结果大于20个，返回20个
        result = len(IdCard.get_zone_info(area_str='市', match_type='FUZZY'))
        assert result == 20

        # area_str, match_type 精确, result_type=SINGLE_STR 字符串, 无结果返回
        result = IdCard.get_zone_info(area_str='美国', match_type='EXACT', result_type='SINGLE_STR')
        values = ''
        assert result == values

    # 2018.12.17 edit by David Yi
    def test_cardbin_get_cardbin_bank(self):
        # 基本测试，检查返回的结果集的第一个结果
        values = ('370247', 'ICBC', 'CC', 15)
        result = CardBin.get_cardbin_info('ICBC', 'CC')[0]
        assert result == values

        # 测试完整的返回 list
        values = [('356889', 'CMB', 'CC', 16), ('439188', 'CMB', 'CC', 16), ('439225', 'CMB', 'CC', 16),
                  ('439226', 'CMB', 'CC', 16), ('439227', 'CMB', 'CC', 16), ('518710', 'CMB', 'CC', 16),
                  ('518718', 'CMB', 'CC', 16), ('622575', 'CMB', 'CC', 16), ('622576', 'CMB', 'CC', 16),
                  ('622577', 'CMB', 'CC', 16), ('622578', 'CMB', 'CC', 16), ('622579', 'CMB', 'CC', 16),
                  ('622581', 'CMB', 'CC', 16), ('622582', 'CMB', 'CC', 16)]
        result = CardBin.get_cardbin_info('CMB', 'CC')
        assert result == values

    # 2018.12.18 edit by David Yi
    def test_cardbin_get_checkcode(self):
        # 测试校验码不正确
        values = '0'
        result = CardBin.get_checkcode('439188000699010')
        assert result != values

        # 测试校验码正确
        values = '9'
        result = CardBin.get_checkcode('439188000699010')
        assert result == values

    # 2018.12.18 edit by David Yi
    def test_cardbin_check_bankcard(self):
        # 测试银行卡校验码是否正确
        result = CardBin.check_bankcard('4391880006990100')
        assert result is False

        result = CardBin.check_bankcard('4391880006990109')
        assert result is True

    # 2018.12.19 edit by David Yi
    def test_cardbin_get_bank_by_name(self):
        # 测试银行卡名称查询
        values = [('CMB', '招商银行')]
        result = CardBin.get_bank_info('招商银行')
        assert result == values

        # 测试银行卡名称查询
        values = 'HSB'
        result = CardBin.get_bank_info('恒生银行')
        assert result[0][0] == values

        # 测试不存在银行卡名称
        values = []
        result = CardBin.get_bank_info('招银行')
        assert result == values

    # 2019.01.07 edit by Hu Jun
    def test_get_note_by_province(self):
        values = IdCard.get_areanote_info('11')
        assert values[0][0].startswith('11')

    # 2019.01.14 edit by Hu Jun
    def test_get_province_info(self):
        values = IdCard.get_province_info()
        assert len(values) > 0

    # 2019.07.17 edit by Hu Jun
    def test_get_card_detail(self):
        values = CardBin.get_card_detail('6212836989522229131')
        assert values[0]
        assert values[1].get('bank_name') == '中国银行'
        assert values[1].get('card_type') == 'DC'

    # 2019.07.17 edit by Hu Jun
    def test_get_card_detail_01(self):
        values = CardBin.get_card_detail('123762515738129')
        assert not values[0]

    # 2019.07.17 edit by Hu Jun
    def test_get_bank_name_by_code(self):
        result = CardBin.get_bank_name_by_code('ABC')
        assert result == '中国农业银行'

    # 2019.07.17 edit by Hu Jun
    def test_get_number_detail_01(self):
        values = IdCard.get_number_detail('130522198407316471')
        assert values[0]
        assert values[1].get('province') == '130000'
        assert values[1].get('gender') == '男'
        assert values[1].get('birth_date') == '19840731'

    # 2019.07.17 edit by Hu Jun
    def test_get_number_detail_02(self):
        values = IdCard.get_number_detail('130522198407316')
        assert not values[0]

    # 2021.6.22 edit by David Yi, #292, 敏感数据掩码unittest
    def test_get_idcard_number_01(self):
        values = SensitiveMask.get_idcard_number('620105199412201639')
        assert values == '620************639'

    def test_get_idcard_number_02(self):
        values = SensitiveMask.get_idcard_number('220681198701034560')
        assert values != '2206***********560'

    def test_get_idcard_number_01_raises(self):
        with pytest.raises(TypeError) as e:
            values = SensitiveMask.get_idcard_number(123)
            # print(values)
        assert True

    def test_get_bankcard_number_01(self):
        values = SensitiveMask.get_bankcard_number('4391880006990109')
        assert values == '439188******0109'

    def test_get_mobile_number_01(self):
        values = SensitiveMask.get_mobile_number('13801108286')
        assert values == '138****8286'

    def test_get_email_01(self):
        values = SensitiveMask.get_email('david@gmail.com')
        assert values == 'd***d@gmail.com'
