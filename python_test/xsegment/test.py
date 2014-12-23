# coding=utf-8
#!/usr/bin/env python


from xsegment.ZooSegment import FMM


if __name__ == '__main__':
    # segment = FMM()
    class Test(object):

        """docstring for Test"""

        def __init__(self, arg):
            super(Test, self).__init__()
            self.arg = arg

        def t(self, x):
            print 't'
    print 'nr'[0]
    t = Test(1)
    if hasattr(t,'t'):
        if callable(t.t):
            print t.t('x')
        print t.t('x')
    if hasattr(t , 'a'):
        print 'xx'
    print u'我爱中国。好'.decode('utf-8')[2:4]
    # for word in segment.segment('我爱中国'):
    #     print word
