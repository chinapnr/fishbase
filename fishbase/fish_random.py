# coding=utf-8
"""

``fish_random`` 包含的是一些生成随机值的函数。

"""

# 2018.12.26 v1.1.5 created
import random
from fishbase.fish_common import get_random_str
from fishbase.fish_data import sqlite_query


# v1.1.5 edit by Hu Jun #163
def gen_string_by_range(min_length, max_length, prefix=None, suffix=None):
    """
    指定一个前后缀以及字符串长度，返回随机生成带有前后缀及指定长度的字符串

    :param:
        * min_length: (int) 字符串最小长度
        * max_length: (int) 字符串最小长度
        * prefix: (string) 字符串前缀
        * suffix: (string) 字符串后缀

    :return:
        * random_str: (string) 指定长度、前后缀的随机字符串
    
    举例如下::

        print('--- gen_string_by_range demo ---')
        print(gen_string_by_range(5, 7))
        print(gen_string_by_range(5, 7, prefix='FISHBASE_'))
        print(gen_string_by_range(5, 7, prefix='FISHBASE_', suffix='.py'))
        print('---')

    执行结果::

        --- gen_string_by_range demo ---
        q4uo6E8
        FISHBASE_8uCBEUH
        FISHBASE_D4wRX2.py
        ---
    """
    if not all([isinstance(min_length, int), isinstance(max_length, int)]):
        raise ValueError('min_length and max_length should be int, but we got {} and {}'.
                         format(type(min_length), type(max_length)))

    if min_length > max_length:
        raise ValueError('min_length should less than or equal to max_length')

    random_str_len = random.randint(min_length, max_length)
    init_rand_str = get_random_str(random_str_len, digits=True)
    prefix = prefix if prefix else ''
    suffix = suffix if suffix else ''

    random_str = ''.join([prefix, init_rand_str, suffix])

    return random_str


# v1.1.5 add by Jia Chunying #171
def gen_name(family_name=None, gender=None, length=None):
    """
    指定姓氏、性别、长度，返回随机人名，也可不指定生成随机人名

    :param:
        * family_name: (string) 姓
        * gender: (string) 性别 "01" 男性， "00" 女性, 默认 None: 随机
        * length: (int) 大于等于 2 小于等于 10 的整数, 默认 None: 随机 2 或者 3

    :return:
        * full_name: (string) 随机人名

    举例如下::

        print('--- gen_name demo ---')
        print(gen_name())
        print(gen_name("赵","01", 3))
        print('---')

    执行结果::

        --- gen_name demo ---
        师艺
        赵群腾
        ---

    """
    family_word = "赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨朱秦尤许何吕施张孔曹严华金魏陶姜戚谢邹喻柏水窦章云苏潘葛奚范彭郎鲁韦昌马苗凤花" \
                  "方俞任袁柳酆鲍史唐费廉岑薛雷贺倪汤滕殷罗毕郝邬安常乐于时傅皮卞齐康伍余元卜顾孟平黄和穆萧尹姚邵湛汪祁毛禹狄米贝" \
                  "明臧计伏成戴谈宋茅庞熊纪舒屈项祝董梁杜阮蓝闵席季麻强贾路娄危江童颜郭梅盛林刁钟徐邱骆高夏蔡田樊胡凌霍虞万支柯咎" \
                  "管卢莫经房裘缪干解应宗宣丁贲邓郁单杭洪包诸左石崔吉钮龚程嵇邢滑裴陆荣翁荀羊於惠甄魏加封芮羿储靳汲邴糜松井段富巫" \
                  "乌焦巴弓牧隗山谷车侯宓蓬全郗班仰秋仲伊宫宁仇栾暴甘钭厉戎祖武符刘姜詹束龙叶幸司韶郜黎蓟薄印宿白怀蒲台从鄂索咸籍" \
                  "赖卓蔺屠蒙池乔阴郁胥能苍双闻莘党翟谭贡劳逄姬申扶堵冉宰郦雍却璩桑桂濮牛寿通边扈燕冀郏浦尚农温别庄晏柴瞿阎充慕连" \
                  "茹习宦艾鱼容向古易慎戈廖庚终暨居衡步都耿满弘匡国文寇广禄阙东殴殳沃利蔚越夔隆师巩厍聂晁勾敖融冷訾辛阚那简饶空曾" \
                  "毋沙乜养鞠须丰巢关蒯相查后江红游竺权逯盖益桓公万俟司马上官欧阳夏侯诸葛闻人东方赫连皇甫尉迟公羊澹台公冶宗政濮阳" \
                  "淳于仲孙太叔申屠公孙乐正轩辕令狐钟离闾丘长孙慕容鲜于宇文司徒司空亓官司寇仉督子车颛孙端木巫马公西漆雕乐正壤驷公" \
                  "良拓拔夹谷宰父谷粱晋楚阎法汝鄢涂钦段干百里东郭南门呼延归海羊舌微生岳帅缑亢况后有琴梁丘左丘东门西门商牟佘佴伯赏" \
                  "南宫墨哈谯笪年爱阳佟第五言福百家姓续"

    name_dict = {"00": "秀娟英华慧巧美娜静淑惠珠翠雅芝玉萍红娥玲芬芳燕彩春菊兰凤洁梅琳素云莲真环雪荣爱妹霞香月莺媛艳瑞凡佳嘉琼勤珍"
                       "贞莉桂娣叶璧璐娅琦晶妍茜秋珊莎锦黛青倩婷姣婉娴瑾颖露瑶怡婵雁蓓纨仪荷丹蓉眉君琴蕊薇菁梦岚苑婕馨瑗琰韵融园艺"
                       "咏卿聪澜纯毓悦昭冰爽琬茗羽希宁欣飘育滢馥筠柔竹霭凝晓欢霄枫芸菲寒伊亚宜可姬舒影荔枝思丽",
                 "01": "伟刚勇毅俊峰强军平保东文辉力明永健世广志义兴良海山仁波宁贵福生龙元全国胜学祥才发武新利清飞彬富顺信子杰涛昌"
                       "成康星光天达安岩中茂进林有坚和彪博诚先敬震振壮会思群豪心邦承乐绍功松善厚庆磊民友裕河哲江超浩亮政谦亨奇固之"
                       "轮翰朗伯宏言若鸣朋斌梁栋维启克伦翔旭鹏泽晨辰士以建家致树炎德行时泰盛雄琛钧冠策腾楠榕风航弘"}

    if family_name is None:
        family_name = random.choice(family_word)
    if gender is None or gender not in ['00', '01']:
        gender = random.choice(['00', '01'])
    if length is None or length not in [2, 3, 4, 5, 6, 7, 8, 9, 10]:
        length = random.choice([2, 3])
    name = "".join([random.choice(name_dict[gender]) for _ in range(length - 1)])
    full_name = "{family_name}{name}".format(family_name=family_name, name=name)
    return full_name


# v1.1.5 add by Jia Chunying #166
def gen_mobile():
    """
    随机生成一个手机号

    :return:
        * str: (string) 手机号

    举例如下::

        print('--- gen_mobile demo ---')
        print(gen_mobile())
        print(gen_mobile())
        print('---')

    执行结果::

        --- gen_mobile demo ---
        16706146773
        14402633925
        ---

    """
    prefix_list = ["13",
                   "1400", "1410", "1440", "145", "146", "147", "148",
                   "15",
                   "162", "165", "166", "167",
                   "170", "171", "172", "173", "175", "176", "177", "178", "1740",
                   "18",
                   "191", "198", "199"]
    prefix_str = random.choice(prefix_list)
    return prefix_str + "".join(random.choice("0123456789") for _ in range(11 - len(prefix_str)))


# v1.1.5 edit by Hu Jun #162
def gen_float_by_range(min, max, decimals=2):
    """
    指定一个浮点数范围，随机生成并返回区间内的一个浮点数，区间为闭区间
    受限于 random.random 精度限制，支持最大 15 位精度

    :param:
        * min: (float) 浮点数最小取值
        * max: (float) 浮点数最大取值
        * decimals: (int) 小数位数，默认为 2 位

    :return:
        * random_float: (float) 随机浮点数

    举例如下::

        print('--- gen_float_by_range demo ---')
        print(gen_float_by_range(1.0, 9.0))
        print(gen_float_by_range(1.0, 9.0, decimals=10))
        print(gen_float_by_range(1.0, 9.0, decimals=20))
        print('---')

    执行结果::

        --- gen_float_by_range demo ---
        6.08
        6.8187342239
        2.137902497554043
        ---

    """
    if not (isinstance(min, float) and isinstance(max, float)):
        raise ValueError('param min and max should be float, but we got min: {} max: {}'.
                         format(type(min), type(max)))
    if not isinstance(decimals, int):
        raise ValueError('param decimals should be a int, but we got {}'.format(type(decimals)))
    # 精度目前只支持最大 15 位
    decimals = 15 if decimals > 15 else decimals
    # 存在 round 之后四舍五入之后位的情况，新加判断
    while True:
        random_float = random.uniform(min, max)
        random_float = round(random_float, decimals)
        if len(str(random_float).split('.')[-1]) == decimals:
            return random_float


# v1.1.5 edit by Hu Jun #173
def get_random_zone_name(province_zone):
    """
    省份行政区划代码，返回下辖的随机地区名称：

    :param:
        * province_zone: (int) 省份行政区划代码 比如 310000

    :returns:
        * random_zone_name: (string) 省份下辖随机地区名称

    举例如下::

        print('--- fish_data get_random_zone_name demo ---')
        print(get_bank_by_name(310000))
        print('---')

    输出结果::

        --- fish_data get_random_zone_name demo ---
        徐汇区
        ---

    """
    province_num = str(province_zone)[:2]
    values = sqlite_query('fish_data.sqlite',
                          'select zone, note from cn_idcard where province = :province_num '
                          'and zone != :zone',
                          {"province_num": province_num, 'zone': province_zone})
    # 获取省份名称
    province_name = sqlite_query('fish_data.sqlite',
                                 'select note from cn_idcard where zone = :zone', {"zone": province_zone})
    if not (values and province_name):
        raise ValueError('province_zone error, please check and try again')

    # 只选取下辖区域
    province_name = province_name[0][0]
    random_zone_info = random.choice(values)
    full_zone_name = random_zone_info[-1]
    return full_zone_name.split(province_name)[-1]
