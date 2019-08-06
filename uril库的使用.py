# -*- coding: utf-8 -*-
import urllib2

request = urllib2.Request("http://www.baidu.com") #Resquest类的实例
response = urllib2.urlopen(request)  #调用urllib2 库里面的urlopen方法
print response.read()


# POST方法
import urllib
import urllib2

values = {"username":"390351078@qq.com", "password":"****" }
data = urllib.urlencode(values)                #利用urllib的urlencode方法将字典编码
url = "https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"
request = urllib2.Request(url, data)     #构建request时传入两个参数
response = urllib2.urlopen(request)
print response.read()

#Get方法

import urllib2
import urllib

values = {}
values['username'] = "390351078@qq.com"
values['password'] ="****"
data = urllib.urlencode(values)
url = "http://passport.csdn.net/account/login"
geturl = url + "?" + data
request = urllib2.Request(geturl)
response = urllib2.urlopen(request)
print response.read()





