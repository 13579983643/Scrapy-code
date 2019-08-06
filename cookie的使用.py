# -*- coding: utf-8 -*-
# cookie 版本1
# 功能：将cookie保存到变量
# 作者：张浩南

import urllib2
import cookielib

#声明一个CookieJar对象实例来保存cookie

cookie = cookielib.CookieJar()

#利用urllib2库的 HTTPCookProcessor  对象来创建cookie处理器

handler = urllib2.HTTPCookieProcessor(cookie)

#通过handle 来构建opener

opener = urllib2.build_opener(handler)

#此处的open 方法同urllib2的urlopen方法，也可以传入request

response = opener.open('http://www.baidu.com')
for item in cookie:
    print 'Name = ' + item.name
    print 'Value = '+item.value




