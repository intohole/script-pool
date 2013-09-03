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
    return {'JUDGE_FILE':'/home/lixuze/motor.dat','WAIT_TIME':1,'SAVE_TOKEN_PATH':'/home/lixuze/tokensave.dat','EVERY_GET_COUNT':50,'UPDATE_BUFFER_TIME':240,'SELECT_COUNT':2000,'LOG_PATH':'/home/lixuze/tokenlog.dat','SERVER_IP':'192.168.1.115','SERVER_PORT':9090 ,'MYSQL_TIME_RANGE':60 , 'MYSQL_FILE':'/home/lixuze/mysql.dat','CLIENT_WAIT_FILE':'/home/lixuze/waitclient.dat' , 'WAIT_BUFFER_TIME':1 , 'WAIT_COUNT':10 ,'USER_LIST':'/home/lixuze/userlist.dat'}

