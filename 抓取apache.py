import re
import requests
import html
import time
from bs4 import BeautifulSoup

def crawl_apache_list_use_bs4():
    url = "http://127.0.0.1"
    res = requests.get(url)
    soup = BeautifulSoup(res.text,"html5lib")
    apache_list = soup.find_all("div",class_="content_section_text")
    for child in apache_list:
        print(child.find('p'))
    time.sleep(1)

crawl_apache_list_use_bs4()
