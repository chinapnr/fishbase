# fish_base

It's my first python package, and mostly for test. Not suggest for download.

Thanks!

functions list:

## class FishCache

### get_cf_cache(self, cf, section, key)

读取 conf 文件类型(ini 文件类型)的缓存功能,不需要每次从文件中读取,第二次访问从内存字典中读取,以提高速度

举例:


    def cf_cache_demo():
    
        # 申明配置文件
        cf = configparser.ConfigParser()
        
        # 读入测试用的 conf 文件
        cf.read('test_conf.ini')
        
        # 申明 conf 文件使用的 cache
        test_cache = FishCache()
        
        # 从 conf 获得参数 args 的设置
        temp_s = test_cache.get_cf_cache(cf, 'get_args', 'args')
        print(temp_s)
  

get_md5(s)

serialize_instance(obj)

auto_add_file_ext(short_filename, ext)

check_kind_path_file(kind_name, file_name)

I will add more notes and optimized the code in the future.

