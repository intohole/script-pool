#!/usr/bin/env python
# -*- coding: utf-8 -*-  


import weibopy # we use our own slightly-extended version of weibopy
import urllib,httplib
from TokenUpdateErro import TokenUpdateErro


class AssertToken(object):
    
    api = None
    
    def __init__(self):
        self.auth = weibopy.auth.OAuthHandler('','')
    
    
    def setToken(self,token = None):
        pass
        
    
    def assertToken(self,token=None):
        isVaild = True
        if token == None:
            raise TokenUpdateErro("NO_VAILD_TOKEN")
        self.auth.set_access_token(token)
        self.api = weibopy.API(self.auth)
        try:
            self.api.l_rate_limit_status()
        except Exception,e:
            print e
            isVaild = False
        return isVaild
            
    
    
if __name__ == "__main__":
    a = AssertToken()
    a.setToken('2.00EmsxPBaYmsTD2135ca0ca58dPRoB')
    try:
        a.assertToken()
    except Exception,e:
        print e