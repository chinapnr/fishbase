# 2017.8.14 small program to test fish logger.py

from fish_base.logger import *
from fish_base.fish_file import *

log_abs_filename = get_abs_filename_with_sub_path('log', 'fish_test.log')[1]

set_log_file(log_abs_filename)

logger.info('test fish base log')

print('log ok')