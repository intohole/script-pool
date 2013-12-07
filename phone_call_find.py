#!/usr/bin/env python
# coding:utf-8


import urllib
import urllib2
import time
import json
import random

URL = 'http://num.10010.com/NumApp/GoodsDetail/queryMoreNums?'


def find_phone_number(province='34', city='340', cost = 1,goodsid='341308068135'):

    query = {
        "callback": "jsonp_queryMoreNums",
        "province": "34",
        "cityCode": "340",
        "preFeeSel": cost,
        "keyValue": "",
        "rankMoney": "126",
        "goodsId": goodsid,
        "roleValue": "",
        "mid": "3400000",
        "q_p": random.randint(10,100),
        "_": long(time.time() * 1000)
    }
    header = {
        "Host": "num.10010.com",
        "Referer": "http://mall.10010.com/goodsdetail/341308068135.html",
        "User-Agent": "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/30.0.1599.114 Chrome/30.0.1599.114 Safari/537.36",
    }

    req = urllib2.Request(URL)
    for _key, _val in header.items():
        req.add_header(_key, _val)
    data = urllib.urlencode(query)
    url = req.get_full_url() + data
    return urllib2.urlopen(url).read()


def get_json(phone_string):
    json = None
    try:
        json = phone_string[
            phone_string.find('{'): phone_string.rfind('}') + 1]
    except Exception, _:
        return None
    finally:
        return json


def paser_json(phone_json):
    __json = json.loads(phone_json)
    phone_list = []
    if __json.has_key('moreNumArray'):
        for info_index in range(len(__json['moreNumArray']) / 5):
            phone_list.append((__json['moreNumArray'][info_index * 5], __json['moreNumArray'][
                              info_index * 5 + 1], __json['moreNumArray'][info_index * 5 + 2], __json['moreNumArray'][info_index * 5 + 3]))
    return phone_list


def score(phone_list):
    if not isinstance(phone_list, list):
        raise TypeError, 'phone_list must be list'
    phone_result = []
    for phone_info in phone_list:
        score = 0
        phone = str(phone_info[0])
        for _num in range(len(phone) - 1, 1, -1):
            if phone[_num] == phone[_num - 1] or (long(phone[_num]) - 1) == long(phone[_num - 1]):
                score = score + 1
        phone_result.append((score, phone_info[0]))
    return phone_result


def get_best_phone(times = 3):
    phone_list = []
    for i in range(3):
        json_html = find_phone_number()
        json_string = get_json(json_html)
        phone_list.extend(paser_json(json_string))
    result = score(phone_list)
    result.sort(reverse = True)
    return result


if __name__ == '__main__':
    print get_best_phone()
