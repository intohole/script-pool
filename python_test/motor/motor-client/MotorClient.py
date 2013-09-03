#!/usr/bin/env python
# coding=utf-8

from motor import Motor
import TokenGet 
import time
from Log import Olog
from TokenMySql import MidDb
import MortorClientInfo
from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol


config = MortorClientInfo.getMotorServerConfig()
log = Olog('motor-client', MortorClientInfo.getMotorServerConfig()['LOG_PATH']).getLog()

def getNotVaildTokenInfo():
    tokenUpdateList = []
    try:
        log.info('正在与服务器链接---')
        transport = TSocket.TSocket(config['SERVER_IP'], config['SERVER_PORT'])
        transport = TTransport.TBufferedTransport(transport)
        protocol = TBinaryProtocol.TBinaryProtocol(transport)
        client = Motor.Client(protocol)
        transport.open()
        tokenUpdateList = client.getVaildTokenInfo(config['CLIENT_SIGN'])
        log.info('开始访问服务器,获得失效列表,从服务器获得 # %d #' % len(tokenUpdateList))
        transport.close()
    except Thrift.TException, ex:
        log.info('链接服务器失败 错误 # %s #' % ex)        
    return tokenUpdateList

def getNotVaildTokenInfoBySize(size):
    tokenUpdateList = []
    try:
        log.info('正在与服务器链接---')
        transport = TSocket.TSocket(config['SERVER_IP'], config['SERVER_PORT'])
        transport = TTransport.TBufferedTransport(transport)
        protocol = TBinaryProtocol.TBinaryProtocol(transport)
        client = Motor.Client(protocol)
        transport.open()
        tokenUpdateList = client.getVaildTokenInfoBySize(config['CLIENT_SIGN'], size)
        log.info('开始访问服务器,获得失效列表-')
        transport.close()
    except Thrift.TException, ex:
        log.info('链接服务器失败 错误 # %s #' % ex)        
    return tokenUpdateList
    
def reportServerStatus(clientSign , getTokenSum , failToken , statusInfo):
    try:
        transport = TSocket.TSocket(config['SERVER_IP'], config['SERVER_PORT'])
        transport = TTransport.TBufferedTransport(transport)
        protocol = TBinaryProtocol.TBinaryProtocol(transport)
        client = Motor.Client(protocol)
        transport.open()
        client.reporTokenStatus( clientSign, statusInfo, failToken, getTokenSum)
        transport.close()
    except Thrift.TException, ex:
        log.info('链接服务器失败 错误 # %s #' % ex)    

    

def getUpdateTokenSQL(datalines):
    sqlkey  = "INSERT INTO token(appkey,username,token,applytime) VALUES "
    values = ""
    isFirst = True
    for data in datalines:
        value = """('%s','%s','%s',%d)""" % (data[0],data[1],data[2],data[3])
        if isFirst:
            values = value
            isFirst = False
        else:
            values = values + "," + value
    updatevalue = "ON DUPLICATE KEY UPDATE applytime=VALUES(applytime),token=VALUES(token)"
    return "%s %s %s" % (sqlkey,values,updatevalue)



    
    
def refreshToken():
    tokenUpdateList = getNotVaildTokenInfo()
#    m_TokenGet = TokenGet.TokenGet()
#    datalines = []
#    db = MidDb()
#    updatetoken = 0
#    log.info('开始更新token')
#    for tokeninfo in tokenUpdateList:
#        
#        token = m_TokenGet.Work(tokeninfo.appkey,tokeninfo.appsecret,tokeninfo.username,tokeninfo.usersecret,tokeninfo.callback)
#        if token != None:
#            datalines.append((tokeninfo.appkey, tokeninfo.username, token.Token, long(time.time()) + token.ExpreIn))
#        else:
#            log.error('刷新token失败 appkey # %s # username # %s # callback # %s #' % (tokeninfo.appkey,tokeninfo.username,tokeninfo.callback))
#    if len(datalines) > 0:
#        db.getConn()
#        updateSQL = getUpdateTokenSQL(datalines)
#        log.info(updateSQL)
#        updatetoken = db.doInsert(updateSQL)
#        db.doCommit()
#        db.closeDbConnection()
#        log.info('将刷新的token更新到数据库')
#    reportServerStatus(config['CLIENT_SIGN'],len(tokenUpdateList) , ( updatetoken /2 ) , '')
#    log.info('更新 # %d #条 token' % (updatetoken/2))
if __name__ == "__main__":
    getNotVaildTokenInfo()
#    reportServerStatus('192.168.1.115', 50, 0, '')
    
            