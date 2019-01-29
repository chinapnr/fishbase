# coding=utf-8
"""

``fish_random`` 包含的是一些生成随机值的函数。

"""

# 2019.1.6 edit by David Yi, #187 #188 修改 IdCard 和 CardBin 两个类，对这里有修改
# 2019.1.13 edit by David Yi, #202 优化 class CardBin(), class IdCard()
# 2019.1.18 edit by Hu Jun, #204 优化函数名称, #200 remove fish_common.get_random_str to gen_random_str

# 2018.12.26 v1.1.5 created
import string
import random
from fishbase.fish_date import GetRandomTime, FishDateTimeFormat
from fishbase.fish_data import CardBin, IdCard


# v1.1.6 edit by Hu Jun #200 合并 fish_common.get_random_str 为 gen_random_str
# v1.1.5 edit by Hu Jun #163
def gen_random_str(min_length, max_length, prefix=None, suffix=None,
                   has_letter=True, has_digit=False, has_punctuation=False):
    """
    指定一个前后缀、字符串长度以及字符串包含字符类型，返回随机生成带有前后缀及指定长度的字符串

    :param:
        * min_length: (int) 字符串最小长度
        * max_length: (int) 字符串最小长度
        * prefix: (string) 字符串前缀
        * suffix: (string) 字符串后缀
        * has_letter: (bool) 字符串时候包含字母，默认为 True
        * has_digit: (bool) 字符串是否包含数字，默认为 False
        * has_punctuation: (bool) 字符串是否包含标点符号，默认为 False

    :return:
        * random_str: (string) 指定规则的随机字符串

    举例如下::

        print('--- gen_random_str demo ---')
        print(gen_random_str(5, 7))
        print(gen_random_str(5, 7, prefix='FISHBASE_'))
        print(gen_random_str(5, 7, prefix='FISHBASE_', suffix='.py'))
        print(gen_random_str(5, 7, has_digit=True, has_punctuation=True))
        print(gen_random_str(5, 7, prefix='FISHBASE_', has_digit=True, has_punctuation=True))
        print('---')

    执行结果::

        --- gen_string_by_range demo ---
        q4uo6E8

        FISHBASE_8uCBEUH

        FISHBASE_D4wRX2.py

        FISHBASE_65nqlNs

        FISHBASE_3"uFm$s
        ---
    """
    if not all([isinstance(min_length, int), isinstance(max_length, int)]):
        raise ValueError('min_length and max_length should be int, but we got {} and {}'.
                         format(type(min_length), type(max_length)))

    if min_length > max_length:
        raise ValueError('min_length should less than or equal to max_length')

    # 避免随机源为空
    if not any([has_letter, has_digit, has_punctuation]):
        raise ValueError('At least one value is True in has_letter, has_digit and has_punctuation')

    random_str_len = random.randint(min_length, max_length)

    random_source = ''
    random_source += string.ascii_letters if has_letter else ''
    random_source += string.digits if has_digit else ''
    random_source += string.punctuation if has_punctuation else ''

    # 避免出现 ValueError: Sample larger than population or is negative
    if random_str_len > len(random_source):
        random_source *= (random_str_len // len(random_source) + 1)

    mid_random_str = ''.join(random.sample(random_source, random_str_len))

    prefix = prefix if prefix else ''
    suffix = suffix if suffix else ''

    random_str = ''.join([prefix, mid_random_str, suffix])

    return random_str


# v1.1.6 add by Hu Jun #204
# v1.1.5 add by Jia Chunying #171
def gen_random_name(family_name=None, gender=None, length=None):
    """
    指定姓氏、性别、长度，返回随机人名，也可不指定生成随机人名

    :param:
        * family_name: (string) 姓
        * gender: (string) 性别 "01" 男性， "00" 女性, 默认 None: 随机
        * length: (int) 大于等于 2 小于等于 10 的整数, 默认 None: 随机 2 或者 3

    :return:
        * full_name: (string) 随机人名

    举例如下::

        print('--- gen_random_name demo ---')
        print(gen_name())
        print(gen_name("赵","01", 3))
        print('---')

    执行结果::

        --- gen_random_name demo ---
        师艺
        赵群腾
        ---

    """
    family_word = ("赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨朱秦尤许何吕施张孔曹严华金魏陶姜戚谢邹喻柏水窦章云苏潘葛"
                   "奚范彭郎鲁韦昌马苗凤花方俞任袁柳酆鲍史唐费廉岑薛雷贺倪汤滕殷罗毕郝邬安常乐于时傅皮卞齐康"
                   "伍余元卜顾孟平黄和穆萧尹姚邵湛汪祁毛禹狄米贝明臧计伏成戴谈宋茅庞熊纪舒屈项祝董梁杜阮蓝闵"
                   "席季麻强贾路娄危江童颜郭梅盛林刁钟徐邱骆高夏蔡田樊胡凌霍虞万支柯咎管卢莫经房裘缪干解应宗"
                   "宣丁贲邓郁单杭洪包诸左石崔吉钮龚程嵇邢滑裴陆荣翁荀羊於惠甄魏加封芮羿储靳汲邴糜松井段富巫"
                   "乌焦巴弓牧隗山谷车侯宓蓬全郗班仰秋仲伊宫宁仇栾暴甘钭厉戎祖武符刘姜詹束龙叶幸司韶郜黎蓟薄"
                   "印宿白怀蒲台从鄂索咸籍赖卓蔺屠蒙池乔阴郁胥能苍双闻莘党翟谭贡劳逄姬申扶堵冉宰郦雍却璩桑桂"
                   "濮牛寿通边扈燕冀郏浦尚农温别庄晏柴瞿阎充慕连茹习宦艾鱼容向古易慎戈廖庚终暨居衡步都耿满弘"
                   "匡国文寇广禄阙东殴殳沃利蔚越夔隆师巩厍聂晁勾敖融冷訾辛阚那简饶空曾毋沙乜养鞠须丰巢关蒯相"
                   "查后江红游竺权逯盖益桓公万俟司马上官欧阳夏侯诸葛闻人东方赫连皇甫尉迟公羊澹台公冶宗政濮阳"
                   "淳于仲孙太叔申屠公孙乐正轩辕令狐钟离闾丘长孙慕容鲜于宇文司徒司空亓官司寇仉督子车颛孙端木"
                   "巫马公西漆雕乐正壤驷公良拓拔夹谷宰父谷粱晋楚阎法汝鄢涂钦段干百里东郭南门呼延归海羊舌微生"
                   "岳帅缑亢况后有琴梁丘左丘东门西门商牟佘佴伯赏南宫墨哈谯笪年爱阳佟第五言福百家姓续")

    name_dict = {"00": ("秀娟英华慧巧美娜静淑惠珠翠雅芝玉萍红娥玲芬芳燕彩春菊兰凤洁梅琳素云莲真环雪荣爱妹霞"
                        "香月莺媛艳瑞凡佳嘉琼勤珍贞莉桂娣叶璧璐娅琦晶妍茜秋珊莎锦黛青倩婷姣婉娴瑾颖露瑶怡婵"
                        "雁蓓纨仪荷丹蓉眉君琴蕊薇菁梦岚苑婕馨瑗琰韵融园艺咏卿聪澜纯毓悦昭冰爽琬茗羽希宁欣飘"
                        "育滢馥筠柔竹霭凝晓欢霄枫芸菲寒伊亚宜可姬舒影荔枝思丽"),
                 "01": ("伟刚勇毅俊峰强军平保东文辉力明永健世广志义兴良海山仁波宁贵福生龙元全国胜学祥才发武"
                        "新利清飞彬富顺信子杰涛昌成康星光天达安岩中茂进林有坚和彪博诚先敬震振壮会思群豪心邦"
                        "承乐绍功松善厚庆磊民友裕河哲江超浩亮政谦亨奇固之轮翰朗伯宏言若鸣朋斌梁栋维启克伦翔"
                        "旭鹏泽晨辰士以建家致树炎德行时泰盛雄琛钧冠策腾楠榕风航弘")}

    if family_name is None:
        family_name = random.choice(family_word)
    if gender is None or gender not in ['00', '01']:
        gender = random.choice(['00', '01'])
    if length is None or length not in [2, 3, 4, 5, 6, 7, 8, 9, 10]:
        length = random.choice([2, 3])
    name = "".join([random.choice(name_dict[gender]) for _ in range(length - 1)])
    full_name = "{family_name}{name}".format(family_name=family_name, name=name)
    return full_name


# v1.1.6 add by Hu Jun #204
# v1.1.5 add by Jia Chunying #166
def gen_random_mobile():
    """
    随机生成一个手机号

    :return:
        * str: (string) 手机号

    举例如下::

        print('--- gen_random_mobile demo ---')
        print(gen_random_mobile())
        print(gen_random_mobile())
        print('---')

    执行结果::

        --- gen_random_mobile demo ---
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


# v1.1.6 edit by Hu Jun #204
# v1.1.6 edit by Hu Jun #190
# v1.1.5 edit by Hu Jun #162
def gen_random_float(minimum, maximum, decimals=2):
    """
    指定一个浮点数范围，随机生成并返回区间内的一个浮点数，区间为闭区间
    受限于 random.random 精度限制，支持最大 15 位精度

    :param:
        * minimum: (float) 浮点数最小取值
        * maximum: (float) 浮点数最大取值
        * decimals: (int) 小数位数，默认为 2 位

    :return:
        * random_float: (float) 随机浮点数

    举例如下::

        print('--- gen_random_float demo ---')
        print(gen_random_float(1.0, 9.0))
        print(gen_random_float(1.0, 9.0, decimals=10))
        print(gen_random_float(1.0, 9.0, decimals=20))
        print('---')

    执行结果::

        --- gen_random_float demo ---
        6.08
        6.8187342239
        2.137902497554043
        ---

    """
    if not (isinstance(minimum, float) and isinstance(maximum, float)):
        raise ValueError('param minimum, maximum should be float, but got minimum: {} maximum: {}'.
                         format(type(minimum), type(maximum)))
    if not isinstance(decimals, int):
        raise ValueError('param decimals should be a int, but we got {}'.format(type(decimals)))
    # 精度目前只支持最大 15 位
    decimals = 15 if decimals > 15 else decimals
    # 存在 round 之后四舍五入之后，精度不匹配的情况，新加判断
    while True:
        random_float = random.uniform(minimum, maximum)
        random_float = round(random_float, decimals)
        if len(str(random_float).split('.')[-1]) == decimals:
            return random_float


# v1.1.6 edit by Hu Jun #204
# v1.1.5 edit by Hu Jun #173
def get_random_areanote(zone):
    """
    省份行政区划代码，返回下辖的随机地区名称

    :param:
        * zone: (string) 省份行政区划代码 比如 '310000'

    :returns:
        * random_areanote: (string) 省份下辖随机地区名称

    举例如下::

        print('--- fish_data get_random_areanote demo ---')
        print(cardbin_get_bank_by_name(310000))
        print('---')

    输出结果::

        --- fish_data get_random_areanote demo ---
        徐汇区
        ---

    """
    # 获取省份下的地区信息
    province = str(zone)[:2]
    areanote_list = IdCard.get_areanote_info(province)
    # 选出省份名称
    province_name_list = [item for item in areanote_list if item[0] == str(zone)]

    if not (areanote_list and province_name_list):
        raise ValueError('zone error, please check and try again')

    # 只选取下辖区域
    areanote_list.remove(province_name_list[0])

    province_name = province_name_list[0][-1]
    random_areanote = random.choice(areanote_list)
    full_areanote = random_areanote[-1]
    return full_areanote.split(province_name)[-1]


# v1.1.6 edit by Hu Jun #204
# v1.1.5 edit by Hu Jun #170
def gen_random_address(zone):
    """
    通过省份行政区划代码，返回该省份的随机地址

    :param:
        * zone: (string) 省份行政区划代码 比如 '310000'

    :returns:
        * random_addr: (string) 省份下辖随机地区名称

    举例如下::

        print('--- gen_address demo ---')
        print(gen_address('310000'))
        print('---')

    输出结果::

        --- gen_address demo ---
        上海市卢湾区陵县支街918号
        ---

    """
    # 获取省份下的地区信息
    province = str(zone)[:2]
    areanote = IdCard.get_areanote_info(province)
    if not areanote:
        raise ValueError('zone error, please check and try again')
    # 第一项是省份名称
    province_name = areanote[0][-1]
    areanote_info = get_random_areanote(zone)
    address_word = ("重庆大厦,黑龙江路,十梅庵街,遵义路,湘潭街,瑞金广场,仙山街,仙山东路,仙山西大厦,白沙河路,"
                    "赵红广场,机场路,民航街,长城南路,流亭立交桥,虹桥广场,长城大厦,礼阳路,风岗街,中川路,"
                    "白塔广场,兴阳路,文阳街,绣城路,河城大厦,锦城广场,崇阳街,华城路,康城街,正阳路,和阳广场,"
                    "中城路,江城大厦,顺城路,安城街,山城广场,春城街,国城路,泰城街,德阳路,明阳大厦,春阳路,"
                    "艳阳街,秋阳路,硕阳街,青威高速,瑞阳街,丰海路,双元大厦,惜福镇街道,夏庄街道,古庙工业园,"
                    "中山街,太平路,广西街,潍县广场,博山大厦,湖南路,济宁街,芝罘路,易州广场,荷泽四路,"
                    "荷泽二街,荷泽一路,荷泽三大厦,观海二广场,广西支街,观海一路,济宁支街,莒县路,平度广场,"
                    "明水路,蒙阴大厦,青岛路,湖北街,江宁广场,郯城街,天津路,保定街,安徽路,河北大厦,黄岛路,"
                    "北京街,莘县路,济南街,宁阳广场,日照街,德县路,新泰大厦,荷泽路,山西广场,沂水路,肥城街,"
                    "兰山路,四方街,平原广场,泗水大厦,浙江路,曲阜街,寿康路,河南广场,泰安路,大沽街,红山峡支路,"
                    "西陵峡一大厦,台西纬一广场,台西纬四街,台西纬二路,西陵峡二街,西陵峡三路,台西纬三广场,"
                    "台西纬五路,明月峡大厦,青铜峡路,台西二街,观音峡广场,瞿塘峡街,团岛二路,团岛一街,台西三路,"
                    "台西一大厦,郓城南路,团岛三街,刘家峡路,西藏二街,西藏一广场,台西四街,三门峡路,城武支大厦,"
                    "红山峡路,郓城北广场,龙羊峡路,西陵峡街,台西五路,团岛四街,石村广场,巫峡大厦,四川路,寿张街,"
                    "嘉祥路,南村广场,范县路,西康街,云南路,巨野大厦,西江广场,鱼台街,单县路,定陶街,滕县路,"
                    "钜野广场,观城路,汶上大厦,朝城路,滋阳街,邹县广场,濮县街,磁山路,汶水街,西藏路,城武大厦,"
                    "团岛路,南阳街,广州路,东平街,枣庄广场,贵州街,费县路,南海大厦,登州路,文登广场,信号山支路,"
                    "延安一街,信号山路,兴安支街,福山支广场,红岛支大厦,莱芜二路,吴县一街,金口三路,金口一广场,"
                    "伏龙山路,鱼山支街,观象二路,吴县二大厦,莱芜一广场,金口二街,海阳路,龙口街,恒山路,鱼山广场,"
                    "掖县路,福山大厦,红岛路,常州街,大学广场,龙华街,齐河路,莱阳街,黄县路,张店大厦,祚山路,苏州街,"
                    "华山路,伏龙街,江苏广场,龙江街,王村路,琴屿大厦,齐东路,京山广场,龙山路,牟平街,延安三路,"
                    "延吉街,南京广场,东海东大厦,银川西路,海口街,山东路,绍兴广场,芝泉路,东海中街,宁夏路,香港西大厦,"
                    "隆德广场,扬州街,郧阳路,太平角一街,宁国二支路,太平角二广场,天台东一路,太平角三大厦,漳州路一路,"
                    "漳州街二街,宁国一支广场,太平角六街,太平角四路,天台东二街,太平角五路,宁国三大厦,澳门三路,"
                    "江西支街,澳门二路,宁国四街,大尧一广场,咸阳支街,洪泽湖路,吴兴二大厦,澄海三路,天台一广场,"
                    "新湛二路,三明北街,新湛支路,湛山五街,泰州三广场,湛山四大厦,闽江三路,澳门四街,南海支路,"
                    "吴兴三广场,三明南路,湛山二街,二轻新村镇,江南大厦,吴兴一广场,珠海二街,嘉峪关路,高邮湖街,"
                    "湛山三路,澳门六广场,泰州二路,东海一大厦,天台二路,微山湖街,洞庭湖广场,珠海支街,福州南路,"
                    "澄海二街,泰州四路,香港中大厦,澳门五路,新湛三街,澳门一路,正阳关街,宁武关广场,闽江四街,"
                    "新湛一路,宁国一大厦,王家麦岛,澳门七广场,泰州一路,泰州六街,大尧二路,青大一街,闽江二广场,"
                    "闽江一大厦,屏东支路,湛山一街,东海西路,徐家麦岛函谷关广场,大尧三路,晓望支街,秀湛二路,"
                    "逍遥三大厦,澳门九广场,泰州五街,澄海一路,澳门八街,福州北路,珠海一广场,宁国二路,临淮关大厦,"
                    "燕儿岛路,紫荆关街,武胜关广场,逍遥一街,秀湛四路,居庸关街,山海关路,鄱阳湖大厦,新湛路,漳州街,"
                    "仙游路,花莲街,乐清广场,巢湖街,台南路,吴兴大厦,新田路,福清广场,澄海路,莆田街,海游路,镇江街,"
                    "石岛广场,宜兴大厦,三明路,仰口街,沛县路,漳浦广场,大麦岛,台湾街,天台路,金湖大厦,高雄广场,海江街,"
                    "岳阳路,善化街,荣成路,澳门广场,武昌路,闽江大厦,台北路,龙岩街,咸阳广场,宁德街,龙泉路,丽水街,"
                    "海川路,彰化大厦,金田路,泰州街,太湖路,江西街,泰兴广场,青大街,金门路,南通大厦,旌德路,汇泉广场,"
                    "宁国路,泉州街,如东路,奉化街,鹊山广场,莲岛大厦,华严路,嘉义街,古田路,南平广场,秀湛路,长汀街,"
                    "湛山路,徐州大厦,丰县广场,汕头街,新竹路,黄海街,安庆路,基隆广场,韶关路,云霄大厦,新安路,仙居街,"
                    "屏东广场,晓望街,海门路,珠海街,上杭路,永嘉大厦,漳平路,盐城街,新浦路,新昌街,高田广场,市场三街,"
                    "金乡东路,市场二大厦,上海支路,李村支广场,惠民南路,市场纬街,长安南路,陵县支街,冠县支广场,"
                    "小港一大厦,市场一路,小港二街,清平路,广东广场,新疆路,博平街,港通路,小港沿,福建广场,高唐街,"
                    "茌平路,港青街,高密路,阳谷广场,平阴路,夏津大厦,邱县路,渤海街,恩县广场,旅顺街,堂邑路,李村街,"
                    "即墨路,港华大厦,港环路,馆陶街,普集路,朝阳街,甘肃广场,港夏街,港联路,陵县大厦,上海路,宝山广场,"
                    "武定路,长清街,长安路,惠民街,武城广场,聊城大厦,海泊路,沧口街,宁波路,胶州广场,莱州路,招远街,"
                    "冠县路,六码头,金乡广场,禹城街,临清路,东阿街,吴淞路,大港沿,辽宁路,棣纬二大厦,大港纬一路,贮水山支街,"
                    "无棣纬一广场,大港纬三街,大港纬五路,大港纬四街,大港纬二路,无棣二大厦,吉林支路,大港四街,普集支路,"
                    "无棣三街,黄台支广场,大港三街,无棣一路,贮水山大厦,泰山支路,大港一广场,无棣四路,大连支街,大港二路,"
                    "锦州支街,德平广场,高苑大厦,长山路,乐陵街,临邑路,嫩江广场,合江路,大连街,博兴路,蒲台大厦,黄台广场,"
                    "城阳街,临淄路,安邱街,临朐路,青城广场,商河路,热河大厦,济阳路,承德街,淄川广场,辽北街,阳信路,益都街,"
                    "松江路,流亭大厦,吉林路,恒台街,包头路,无棣街,铁山广场,锦州街,桓台路,兴安大厦,邹平路,胶东广场,章丘路,"
                    "丹东街,华阳路,青海街,泰山广场,周村大厦,四平路,台东西七街,台东东二路,台东东七广场,台东西二路,东五街,"
                    "云门二路,芙蓉山村,延安二广场,云门一街,台东四路,台东一街,台东二路,杭州支广场,内蒙古路,台东七大厦,"
                    "台东六路,广饶支街,台东八广场,台东三街,四平支路,郭口东街,青海支路,沈阳支大厦,菜市二路,菜市一街,"
                    "北仲三路,瑞云街,滨县广场,庆祥街,万寿路,大成大厦,芙蓉路,历城广场,大名路,昌平街,平定路,长兴街,"
                    "浦口广场,诸城大厦,和兴路,德盛街,宁海路,威海广场,东山路,清和街,姜沟路,雒口大厦,松山广场,长春街,"
                    "昆明路,顺兴街,利津路,阳明广场,人和路,郭口大厦,营口路,昌邑街,孟庄广场,丰盛街,埕口路,丹阳街,汉口路,"
                    "洮南大厦,桑梓路,沾化街,山口路,沈阳街,南口广场,振兴街,通化路,福寺大厦,峄县路,寿光广场,曹县路,昌乐街,"
                    "道口路,南九水街,台湛广场,东光大厦,驼峰路,太平山,标山路,云溪广场,太清路")
    random_addr = random.choice(address_word.split(','))
    if random_addr.endswith('路') or random_addr.endswith('街'):
        random_addr = ''.join([random_addr, str(random.randint(1, 1000)), '号'])
    address_pattern = '{province_name}{areanote_info}{random_addr}'
    return address_pattern.format(province_name=province_name,
                                  areanote_info=areanote_info,
                                  random_addr=random_addr)


# v1.1.5 edit by Hu Jun #172
def gen_random_bank_card(bankname, card_type):
    """
    通过指定的银行名称，随机生成该银行的卡号

    :param:
        * bankname: (string) 银行名称 eg. 中国银行
        * card_type：(string) 卡种类，可选 CC(信用卡)、DC(借记卡)

    :returns:
        * random_bank_card: (string) 随机生成的银行卡卡号

    举例如下::

        print('--- gen_random_bank_card demo ---')
        print(gen_bank_card('中国银行', 'CC'))
        print(gen_bank_card('中国银行', 'DC'))
        print('---')

    输出结果::

        --- gen_random_bank_card demo ---
        6259073791134721
        6212836989522229131
        ---

    """
    bank_info = CardBin.get_bank_info(bankname)
    if not bank_info:
        raise ValueError('bankname {} error, check and try again'.format(bankname))

    # 获取银行代码
    bank = bank_info[0][0]

    # 获取 cardbin
    cardbin_info = CardBin.get_cardbin_info(bank, card_type)
    if not cardbin_info:
        raise ValueError('card_type {} error, check and try again'.format(card_type))

    random_cardbin = random.choice(cardbin_info)

    cardbin = random_cardbin[0]
    card_len = random_cardbin[-1]

    # 银行卡前缀
    card_number_str = cardbin

    # 随机生成前N-1位
    while len(card_number_str) < card_len - 1:
        card_number_str += str(random.randint(0, 9))

    # 获取校验位
    check_code = CardBin.get_checkcode(card_number_str)
    return card_number_str + check_code


# v1.1.5 edit by Hu Jun #165
def gen_random_id_card(zone=None, gender=None, age=None, result_type='SINGLE_STR'):
    """
    根据指定的省份编号、性别或年龄，随机生成一个身份证号

    :param:
        * zone: (string) 省份编号 eg. 310000, 默认 None: 随机
        * gender：(string) 性别 "01" 男性， "00" 女性, 默认 None: 随机
        * age：(int) 年龄 默认 None：随机 身份证最早出生年份为 1970
        * result_type: (string) 返回结果数量类型，默认值 'SINGLE_STR'，表示随机返回一个身份证号，可选 'LIST'，返回一个随机身份证列表

    :returns:
        * id_num_list: (list) 随机生成的身份证号组成的列表

    举例如下::

        print('--- gen_random_id_card demo ---')
        print(gen_id('310000'))
        print(gen_id('310000', age=100))
        print(gen_id('310000', age=30, gender='00'))
        print(gen_id(age=30, gender='01', result_type='LIST'))
        print('---')

    输出结果::

        --- gen_random_id_card demo ---
        ['310109198610243547']
        ['310101197006245479']
        ['310101198808249062']
        ['441229198805145278', '440507198812196011', '441622198805222074', '441721198801046033', ...
        ---

    """
    if zone:
        province = zone[:2]
    else:
        province_list = IdCard.get_province_info()
        province = random.choice(province_list)[0]
        zone = province + '0000'
    areanote_list = IdCard.get_areanote_info(province)

    # 判断 zone 是否合法
    if zone and (zone not in set([item[0] for item in areanote_list])):
        raise ValueError('zone {} error, check and try again'.format(zone))

    # 删除省份编号，身份证前缀不包含省份编号
    areanote_list.remove([item for item in areanote_list if item[0] == zone][0])

    zone_list = [item[0] for item in areanote_list]

    total_num = 1 if result_type == 'SINGLE_STR' else 20

    id_num_list = list()

    for _ in range(total_num):
        # 顺序码的奇数分配给男性，偶数分配给女性
        gender = gender if gender else random.choice(['00', '01'])
        gender_dict = {'00': [0, 2, 4, 6, 8],
                       '01': [1, 3, 5, 7, 9]}

        now_date_str = FishDateTimeFormat.strftime(time_format='%Y-%m-%d')
        year, month, day = now_date_str.split('-')
        # 年龄最大为 1970 年开始
        if age:
            age = min(age, int(year) - 1970)
        else:
            age = random.randint(0, int(year) - 1970)

        start_date_str = '{year}-{month}-{day}'.format(year=int(year) - age, month=month, day=day)
        birth = GetRandomTime.gen_date_by_range(start_date_str, now_date_str, date_format="%Y%m%d")
        birth = str(int(year) - age) + birth[4:]

        zone = random.choice(zone_list)
        random_str = str(random.randint(10, 99))
        gender_str = str(random.choice(gender_dict.get(gender)))
        _, check_code = IdCard.get_checkcode(zone + birth + random_str + gender_str)
        random_id = ("{zone}{birth_date}{random_str}{gender}{check_code}".
                     format(zone=zone,
                            birth_date=birth,
                            random_str=random_str,
                            gender=gender_str,
                            check_code=check_code))
        id_num_list.append(random_id)
    return id_num_list


# v1.1.6 edit by Hu Jun #204
# v1.1.5 edit by Hu Jun #171
def gen_random_company_name():
    """
    随机生成一个公司名称

    :returns:
        * company_name: (string) 银行名称

    举例如下::

        print('--- gen_random_company_name demo ---')
        print(gen_random_company_name())
        print('---')

    输出结果::

        --- gen_random_company_name demo ---
        上海大升旅游质询有限责任公司
        ---

    """
    region_info = ("北京,上海,广州,深圳,天津,成都,杭州,苏州,重庆,武汉,南京,大连,沈阳,长沙,郑州,西安,青岛,"
                   "无锡,济南,宁波,佛山,南通,哈尔滨,东莞,福州,长春,石家庄,烟台,合肥,唐山,常州,太原,昆明,"
                   "潍坊,南昌,泉州,温州,绍兴,嘉兴,厦门,贵阳,淄博,徐州,南宁,扬州,呼和浩特,鄂尔多斯,乌鲁木齐,"
                   "金华,台州,镇江,威海,珠海,东营,大庆,中山,盐城,包头,保定,济宁,泰州,廊坊,兰州,洛阳,宜昌,"
                   "沧州,临沂,泰安,鞍山,邯郸,惠州,江门,襄阳,湖州,吉林,芜湖,德州,聊城,漳州,株洲,淮安,榆林,"
                   "常德,咸阳,衡阳,滨州,柳州,遵义,菏泽,南阳,新乡,湛江,岳阳,郴州,许昌,连云港,枣庄,茂名,周口,"
                   "宿迁")
    middle_word = ("泰宏本晶辉昌昌本同永康洪皇贵久圣正裕如恒长佳协义晶合优荣汇洪千东祥复昌皇久丰兴昌国裕亚大"
                   "荣康通仁元裕厚瑞如弘升久隆旺吉德谦长贵百久汇百伟升隆复飞佳隆浩发丰亨公荣复光福美禄欣丰大"
                   "祥晶宏中仁宏华隆盈旺仁顺春满美中谦瑞和圣多信合盛千亚晶祥鑫隆飞鑫优合本旺发久国汇百恒佳东"
                   "洪通恒大公中优广宝盈泰如合丰捷本伟华春元亚广中晶如浩仁汇亚永凯富富裕茂华中飞浩台美佳圣仁"
                   "成全润金庆百贵康仁茂皇东广荣宏荣新元康公升亨洪福伟永义巨国升进合耀巨润巨元发洪源寿仁发光"
                   "顺升凯全全辉欣成公裕康合禄兴汇顺浩贵晶捷东飞益福宏国禄元昌弘和满发巨宝生耀隆大欣昌佳本兴"
                   "吉生宝凯润新高和元亨巨久光益旺春巨鑫进东晶中飞兴中美丰同晶复耀进洪全兴汇宝捷伟仁安宏多庆"
                   "益生和干干福亚新复吉亚恒亚春德飞伟利庆华丰宏合德瑞进顺祥信合康富益全巨茂台谦厚台成福捷浩"
                   "信长飞长金利美昌满丰干佳美金洪昌富千和美旺旺晶春仁华中凯浩鼎泰辉新干高进辉同欣广庆吉益德"
                   "浩中润和春元生高进皇茂利同盈复复晶多巨圣弘捷公宝汇鑫成高新正和和巨祥光宏大丰欣恒昌昌厚合"
                   "庆泰丰干益和金洪复元顺捷金万辉全吉庆德瑞优长鼎顺汇顺欣飞浩荣祥光泰多春凯信进公优飞昌协美"
                   "多发中盈协成祥益昌汇泰春满千鼎东光优谦仁中飞生恒伟福晶宝信辉金皇升飞亨鑫安伟华元旺益大寿"
                   "皇元康耀久荣满协信凯谦宝巨丰正光发康康捷中源国多多康公利顺光辉如茂晶永大高成生裕裕和万干"
                   "飞全洪伟同发禄升欣盈高欣谦亨裕康宝复庆光皇源凯凯圣发东本辉寿捷茂和庆丰多宏亚万益公福捷升"
                   "福茂宝捷同复合隆中汇禄鑫中新德昌新大皇安东信瑞元皇皇洪瑞弘捷本鑫中亨亚广昌永宏润同成高利"
                   "台中生如百康旺巨福德春元通国成浩永康泰盛泰利生茂巨久昌佳复富隆通盈同庆皇顺如辉全旺捷皇长"
                   "全富广源恒鼎顺汇本百洪鼎进欣吉凯汇欣义东长禄捷浩益旺复弘昌生发伟荣高亨元聚广新复多富千中"
                   "兴佳升康成同贵宝生捷晶全泰全永旺发富康仁兴谦利茂亨洪佳洪元鼎全国本丰亨鑫弘富干寿春贵国成"
                   "盛大发久弘国大金生久高久益浩晶盈益瑞正丰百浩泰台合德昌昌美皇合隆裕东广亚国升益福旺高贵信"
                   "生汇多泰元厚瑞飞千顺盛如大德润新新顺润飞瑞优源宏千盛吉高大耀进信欣信利瑞荣升亨盈盛千合复"
                   "隆贵丰义公优荣宏广福华洪洪捷吉进盛盛裕国洪浩祥晶弘吉欣鼎德佳成和满台光复汇佳通浩昌欣康瑞"
                   "万亚谦兴福利千元皇瑞润禄信合长润捷中旺成金益公隆宏康亚禄隆通光广国义中优多富复盛庆千长永"
                   "国源安永千中正康发复协利皇亚协鑫义巨源中润旺高进巨新高协兴生福恒富国协捷盛同复巨千益长洪"
                   "亚欣美复康洪全高安进千汇通益美耀美台耀万康合洪禄中宏百凯华优鑫协泰兴裕欣进安茂丰光飞全飞"
                   "高康进同大洪永祥飞美满兴丰谦和鑫贵百洪通裕升干永升亨光德盛永金东鼎永裕佳和德仁荣辉同瑞恒"
                   "聚谦长广鑫金久庆国吉禄弘顺汇恒汇瑞隆洪光鼎复公鼎泰盛佳恒鼎中飞聚亚宏盈光安谦成合巨洪飞庆"
                   "久瑞正茂信协百生盛合国圣盛同同盈信宏禄仁大中皇宝德金台优长成成亚盛公美荣成昌久禄泰亚进台"
                   "辉佳凯安久本荣飞晶隆晶弘同丰辉华高光兴庆贵如耀飞仁宏欣皇洪宏金满鼎耀巨义德昌源中洪裕祥晶"
                   "本国金洪昌金源恒福万义久多谦高佳欣和凯本泰春贵大浩永寿昌禄金弘仁美久升亨辉久茂皇弘泰德成"
                   "宏美辉辉禄仁华晶春干圣长同耀光庆华晶生新辉鑫金满中千谦瑞祥昌茂复长新祥祥福同优佳恒千如兴"
                   "裕华凯康全贵巨旺祥捷厚贵富宏义盛谦同盛同益谦润东广千进辉升复昌聚吉飞飞元公台本华升美久长"
                   "庆亚升东正高弘亚庆和寿宏满万优伟浩新合聚庆万广寿东恒光圣润同高谦昌兴义仁安本捷公进康益金"
                   "庆正进正千辉和升本益高广中百新庆金同如鼎寿茂鼎庆茂瑞全禄辉美贵优丰益同信兴聚浩新协宝耀圣"
                   "晶盈飞安荣富千祥成源裕合兴佳裕旺金长禄亨本大德成亨皇通全华贵弘成福聚信福光盛丰满宏福益国"
                   "弘生弘源新万泰成生伟兴兴辉和大元和协通千宝协伟荣长禄晶盛欣隆新本复正盛和皇升万益高盈义裕"
                   "成仁巨弘千亚耀吉庆厚国新高利和润中捷亚信百合亨佳佳多信鑫永复公千佳捷元东宝协大贵本满泰长"
                   "协耀圣仁旺生干盛恒义多宏益协润长皇伟晶茂大辉谦多台高恒巨兴辉台华升满公升成元利利厚隆裕厚"
                   "高公通浩凯金皇庆新发宏大本谦升欣升华益巨益百辉亨辉成欣庆同晶瑞义久成佳利优进满康信盈东盛"
                   "华义公贵美宝信丰正谦旺华皇吉如鑫泰协全优福寿中生厚成生亚公弘顺千信祥和圣金华康德台顺全厚"
                   "协亨美万瑞美东飞万飞如长仁高全汇升宏利吉泰益发谦亚汇亚恒耀恒飞浩益通捷亨新恒百佳中成公圣"
                   "宏满鑫成旺禄元福凯百永东源庆耀万鼎公春昌广润全聚德旺洪隆宝伟亨合满隆进升盛东正新多进浩康"
                   "长合大耀和美厚如寿鑫禄德仁发庆光通义荣盈昌升荣优华国成欣大宏丰光亚复万光春鼎汇旺和辉辉伟"
                   "捷汇通寿耀益皇盛晶隆义同合益春通万飞弘如安信本利安复协庆吉新永久公鑫广同富源公宏台长辉耀"
                   "光千佳宝康祥盛富升顺亚吉皇美润仁广仁台瑞干隆美信优伟安生如成耀盛润升正升新公荣宏恒洪圣泰"
                   "弘升美益顺隆大生新茂复丰亚华恒仁弘富公美昌干永满汇如洪昌荣飞新谦万百丰进宝禄贵千生进大润"
                   "禄祥公金祥聚兴和旺盈晶百义协巨顺裕中发千辉亨美本元丰金盈盛新全国源和协富谦发万耀福大发浩"
                   "隆正宏升弘旺长德百发鼎金满春新成新台正弘润晶大盈茂厚富泰通厚协百源复广恒欣合圣本巨复多正"
                   "伟润高满凯仁凯高禄万本复信满德升茂金如富谦旺佳美盈千发宝禄进兴鼎丰圣广公进昌东润进优祥生"
                   "辉茂安顺正伟圣宝优庆厚新益亚鑫皇浩兴顺多生寿金益千丰旺义东光庆泰全协吉兴千瑞丰兴茂泰庆捷"
                   "丰升弘茂鼎润复永发多成美聚福贵合光亚聚庆大大万顺贵进光国顺飞耀佳合巨洪源祥聚百汇兴本洪荣"
                   "利春庆协成昌瑞同厚春百光国如升同仁佳合成复凯佳汇升鼎宝宝进洪和信昌康润源圣巨康同欣浩辉正"
                   "永汇泰禄弘鼎多厚和佳进荣如茂全贵祥飞祥祥汇禄合源盈如和庆利寿旺汇春盈荣洪宏凯宝润如洪金鼎"
                   "聚安和吉宏捷亚伟美洪元吉厚谦吉凯汇晶中义升协吉大益祥中鑫成正盛福满辉成亨福富益洪厚禄佳益"
                   "亨巨圣辉厚皇")
    service_type = ("咨询,中介,科技服务,文化交流服务,技术服务,信息服务,零售贸易,制造,批发贸易,集团,餐饮服务,"
                    "餐饮管理,旅游质询,人事服务")
    company_type = "股份有限公司,有限责任公司"

    company_pattern = '{region_info}{middle_word}{service_type}{company_type}'

    return company_pattern.format(region_info=random.choice(region_info.split(',')),
                                  middle_word=''.join([random.choice(middle_word)
                                                       for _ in range(random.randint(2, 5))]),
                                  service_type=random.choice(service_type.split(',')),
                                  company_type=random.choice(company_type.split(',')))
