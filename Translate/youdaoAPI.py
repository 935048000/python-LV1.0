import urllib
import random
import hashlib
from urllib.request import urlopen


def youdao_translate(text, fromLang='EN', toLang='zh-CHS'):
    appKey = 'XXXX'
    secretKey = 'XXXXX'
    
    myurl = 'http://openapi.youdao.com/api'
    q = text
    salt = random.randint (1, 65536)
    
    sign = appKey + q + str (salt) + secretKey
    m1 = hashlib.md5 ()
    m1.update (sign.encode ('utf-8'))
    sign = m1.hexdigest ()
    myurl = myurl + '?appKey=' + appKey + '&q=' + urllib.parse.quote (
        q) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str (salt) + '&sign=' + sign
    
    try:
        httpClient = urlopen (myurl)
        response = eval (httpClient.read ().decode ())
        l1 = len (response["translation"])
        l2 = len (response["basic"]["explains"])
        if response["translation"] and l1 > l2:
            print (response["translation"])
        else:
            print (response["basic"]["explains"])
    
    
    except Exception as e:
        print (e)
    finally:
        if httpClient:
            httpClient.close ()
