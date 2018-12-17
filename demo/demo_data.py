# demo_data
# 2018.12.9 create by David Yi

from fishbase.fish_data import *

print('--- fish_data get_idcard_checkcode demo ---')

# id number
id1 = '32012419870101001'
print(id1, get_idcard_checkcode(id1)[1])

# id number
id2 = '13052219840731647'
print(id2, get_idcard_checkcode(id2)[1])

print('---')


print('--- fish_data is_valid_id_number demo ---')

# id number false
id1 = '320124198701010012'
print(id1, is_valid_id_number(id1)[0])

# id number true
id2 = '130522198407316471'
print(id2, is_valid_id_number(id2)[0])

print('---')


# 2018.12.16 edit by David Yi
print('--- fish_data get_zonecode_by_area demo ---')

result = get_zonecode_by_area(area_str='北京市')
print(result)

result = get_zonecode_by_area(area_str='上海市')
print(result)

# 精确查询，参数不省略
result = get_zonecode_by_area(area_str='北京市', match_type='EXACT')
print(result)

# 模糊查询
result = get_zonecode_by_area(area_str='北京市', match_type='FUZZY')
print(result)

# 模糊查询，转换为地区码列表
result = get_zonecode_by_area(area_str='西安市', match_type='FUZZY')
print(result)

result0 = []
for i in result:
    result0.append(i[0])

print('---西安市---')
print(len(result0))
print(result0)

# 模糊查询
result = get_zonecode_by_area(area_str='西安', match_type='FUZZY')
print(result)

# 模糊查询, 结果返回设定 list
result = get_zonecode_by_area(area_str='西安', match_type='FUZZY', result_type='LIST')
print(result)

# 模糊查询, 结果返回设定 single_str
result = get_zonecode_by_area(area_str='西安市', match_type='FUZZY', result_type='SINGLE_STR')
print(result)

# 模糊查询, 结果返回设定 single_str，西安市 和 西安 的差别
result = get_zonecode_by_area(area_str='西安', match_type='FUZZY', result_type='SINGLE_STR')
print(result)


print('---')


result = get_cardbin_by_bank('ICBC', 'CC')
print(result)
