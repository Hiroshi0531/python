import requests
from bs4 import BeautifulSoup
import re

'''
def get_element(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    #return soup
get_element("https://www.maruto-gp.co.jp/shop/")

for a in soup.select("a.btn.btn-warning.btn-xs"):
    shop_get = a.get("href")
    get_element(shop_get)
    print(soup.select("h1.entry-title.col-xs-12"))
'''

code_regex = re.compile('[!"#$%&\'\\\\()*+,-./:;<=>?@[\\]^_`{|}~「」〔〕“”〈〉『』【】＆＊・（）＄＃＠。、？！｀＋￥％]')

target_url= 'https://www.maruto-gp.co.jp/shop/'
r = requests.get(target_url)
soup = BeautifulSoup(r.text, "html.parser")
for a in soup.select('a.btn.btn-warning.btn-xs'):
    shop_get = a.get('href')
    shop_url = requests.get(shop_get)
    shop_info = BeautifulSoup(shop_url.text,"html.parser")
    print(re.sub(r"<[^>]*?>",'',shop_info.select('h1.entry-title.col-xs-12')))
    print(re.sub(r"<[^>]*?>",'',shop_info.selectshop_info.findAll('dd')[0]))
