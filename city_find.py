# coding=utf-8
#!/usr/bin/env python


import urllib2
import urllib
import time
import json
import sys


headers = {
    "Host": "map.baidu.com",
    "Referer": "http://map.baidu.com/",
    "User-Agent": "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/30.0.1599.114 Chrome/30.0.1599.114 Safari/537.36"
}

BASE_URL = 'http://map.baidu.com/?'


def find_city(city, geo="(13202938.63,3745922.29;13267962.63,3758146.29)"):

    # query = {
    #     "newmap": 1,
    #     "reqflag": "pcmap",
    #     "biz": "1",
    #     "qt": "s",
    #     "wd": city,
    #     "c": "315",
    #     "src": "0",
    #     "wd2": "",
    #     "sug": "0",
    #     "l": "12",
    #     "b": geo,
    #     "from": "webmap",
    #     "tn": "B_NORMAL_MAP",
    #     "nn": "0",
    #     "ie": "utf-8",
    #     "t": long(time.time() * 1000)

    # }
    # query = {
    #     "newmap": "1",
    #     "reqflag": "pcmap",
    #     "biz": "1",
    #     "qt": "con",
    #     "from": "webmap",
    #     "contp": "1",
    #     "wd": city,
    #     "c": "102",
    #     "tn": "B_NORMAL_MAP",
    #     "nn": "0",
    #     "ie": "utf-8",
    #     "l": "12",
    #     "b": geo,
    #     "t": long(time.time() * 1000)
    # }

    query = {
        "newmap": "1",
        "reqflag": "pcmap",
        "biz": "1",
        "qt": "s",
        "wd": city,
        "c": "7",
        "src": "0",
        "wd2": "",
        "sug": "0",
        "l": "9",
        "b": "(12366554.66,2552210.2;12809434.66,2748818.2)",
        "from": "webmap",
        "tn": "B_NORMAL_MAP",
        "nn": "0",
        "ie": "utf-8",
        "t": long(time.time() * 1000)
    }
    # print geo
    req = urllib2.Request(BASE_URL)
    for _key, _val in headers.items():
        req.add_header(_key, _val)
    data = urllib.urlencode(query)
    url = req.get_full_url() + data
    # print url
    return urllib2.urlopen(url)


def exist_city(city):
    city_dict = json.loads(find_city(city).read())
    if city_dict.has_key('content') or city_dict.has_key('addrs'):
        if city_dict.has_key('current_city'):
            return city_dict['current_city']['up_province_name'].encode('utf-8')
    return None
    # print city_dict['current_city']['up_province_name'].encode('utf-8')
    # if city_dict.has_key('content'):
    #     city_info = json.loads(find_city(city, geo='(%s)' %
    #                                      city_dict['content'][0]['geo'].split('|')[1]).read())
    #     if city_info.has_key('content'):
    #         if city_info.has_key('current_city'):
    #             return city_info['current_city']['up_province_name'].encode('utf-8')
    # return None


if __name__ == '__main__':
    if len(sys.argv) < 5:
        print 'python city_find.py --province xx --input xx.txt'
        sys.exit()
    else:
        province = None
        inputfile = None
        for i in range(1, len(sys.argv)):
            if sys.argv[i] == '--province':
                province = sys.argv[i + 1]
                i = i + 1
            elif sys.argv[i] == '--input':
                inputfile = sys.argv[i + 1]
                i = i + 1
        if province and inputfile:
            open(inputfile + '.result','w').close()
            erro_log = open('erro.dat' , 'a')
            fileHandle = open(inputfile + '.result', 'a')
            with open(inputfile) as f:
                for line in f.readlines():
                    for i in range(3):
                        city = exist_city(line)
                        if city != None:
                            break
                    if city == None or city.find(province) == -1:
                        erro_log.write('%s\t%s\n' % (line.strip(), city))
                        erro_log.flush()
                    else:
                        fileHandle.write(line)
                        fileHandle.flush()
            fileHandle.close()
            erro_log.close()
            print 'over'
