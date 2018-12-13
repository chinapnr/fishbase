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

