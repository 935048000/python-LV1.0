import urllib
import random
import hashlib
from urllib.request import urlopen


def baidu_translate(text, fromLang='en', toLang='zh'):
    appid = 'XXXXX'
    secretKey = 'XXXXXX'
    
    httpClient = None
    myurl = 'http://api.fanyi.baidu.com/api/trans/vip/translate'
    q = text
    salt = random.randint (32768, 65536)
    
    sign = appid + q + str (salt) + secretKey
    m1 = hashlib.md5 ()
    m1.update (sign.encode ('utf-8'))
    sign = m1.hexdigest ()
    myurl = myurl + '?appid=' + appid + '&q=' + urllib.parse.quote (
        q) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str (salt) + '&sign=' + sign
    
    try:
        httpClient = urlopen (myurl)
        response = eval (httpClient.read ().decode ())
        
        print (response["trans_result"][0]["dst"])
    
    except Exception as e:
        print (e)
    finally:
        if httpClient:
            httpClient.close ()
