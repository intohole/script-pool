#coding=utf-8





from tag import HSpeech


if __name__ == '__main__':
    h = HSpeech()
    for i in h.tag('伟大 的 习近平 总书记 亲切 访问 孤儿院 !'):
        print i[0] , i[1]


