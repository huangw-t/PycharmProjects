__author__ = 'huangw-d'
import zlib
import urllib

fp = urllib.urlopen('http://www.zhihu.com/')
str = fp.read()
fp.close()

# 压缩数据流
str1 = zlib.compress(str, zlib.Z_BEST_COMPRESSION)
str2 = zlib.decompress(str1)
print(len(str))
print(len(str1))
print(len(str2))
