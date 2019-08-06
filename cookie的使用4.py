# -*- coding: utf-8 -*-
# cookie 版本4
# 功能：利用cookie模拟网站登录
# 作者：张浩南
import urllib
import urllib2
import cookielib

filename = 'cookie.txt'
# 声明一个MozillaCookieJar 对象实例来保存cookie ，之后写入文件
cookie = cookielib.MozillaCookieJar(filename)
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie) )

postdata = urllib.urlencode({'stuid': '201200131012', 'pwd': '23342321'})
#登录教务系统的URL
loginUrl = 'http://jwxt.sdu.edu.cn:7890/pls/wwwbks/bks_login2.logi'
#模拟登陆，并把cookie保存到变量

result = opener.open(loginUrl,postdata)

#保存cookie到cookie.txt中
cookie.save(ignore_discard = True , ignore_expires = True)
#利用cookie请求访问另一个网站，此网站是成绩查询网站
gradeUrl = 'http://jwxt.sdu.edu.cn:7890/pls/wwwbks/bkscjcx.curscopre'

#请求访问成绩查询网址
result = opener.open(gradeUrl)
print result.read()

