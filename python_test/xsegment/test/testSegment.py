#coding=utf-8


import os
from testTrie import Trie
from testHmm import HSegment


class MMSegment(object):



    def __init__(self , dictpath=  'dict.txt' , maxlength=5 ):
        self.__trie = Trie()
        self.__load_dict(dictpath , self.__trie)
        self.maxlength = maxlength
        self.hmm = HSegment()

    def __load_dict(self , dictpath , trie):
        with open(dictpath) as f:
            for line in f.readlines():
                line = line.strip().split()
                trie.add(line[0] , int(line[1]))


    def segment(self , words):
        if words and isinstance(words , basestring) and len(words) > 0 :
            if not isinstance(words , unicode):
                words = words.decode('utf-8')
                lindex = 0
                rindex = min(len(words) , self.maxlength)
                items = []
                unknow = []
                while lindex < len(words):
                    if self.__trie.search(words[lindex : rindex]):
                        if len(unknow):
                            items.extend(self.hmm.segment(''.join(unknow)))
                            del unknow[:]
                        items.append(words[lindex : rindex])
                        lindex = rindex 
                        rindex = min(len(words) , self.maxlength + lindex)
                        continue
                    rindex -= 1
                    if rindex == lindex:
                        unknow.append(words[lindex])
                        lindex += 1
                        rindex = min(len(words) , self.maxlength + lindex)
                if len(unknow):
                    items.extend(self.hmm.segment(''.join(unknow)))
                    del unknow[:]
                return items 
        return []


if __name__ == '__main__':
    m = MMSegment()
    print ' '.join(m.hmm.segment('在2015年开端，作为程序员来说！努力是个球！,世界杯 开赛！梅西很犀利!,世界卫生组织宣布！我了个去!梅花盛开在三月!腊月是个神奇的日子！'))
    print ' '.join(m.segment('南京市长江大桥今天竣工！'))
    print ' '.join(m.segment('理想很远大，现实很骨干'))
    print ' '.join(m.segment('做我女朋友好不好?'))
    print ' '.join(m.segment('在2015年开端，作为程序员来说！努力是个球！,世界杯 开赛！梅西很犀利!,世界卫生组织宣布！我了个去!梅花盛开在三月!腊月是个神奇的日子！'))
    print ' '.join(m.segment(''' 
 现向大家征集2015年全年 办公硬件需求，  截至日期：周五（12月12日）15点之前，请大家在规定时间内回复。
   如有需求显示器、笔记本支架、电池、电源 、内存（并符合要求） 的同学，请单独回复我，并且cc经理，同时请经理回复邮件确认即可申请。  
  2015年  三年笔记本到期的同学，为了避免之前统计不周全，有不在以下名单的同学，请单独回复我。
鼠标键盘等小额物品可直接在ite填写申请单，并经理签字领用，不需要提交给我申请。
        '''))
