#!/usr/bin/env python
# -*- coding:utf-8 -*- 

import logging
import sys

class Olog(object):
    LEVELS={'debug':logging.DEBUG,
            'info':logging.INFO,
            'warning':logging.WARNING,
            'error':logging.ERROR,
            'critical':logging.CRITICAL}
    def  __init__(self,name ,filename= '/tmp/tokenlog.dat',level = 'info',fmt = '%(name)s - %(asctime)s - %(message)s'):
        self.log = logging.getLogger(name)
        self.log.setLevel(self.LEVELS[level])   
        stream_handler = logging.StreamHandler(sys.stderr)      
        hdlr = logging.FileHandler(filename)
        formatter = logging.Formatter(fmt)
        hdlr.setFormatter(formatter)
        self.log.addHandler(hdlr)
        self.log.addHandler(stream_handler)
    def getLog(self):
        return self.log


if __name__ == '__main__':
    loger = Olog('text','/home/lixuze/xx.dat')
    log = loger.getLog()
    log.warn('warn')
    log.error('erro')
    log.info('info')
    log.debug('debug')
        
    