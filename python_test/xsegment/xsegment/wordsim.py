#!/usr/bin/env python
#coding=utf-8

import os
from collections import defaultdict
from math import cos
from math import pi



class Node(dict):
    '''
    树节点 ， 继承dict
    '''
    pass


class WordTrie(object):

    def __init__(self):
        self.root = Node()

    def add(self, elements):
        cur_node = self.root
        for node in self.to_element(elements):
            if not cur_node.has_key(node):
                cur_node[node] = Node()
                cur_node = cur_node[node]
            else:
                cur_node = cur_node[node]

    def get_child_num(self, head_node):
        level = 0
        cur_node = self.root
        for node in self.to_element(head_node):
            if not cur_node.has_key(node):
                break
            cur_node = cur_node[node]
            level += 1
        return (0, 0) if cur_node == self.root else (len(cur_node), level)

    def to_element(self, element):
        return element


class CiLin(WordTrie):

    def to_element(self, element):
        elements = []
        word_len = len(element)
        if word_len >= 1:
            elements.append(element[0])
        if word_len >= 2:
            elements.append(element[1])
        if word_len >= 4:
            elements.append(element[2:4])
        if word_len >=5:
            elements.append(element[4])
        if word_len >=7:
            elements.append(element[5:7])
        return elements


class WordSim(object):

    def __init__(self, dictpath=os.path.join(os.path.abspath(os.path.dirname(__file__)),  'dict/cilin.txt'), a=0.65, b=0.8, c=0.9, d=0.96 ,e=0.5, f=0.1):
        self.wordForest = CiLin()
        self.word_dict = defaultdict(list)
        self.load_dict(dictpath)
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f

    def load_dict(self, dictpath):
        with open(dictpath) as f:
            for line in f.readlines():
                line = line.strip().split('=')
                if len(line) == 2:
                    self.wordForest.add(line[0])
                    for word in line[1].split():
                        if word != "":
                            self.word_dict[word].append(line[0])

    def word_sim(self, word1, word2 , desc = True):
        '''
        计算两个词的相似度 [0 , 1]
        word1 : 计算词1
        word2 : 计算词2
        desc : 是否降序排列 ， 默认降序排列
        exception : 
            如果word1 不是字符串或者为空 ， 抛出 ValueError
            如果word2 不是字符串或者为空 ， 抛出 ValueError
        返回：
            相似度list
        '''
        word1_vector = self.get_word_vector(word1)
        if word1_vector == None:
            return None
            # raise ValueError, '%s not included in dict !' % word1
        word2_vector = self.get_word_vector(word2)
        if word2_vector == None:
            return None 
            # raise ValueError, '%s not included in dict !' % word2
        result = []
        for v1 in word1_vector:
            for v2 in word2_vector:
                result.append(self.__calc_sim(v1 , v2))
        return sorted(result  , reverse = desc)
    
    def __calc_sim(self , vector1 , vector2):
        head_path = self.__get_same_start(vector1 , vector2)
        if  len(head_path) == 0:
            return self.f
        n = self.wordForest.get_child_num(head_path)[0]
        if len(head_path) == 1:
            k = abs( ord(vector1[1]) - ord(vector2[1]))
            return self.__sim(self.a , n , k)
        elif len(head_path) == 2 :
            k = abs( int(vector1[2:4]) - int(vector2[2:4]))
            return self.__sim(self.b , n , k)
        elif len(head_path) == 4:
            k = abs( ord(vector1[4]) -  ord(vector2[4]))
            return self.__sim(self.c , n , k)
        elif len(head_path) == 5:
            k = abs( int(vector1[5:7]) -  int(vector2[5:7]))
            return self.__sim(self.d , n , k)
        elif len(head_path) >=6:
            if vector1[-1] == '=':
                return 1.
            elif vector1[-1] == '#':
                return self.e
            else:
                return 1.

    def __sim(self , var , child_num , length):
        return var * cos( child_num * pi /  180  ) * ( float(child_num -length + 1 ) / child_num )


    def get_word_vector(self, word):
        if not (word and isinstance(word, (str, unicode))):
            raise ValueError, 'word not string or emtpy!'
        if self.word_dict.has_key(word):
            return self.word_dict[word]
        else:
            return None

    def __get_same_start(self , word1 , word2):
        word_len = min(len(word1) , len(word2))
        for i in range(word_len):
            if word1[i] != word2[i]:
                return word1[:i]
        return word1[:word_len]


if __name__ == '__main__':
    w = WordTrie()
    w.add('abc')
    w.add('adc')
    print w.get_child_num('a')
    w = WordSim()
    print w.word_sim('人民供' , '国民')
    print w.word_sim('人民' , '群众')
    print w.word_sim('人民' , '先锋')
    print w.word_sim('骄傲' , '谦虚')
