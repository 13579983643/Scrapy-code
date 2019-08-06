# -*- coding: utf-8 -*-
# cookie 版本3
# 功能：从文件中获取cookie并访问
# 作者：张浩南

import urllib2
import cookielib

# 创建MozillaCookieJar实例对象
cookie = cookielib.MozillaCookieJar()
# 从文件中读取cookie内容到变量
cookie.load('cookie.txt', ignore_discard=True, ignore_expires=True)
# 创建请求的request
req = urllib2.Request("http://www.baidu.com")
# 利用urllib2的build_opener方法创建一个opener
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
response = opener.open(req)
print response.read()