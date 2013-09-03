#!/usr/bin/env python
#coding=utf-8

import MySQLdb
import MortorServerInfo
import time


'''
数据库操作类

'''
class MidDb(object):    
    DBCONFIG = MortorServerInfo.getDBHostPort()
    con = None
    
    def __init__(self):
        self.username = self.DBCONFIG["USERNAME"]
        self.password = self.DBCONFIG["PASSWORD"]
        self.port = self.DBCONFIG["PORT"]
        self.dbhost = self.DBCONFIG["DBHOST"]
        self.dbname = self.DBCONFIG["DBNAME"]
        
    def initDbConnection(self, HOST, USER, PASSWD, DB, CHARSET = None):
        #self.con = MySQLdb.connect(host = 'im3.db.d.xiaonei.com', user = 'xndev', passwd = 'rebornlOM', db = 'stat')
        if CHARSET is not None:
            self.con = MySQLdb.connect(host = HOST, user = USER, passwd = PASSWD, db = DB, use_unicode = True, charset = CHARSET)
        else:
            self.con = MySQLdb.connect(host = HOST, user = USER, passwd = PASSWD, db = DB)

        self.cursor = self.con.cursor()

    def closeDbConnection(self):
        self.cursor.close()
        self.con.close()
        self.con = None
        self.cursor = None
    def doInsert(self, sql):
        self.getConn()
        exLine = 0 
        try:
            exLine = self.cursor.execute(sql)
        except Exception as e:
            print "Mysql Error %d: %s" % (e.args[0], e.args[1])
        return exLine
    def doExcuteMany(self , sql , datalines):
        self.getConn()
        exLine = 0
        try:
            exLine = self.cursor.executemany(sql,datalines)
        except Exception,e:
            print e
        return exLine
            
    def doCommit(self):
        self.con.commit()
    """
    函数功能:执行数据库select语句
    参数:sql select语句
    输出: dict词典格式 selres 查询结果以一个元组显示,如数据库无此值则,为None
                      selcount 执行select,查询出的结果数目
    描述:
        无
    """
    def doSelect(self, sql):
        self.getConn()
        try:
            nSelCount = self.cursor.execute(sql)
        except Exception, e:
            print e
        return {"selres" : self.cursor.fetchall() , "selcount" : nSelCount}
    """
    函数功能: 执行数据库delete语句
    输入:deletesql delete语句
    输出: affectrow >=0 执行成功 为受影响的行数
                    =-1 执行失败 
    描述:
        无
    """
    def doDelete(self,deleteSql):
        self.getConn()
        try:
            affectrow = self.cursor.execute(deleteSql)
        except Exception as e:
            print e
            affectrow = -1
        self.con.commit()
        return affectrow
    """
     函数功能: 链接数据库
    """
    def getConn(self):
        if  self.con is None:
            self.initDbConnection( self.dbhost , self.username , self.password , self.dbname ,"utf8")
        return self.con
if __name__ == '__main__':
    middb = MidDb()
    con = middb.getConn()
    count = 0 
    sql = "select a.appkey , a.username,b.secret , c.appsecret from token as a , user as b , app as c where a.username = b.username and a.appkey = c.appkey and a.applytime < %d order by applytime limit 500" % (time.time() + 200 * 60)
    for i in middb.doSelect(sql)["selres"]:
        count = count + 1
    print count
    print sql
    print middb.doSelect("select user.secret from token left join user on token.username=user.username limit 1")
    middb.closeDbConnection()
