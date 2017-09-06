import requests
import re
import json

def crawl(page):
    pn = (page-1)*8
    url = "https://sp0.baidu.com/8aQDcjqpAAV3otqbppnN2DJv/api.php?resource_id=6863&from_mid=1&&format=json&ie=utf-8&oe=utf-8&query=%E5%8A%A8%E6%BC%AB&sort_key=16&sort_type=1&stat0=&stat1=&stat2=&stat3=&pn=" + str(pn) + "&rn=8&cb=jQuery110208255298612769988_1500298565004&_=1500298565026"
    res = requests.get(url)
    json_str_re = re.compile("{.*}")
    json_str = json_str_re.search(res.text).group()
    comic_dict = json.loads(json_str)
    for comic in comic_dict["data"][0]["disp_data"]:
        print(comic["ename"])

if __name__ == '__main__':
    for page in range(1,6):
        crawl(page)
