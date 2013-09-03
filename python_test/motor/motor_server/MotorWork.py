#!/usr/bin/env python
# coding=utf-8

'''
Created on 2013-5-19

@author: lixuze
'''
import os
from motor.ttypes import  TokenUpdateInfo
from motor.Motor import Iface
import time

import MortorServerInfo 
from TokenMySql import MidDb
from Log import Olog
from WaitClient import WaitClient


class MotorWork(Iface):
    config = MortorServerInfo.getMotorServerConfig()
    '''
    MotorWork 
    方法:
    '''


    def __init__(self):
        self.log = Olog('MotorWork' , self.config['LOG_PATH']).getLog()
        self.waitClient = WaitClient()
    
    
    def getVaildTokenInfoBySize(self, clientSign, size):
        self.log('客户端 # %s # 正在请求服务端 getVaildTokenInfoBySize size # %s #' % (clientSign,size))
        if self.waitClient.isWaitClient(clientSign):
            self.log.info('客户端 # %s # 因为ip限制,沉睡中不予返回工作内容' % clientSign)
            return []
        tokenList = self.getVaildTokenBySize(self.config['EVERY_GET_COUNT'])
        self.log('客户端 # %s # 请求服务结束 获得失效的tokenlist size # %s #' % (clientSign,len(tokenList)))
        return tokenList
    
    '''
    功能: 获得失效token列表
    原理:
    参数: 1.clientSign 计算机标识
    返回: token(TokenUpdateInfo)信息列表
    '''
    def getVaildTokenInfo(self,clientSign):
        self.log.info('客户端 # %s # 正在请求服务器 getVaildTokenInfo' % clientSign)
        if self.waitClient.isWaitClient(clientSign):
            self.log.info('客户端 # %s # 因为ip限制,沉睡中不予返回工作内容' % clientSign)
            return []
        tokenList = self.getVaildTokenBySize(self.config['EVERY_GET_COUNT'])
        self.log.info('客户端 # %s # 请求服务结束 getVaildTokenInfo 获得失效的tokenlist size # %s #' % (clientSign,len(tokenList)))
        return tokenList
    
    '''
    功能:报告更新情况
    原理: 记录到log日志,以方便观察
    参数:1.clientSign 计算机标识
        2.statusInfo 附加信息
        3.failToken  更新失败token数目
        4.getTokenSum 共更新数目
    返回:
        无
    '''
    def reporTokenStatus(self, clientSign, statusInfo, failToken, getTokenSum):
        #if getTokenSum > 0 and failToken ==0:
        #    waitClientDict = self.waitClient.readWaitClient()
        #    self.waitClient.writeWaitClient(waitClientDict , clientSign)
        #logstring = "客户端 # %s # 从服务器获得 # %s # 条token 更新失败 # %s # 附加信息 # %s #" % (clientSign,getTokenSum,failToken,statusInfo) 
        self.log.info(logstring)
    
    
    def getVaildAgentIP(self):
        pass
    
    
    '''
    功能:
    '''      
    def getVaildTokenBySize(self,size):
        self.waitWorkSign() #等待释放锁
        self.createWorkSign() #加文件锁
        tokenSave = ([],[])
        try:
            self.log.info('开始获取失效token')
            tokenList = self.readTokenInfo() #从文件读入token信息
            self.log.info('从历史文件读取# %d #条token信息' % len(tokenList))
            if len(tokenList) == 0 and self.readMysqlTime(): #如果已无token信息,并且数据访问时间不超时
                self.log.info('文件为空，从数据库中读取')
                username = self.getUserFromFile()
                if username == '':
                    return tokenSave[0]
                db = MidDb()
                db.getConn()
                sql = self.getNotVaildTokenSQLByUserName(self.config['UPDATE_BUFFER_TIME'] * 60, username ,self.config['SELECT_COUNT'])
                notvaildToken = db.doSelect(sql)
                db.closeDbConnection()
                self.writeMysqlTime()
                if notvaildToken['selcount'] > 0:
                    for t in notvaildToken['selres']:
                        token = TokenUpdateInfo(t[0],t[1],t[2],t[3],t[4])
                        tokenList.append(token)
                    self.log.info('从数据库选取出# %d #条token' % (len(tokenList)))
            tokenSave =self.getTopList(tokenList, size)
            self.log.info('选取 # %d #条token进行更新' % (len(tokenSave[0])))
            self.writeTokenInfo(tokenSave[1])#将剩余的token信息,存入到文件
            self.log.info('将剩余数据写回文件')
        except Exception,e:
            self.log.error('访问 getVaildTokenBySize 出错 # %s #' % e)
        finally:
            self.removeWordSign() #解锁
            return tokenSave[0]
    
    
    '''
    功能:获得列表前ｎ个
    原理:
    参数:
    返回:
    '''
    def getTopList(self , tokenlist, top):
        if len(tokenlist) <= top:
            return (tokenlist, [])
        else:
            tokenUpdateList = tokenlist[:top]
            
            return (tokenUpdateList, tokenlist[top:])
   
    '''
    功能:等待工作文件锁
    原理:是否存在文件
    参数:
        无
    返回:
        无
    '''   
    def waitWorkSign(self):
        wait_count = 0 
        while os.path.exists(self.config["JUDGE_FILE"]):
            time.sleep(2)
            if wait_count > long(self.config['WAIT_COUNT']):
                self.log.info('因一直死锁,强行进入,获得失效列表')
                break
            wait_count = wait_count +1
            self.log.info('有进程在等待操作')
    
    '''
    功能:创建工作锁
    原理:建立锁文件
    参数:无
    返回:无
    '''
    def createWorkSign(self):
        filehandle = open(self.config['JUDGE_FILE'], 'w')
        filehandle.close()
    
    '''
    功能:解锁
    原理:删除锁文件
    参数:无
    返回:无
    ''' 
    def removeWordSign(self):
        if os.path.exists(self.config['JUDGE_FILE']):
            os.remove(self.config['JUDGE_FILE'])
    
    '''
    功能:读取 token信息列表
    原理:文件读取,分割字符串
    参数:无
    返回:TokenUpdateInfo list 
    '''
    def readTokenInfo(self):
        if not os.path.exists(self.config['SAVE_TOKEN_PATH']):
            return []
        tokeninfolist = []
        fileHandle = open(self.config['SAVE_TOKEN_PATH'], 'r')
        contents = fileHandle.readlines()
        for line in contents:
            line = line.strip('\n')
            l = line.split('#')
            if len(l) == 5:
                tokeninfo = TokenUpdateInfo(l[0], l[1], l[2], l[3], l[4])
                tokeninfolist.append(tokeninfo)
        return tokeninfolist
                
    '''
    功能:将token列表写入文件
    参数:1 tokenlist TokenUpdateInfo list
    原理:写文件 分割字符串 
    返回:无
    '''
    def writeTokenInfo(self , tokenlist):
        fileHandle = open(self.config['SAVE_TOKEN_PATH'],'w')
        for token in tokenlist:
            tokenString = '%s#%s#%s#%s#%s' % (token.appkey,token.appsecret,token.username,token.usersecret,token.callback)
            fileHandle.write(tokenString + '\n')
        fileHandle.close()
    
    '''
    功能: 判断是否可以进行数据库操作
    原理: 判断上次进行数据库操作时间判断,如果无文件,可以进行,如果为空 ,可以进行操作 
    返回值: True 可以进行mysql操作
           False 不可以
    '''
    def readMysqlTime(self):
        isCan = False
        if not os.path.exists(self.config['MYSQL_FILE']):
            return True
        try:
            fileHandle = open(self.config['MYSQL_FILE'],'r')
            old_selecttime = fileHandle.readline()
            old_selecttime = old_selecttime.strip("\n")
        except Exception,e:
            print e
            isCan = False
        if (long(old_selecttime) + self.config['MYSQL_TIME_RANGE']) < long(time.time()) or old_selecttime == '':
            isCan = True
        else:
            self.log.info('请求数据库时间未达到时间,不允许访问数据库,请等待')
        return isCan
    
    '''
    功能:写数据库操作时间
    原理:写入文件字符串
    返回值:无
    '''
    def writeMysqlTime(self):
        fileHandle = open(self.config['MYSQL_FILE'],'w')
        fileHandle.write('%s' % long(time.time()))
        fileHandle.close()
    
    
    '''
    功能:获得一个用户名称
    原理:处理文件
    返回:字符串 
    '''
    def getUserFromFile(self):
        if not os.path.exists(self.config['USER_LIST']):
            return ''
        fileHandle = open(self.config['USER_LIST'],'r')
        contents = fileHandle.readlines()
        username = ''
        if len(contents) > 0:
            username = contents.pop().strip("\n")
        fileHandle.close()
        fileHandle = open(self.config['USER_LIST'] ,'w')
        fileHandle.writelines(contents)
        fileHandle.close()
        return username
        
            
    '''
    功能:返回失效ｔｏｋｅｎ列表语句
    参数:1 buffertime 缓冲时间
        2 limitcount 选取数目
    返回:ｓｑｌ语句
    '''
    def getNotValidTokenSQL(self, buffertime, limitcount=200):
        return "select a.appkey , c.appsecret, a.username,b.secret  , a.callbackurl from token as a , user as b , app as c where a.username = b.username and a.appkey = c.appkey and a.applytime < %d order by applytime group by username limit %d" % ((long(time.time()) + buffertime), limitcount)
    

    '''
    '''
    def getNotVaildTokenSQLByUserName(self, buffertime, username , limitcount=200):
        return "select a.appkey , c.appsecret, a.username,b.secret  , a.callbackurl from token as a , user as b , app as c where a.username = b.username and a.appkey = c.appkey and a.applytime < %d and a.username='%s' limit %d" % ((long(time.time()) + buffertime),username,limitcount)

if __name__ == "__main__":
    s = MotorWork()
    print s.getUserFromFile()
    
    
        
