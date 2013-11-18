#!/usr/bin/env python
# coding=utf-8


word_bag = {}
content_list = []
with open('/home/lixuze/下载/15.txt') as f:
    content_list = [line.strip() for line in f.readlines()]

for line in content_list:
    for word in line.split(" "):
        if word_bag.has_key(word):
            word_bag[word] = word_bag[word] + 1
        else:
            word_bag[word] = 1
with open('/home/lixuze/word_bag.dat' , 'w') as f:
    [f.write('%s %s\n' % (_key , _val)) for _key , _val in word_bag.items()]
