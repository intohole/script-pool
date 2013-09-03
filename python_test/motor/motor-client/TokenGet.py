#!/usr/bin/env python
# -*- coding: utf-8 -*-  


from urllib2 import Request, urlopen
import urllib
import httplib
import Moudle
from Log import Olog
import time
import MortorClientInfo

'''
类功能: 根据输入的应用id,sercet,用户id,screct获得token

作者:泽
'''
class TokenGet:
    config = MortorClientInfo.getTokenGetConfig()
    OAUTH_HOST = 'api.weibo.com'
    OAUTH_ROOT = '/oauth2/'
    lastusetime = 0
    def __init__(self):
        self.loger = Olog('TokenGet')
        self.log = self.loger.getLog()
        
    def import_simplejson(self):
        try:
            import simplejson as json
        except ImportError:
            try:
                import json  # Python 2.6+
            except ImportError:
                try:
                    from django.utils import simplejson as json  # Google App Engine
                except ImportError:
                    raise ImportError, "Can't load a json library"
        return json
    def get_access_token(self, app_key,app_secret,callback,code=None):
        try:
            url = self._get_oauth_url('access_token')
            if code == None:
                self.log.info("get_access_token code None # app_key # %s # callback # %s" % (app_key,callback) )

            parameters = {
                'client_id': app_key,
                'client_secret': app_secret,
                'grant_type': 'authorization_code',
                'redirect_uri':callback,
                'code': code
                }
            resp = urlopen(Request(url, data=self.to_postdata(parameters)))
            data = resp.read()
            r = self.import_simplejson().loads(str(data))
            token = Moudle.AccessToken(r['access_token'],r['remind_in'],r['expires_in'],r['uid'])
            return token
        except Exception, e:
            print e
            self.log.info("get_access_token failed # erro # %s # app_key # %s # callback # %s  " % (e,app_key , callback))
            return None 
    def _get_oauth_url(self, endpoint):
        prefix = 'https://'
        return prefix + self.OAUTH_HOST + self.OAUTH_ROOT + endpoint
    
    def to_postdata(self,parameters):
        """Serialize as post data for a POST request."""
        return '&'.join(['%s=%s' % (self.escape(str(k)), self.escape(str(v))) \
            for k, v in parameters.iteritems()])
    def getToken(self,userid,userserect,app_key,app_screct,callback_url):
        conn = httplib.HTTPSConnection('api.weibo.com')
        postdata = urllib.urlencode({'client_id':app_key,'response_type':'code','redirect_uri':callback_url,\
                                     'action':'submit','userId':userid,'passwd':userserect,\
                                     'isLoginSina':0,'from':'','regCallback':'','state':'','ticket':'','withOfficalFlag':0})
        conn.request('POST','/oauth2/authorize',postdata,{'Referer':self.get_code_url(app_key,callback_url),'Content-Type': 'application/x-www-form-urlencoded'})
        res = conn.getresponse()
        print res.read()
        data=res.msg 
        print   'version:' , res.version  
        print   'reason:' , res.reason  
        print   'status:' , res.status  
        print   'msg:' , res.msg  
        print   'headers:' , res.getheaders()  
        conn.close()
        try:
            return self.get_access_token(app_key,app_screct,callback_url,data['Location'].split('=')[1])
        except Exception , e:
            self.log.info('getToken -> # erro# %s # app_key # %s # app_screct  # %s #  userid # %s # userserect  # %s callback_url # %s' % (e,app_key,app_screct, userid, userserect, callback_url))
            return None
 
    '''
    得到apiUrl
    '''
    def get_code_url(self,app_key,callback_url):
        return 'https://api.weibo.com/oauth2/authorize?redirect_uri=%s&response_type=code&client_id=%s' %(callback_url,app_key)
    
    def Work(self,appKey,appSecrect,userName,userScrect,Callback):
        token = None
        for i in range(self.config['RETRY_COUNT']):
            time.sleep(self.config['SLEEP_TIME'])
            token = self.getToken(userName, userScrect, appKey, appSecrect, Callback)
            if token == None:
                continue
            else:
                break
        return token
            
    def escape(self,s):
        """Escape a URL including any /."""
        return urllib.quote(s, safe='~')
    
if __name__ == '__main__':
    tk = TokenGet()
    # app_key # 2425731282 # app_screct # 687c5985e9a5333164e26676a8181a79 # username # 18704941021 # userserect # bcefjj4455y # callback_url # http://t5.iyuewe.com 

    token  = tk.Work('2421908886', 'eb0412cef4e78aaeefbe567b1b9aafc5', '18704941024', 'yzaceg2334b', 'http://t3.iyuewe.com')
    print token.toString()

    
 
        
        
        
        
