# -*- coding: utf-8 -*

import re
import requests

def eq(a,b):
    return not all([a-b])

keyWord = raw_input("请输入关键词")
pageNumber = int(raw_input("请输入需要的数量"))
# if pageNumber == null:
#     pageNumber = 60
url = 'http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=' + keyWord + '&pn='
i = 1
j = 0
while j < pageNumber:
    url1 = url + str(j) + '&gsm=50'
    html = requests.get(url1).text
    pic_url = re.findall('"objURL":"(.*?)",',html,re.S)
    for each in pic_url:
        print each
        try:
            pic = requests.get(each, timeout=5)
        except Exception as err:
            print 'error'
            i += 1
            continue
        string = 'pictures\\' + str(i) + '.jpg'
        fp = open(string, 'wb')
        fp.write(pic.content)
        fp.close()
        i += 1
        if eq(pageNumber+1,i):
            exit()
    j += 60