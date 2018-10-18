"""
爬取CSDN博客的总访问量（总阅读量）


"""

from urllib.request import urlopen
from bs4 import BeautifulSoup
from datetime import datetime
from re import sub
from time import sleep

html = urlopen ("https://me.csdn.net/ChenVast")
bsObj = BeautifulSoup (html, "html.parser")
data = bsObj.find ('body').find ('div', {'class': 'tab_page my_tab_page'}).find ('ul', {
    'class': 'mod_my_t clearfix'}).get_text ()
print (data.strip ("\n").split ("\n")[3])
