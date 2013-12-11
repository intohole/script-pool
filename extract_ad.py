# coding=utf-8
#!/usr/bin/env python


import re


conection_regx = re.compile(
    '(手机|QQ|qq|热线|详情|群|电话|信|询|联系|加|电)[ ]*[:]?[ ]*\w+(-)?\w*')

short_link = re.compile('http://t.cn/\w+')

short_price = re.compile(
    '(\d+(\.\d+)? 折|(充|满|买)[ ]*\d+[ ]*(再)?[ ]*(减|送)[ ]*\d+)')

money_regx = re.compile('(\d*[\.]?\d+|零)[ ]*(千|万|元|(元)?[ ]*/[ ]*[元个]|%)')

# (\d+[ ]?(年|-))[ ]?\d(月|-|\.)[ ]?\d[ ]?日?((-|起 至)(\d+[ ]?(年|-))[ ]?\d(月|-|\.)[ ]?\d[ ]?(日)?)?
date_regx = re.compile(
    '(((\d{2,4}[ ]?(年|-|/))?[ ]?\d{1,2}[ ]?(月|-|/)[ ]?)?\d{1,2}[ ]?(号|日)([ ]?(—|-|至|起 至)[ ]?((\d{2,4}[ ]?(年|-|/))?[ ]?\d{1,2}[ ]?(月|-|/)[ ]?)?\d{1,2}[ ]?(号|日|-|/))?|\d{1,2}(\.\d{1,2})?[ ]?([-]+)[ ]?\d{1,2}(\.\d{1,2})?(日|号))')


def extract_conection(text):
    if text and isinstance(text, (str, unicode)):
        match = 0
        for i in conection_regx.finditer(text):
            match = match + 1
        return match
    return 0


def extract_link(text):
    if text and isinstance(text, (str, unicode)):
        match = 0
        for i in short_link.finditer(text):
            match = match + 1
        return match
    return 0


def extract_price(text):
    if text and isinstance(text, (str, unicode)):
        match = 0
        for i in short_price.finditer(text):
            match = match + 1
        return match
    return 0


def extract_money(text):
    if text and isinstance(text, (str, unicode)):
        match = 0
        for i in money_regx.finditer(text):
            match = match + 1
        return match
    return 0


def extract_date(text):
    if text and isinstance(text, (str, unicode)):
        match = 0
        for i in date_regx.finditer(text):
            match = match + 1
        return match
    return 0


if __name__ == "__main__":
    # print extract_conection('信55884447 qq144544')
    new_content = []
    with open('/home/lixuze/project/ad/classifier/data.txt.back') as f:
        for line in f.readlines():
            print '%s\t%s\t%s\t%s\t%s' % (line.strip(),extract_date(line.strip()), extract_money(line.strip()), extract_price(line.strip()), extract_conection(line.strip()))
    # with open('/home/lixuze/project/ad/classifier/data.txt' , 'w') as f:
    #     [f.write(line) for line in new_content]
