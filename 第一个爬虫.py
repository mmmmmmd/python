import urllib2
res = urllib2.urlopen('http://127.0.0.1')
ret = res.read()
print ret
