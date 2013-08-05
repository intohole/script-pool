#!/usr/bin/python
#coding=utf8



class Class1:
    def __init__(self):
        self.age = 18
        self.name = u"我"



class Class2(object):
    def __init__(self,age,name):
        self.age = age 
        self.name = name 
        self.ll = 11
    @classmethod 
    def pri(cls):
        print cls



clas2 = Class2(11,u'李旭则')
clas2.pri()

