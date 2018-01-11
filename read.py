# -*- coding: utf-8 -*-
import urllib2
import urllib

values = {"username":"doorsky123","password":"123doorsky"}
data = urllib.urlencode(values)
url = "https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"
request = urllib2.Request(url, data)
response = urllib2.urlopen(request)
print response.read()