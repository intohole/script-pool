#!/usr/bin/env python
# coding=utf-8

def getDBHostPort():
    return {'DBHOST':'192.168.70.12',\
            'PORT':3606 ,\
            'USERNAME':"mota",\
            "PASSWORD":"motadb" ,\
            "DBNAME":"sina"}

    '''
    UPDATE_BUFFER_TIME:数据库更新token时间间隔(分钟)
    '''
def getMotorServerConfig():
    return {'CLIENT_SIGN':'192.168.1.115','LOG_PATH':'/home/lixuze/tokenlog.dat' , 'SERVER_IP':'192.168.1.115','SERVER_PORT':9090}


def getTokenGetConfig():
    return {'RETRY_COUNT':2 , 'SLEEP_TIME':1}
