#!/usr/bin/env python
#coding=utf-8

class Moudle:
    __dict__ = {}
    def __init__(self):
        pass

    def __setattr__(self,attr,val):
        self.__dict__[attr] = val

    def toDict(self):
        return self.__dict__

    def initWithDict(self,datadict):
        for _key,_value in datadict.items():
            setattr(self, _key, _value)
    def toString(self):
        restr = ''
        for _key,_value in self.__dict__.items():
            infostr = '%s,%s\n' % (_key,_value)
            restr = restr + infostr 
        return restr
    
class AppMoudle(Moudle):
    def __init__(self,AppKey='',AppSecret='',CallBack=""):
        Moudle.__init__(self)
        self.AppKey = AppKey
        self.AppSecret = AppSecret
        self.CallBack = CallBack
        
class UserMoudle(Moudle):
    def __init__(self,UserName='',UserSecret='weidou'):
        Moudle.__init__(self)
        self.UserName = UserName
        self.UserSecret = UserSecret

class TokenMoudle(Moudle):
    def __init__(self,Token='',AppKey='',UserName='',SourceAt='sina',ApplyTime=0,ExpreIn=0,State=0,HostName='',CallBackUrl='http://www.hutouxie.info',UseTime=0):
        Moudle.__init__(self)
        self.Token = Token
        self.AppKey = AppKey
        self.UserName = UserName
        self.SourceAt = SourceAt
        self.ApplyTime = ApplyTime
        self.ExpreIn = ExpreIn
        self.UseTime = UseTime
        self.State =State
        self.HostName = HostName
        self.CallBackUrl = CallBackUrl

class AccessToken(Moudle):
    def __init__(self,Token,ApplyTime,ExpreIn,Uid):
        self.Token = Token
        self.ApplyTime = ApplyTime
        self.ExpreIn = ExpreIn
        self.Uid = Uid


if __name__ == '__main__':
    token = AccessToken('sss',12232,122,'123123')
    print len(token.toDict())
    token.toString()
    

        
    