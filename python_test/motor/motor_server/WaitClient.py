#!/usr/bin/env python
# coding=utf-8

import os
import MortorServerInfo
import time
from Log import Olog
'''
'''
class WaitClient(object):
    
    waitClientDict = {} #等待客户端
    config = MortorServerInfo.getMotorServerConfig() #配置
    WAIT_BUFFER_TIME = MortorServerInfo.getMotorServerConfig()['WAIT_BUFFER_TIME'] * 60
    log = Olog('WaitClient', config['LOG_PATH']).getLog() 
    
    '''
    功能:读取等待客户端列表(词典)
    原理:文件读取,分割字符串 词典结构 {电脑标识 , 上次时间}
    参数:
    返回:等待客户端(客户端标识,客户端被沉默时间)
    '''
    def readWaitClient(self):
        waitClintDict = {}
        if os.path.exists(self.config['CLIENT_WAIT_FILE']):
            fileHandle = open(self.config['CLIENT_WAIT_FILE'],'r')
            contents = fileHandle.readlines()
            for line in contents:
                line = line.strip("\n")
                clientInfo =  line.split("#")
                if len(clientInfo) == 2:
                    waitClintDict[clientInfo[0]] = clientInfo[1]
        return waitClintDict
    
    '''
    功能:写入等待客户端
    原理:写入文件
    参数:1.waitClientDict 等待客户端词典
        2.clientSign 客户端标识
    ''' 
    def writeWaitClient(self , waitClientDict , clientSign = "" ):
        if clientSign != "":
            waitClientDict[clientSign] = long(time.time())    
        fileHandle = open(self.config['CLIENT_WAIT_FILE'],'w')
        for _k , _v in waitClientDict.items():
            fileHandle.write('%s#%s\n' % (_k,_v))
        fileHandle.close()
    
    '''
    功能:判断是否是等待客户端
    原理:读取文件,判断
    参数: 1.clientSign 客户端标识
    返回: boolean 
    '''
    def isWaitClient(self,clientSign):
        waitClientDict = self.readWaitClient()
        isWait = False
        if waitClientDict.has_key(clientSign):
            self.log.info('client # %s # 因ip限制,现在不能正常工作,等待中' % clientSign)   
            isWait = True
        return isWait
    
    '''
    功能: 移除等待客户端
    原理:判断是否超过警戒时间
    参数:1.nowtime 时间
    返回:无
    '''
    def removeCanWorkClient(self , nowtime = long(time.time())):
        waitClientOldDict = self.readWaitClient()
        waitClientDict = {}
        for _client , _time in waitClientOldDict.items():
            if ( long(_time) + self.WAIT_BUFFER_TIME ) > nowtime:
                waitClientDict[_client] = _time
            else:
                self.log.info('client # %s # 可以被释放' % _client)             
        self.writeWaitClient(waitClientDict)
                 

if __name__ == "__main__":
    print time.time()
#    wc = WaitClient()
#    wc.removeCanWorkClient()
        