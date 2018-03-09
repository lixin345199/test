# coding:utf-8
import urllib
import urllib2
# 请求地址
url = "http://nuyd.eastmoney.com/EM_UBG_PositionChangesInterface/api/js?style=top&js=([(x)])&ac=normal&check=itntcd&dtformat=HH:mm:ss&cb=jQuery18308750232620245249_1514358625562&num=5&_=1514358685894"

# 请求
req = urllib2.Request(url)
# 请求结果数据
res_data = urllib2.urlopen(req)
# 解析请求结果数据
res = res_data.read()
# 打印请求结果
print '123456789'