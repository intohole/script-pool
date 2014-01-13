#coding=utf-8
#!/usr/bin/env python

import re


find_face = re.compile('\\[(.*?)\\]').finditer

for face in find_face('[开心]'):
    print face.group()


weibo_file ='/home/lixuze/weibo'

face_file='/home/lixuze/face.txt'
face_dict = {}
with open(face_file , 'r') as f:
    content = [ line.strip().split('\t') for line in f.readlines()]
    for line in content:
        face_dict[line[0]] = long(line[2])
sen = open(weibo_file + '.sen' , 'w')
pos = open(weibo_file + '.pos' ,'w')
with open(weibo_file ) as f:
    content = [line.strip() for line in f.readlines()]
    for line in content:
        __count = 0
        for face in find_face(line):
            face = face.group()
            if not face_dict.has_key(face):
                continue
            __count = face_dict[face] + __count
        if __count > 0:
            sen.write(line + '\n')
        elif __count < 0:
            pos.write(line + '\n')
sen.close()
pos.close()


