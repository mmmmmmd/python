import re
import urllib2

response = urllib2.urlopen("http://127.0.0.1")
html = response.read();

m = re.findall("<title>(.*)</title>",html,re.S)

for temp in m:
    print temp
