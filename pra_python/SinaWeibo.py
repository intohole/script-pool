#!/usr/bin/env python
# -*- coding: utf-8 -*-  


from urllib2 import Request, urlopen
import urllib
import httplib
class sinaWeibo:
    OAUTH_HOST = 'api.weibo.com'
    OAUTH_ROOT = '/oauth2/'
    def __init__(self):
        print "__init__"
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

            parameters = {
                'client_id': app_key,
                'client_secret': app_secret,
                'grant_type': 'authorization_code',
                'redirect_uri':callback,
                'code': code
                }
            resp = urlopen(Request(url, data=self.to_postdata(parameters)))
            data = resp.read()
            print data
            r = self.import_simplejson().loads(str(data))
            print r

            access_token = r['access_token']
            
            return access_token
        except Exception, e:
            print e
    def _get_oauth_url(self, endpoint):
#        if self.secure:
#            prefix = 'https://'
#        else:
        prefix = 'https://'
        return prefix + self.OAUTH_HOST + self.OAUTH_ROOT + endpoint
    
    def to_postdata(self,parameters):
        """Serialize as post data for a POST request."""
        return '&'.join(['%s=%s' % (escape(str(k)), escape(str(v))) \
            for k, v in parameters.iteritems()])
    def getToken(self,userid,userserect,app_key,app_screct,callback_url):
        print userid
        conn = httplib.HTTPSConnection('api.weibo.com')
        postdata = urllib.urlencode({'client_id':app_key,'response_type':'code','redirect_uri':callback_url,\
                                     'action':'submit','userId':userid,'passwd':userserect,\
                                     'isLoginSina':0,'from':'','regCallback':'','state':'','ticket':'','withOfficalFlag':0})
        print postdata
        conn.request('POST','/oauth2/authorize',postdata,{'Referer':self.get_code_url(),'Content-Type': 'application/x-www-form-urlencoded'})
        res = conn.getresponse()
#        page = res.read()
        print 'msg===========',res.msg
        data=res.msg 
        print data['Location']
        self.get_access_token(app_key,app_screct,callback_url,data['Location'].split('=')[1])
 
    def get_code_url(self,app_key,callback_url):
        return 'https://api.weibo.com/oauth2/authorize?redirect_uri=%s&response_type=code&client_id=%s' %(callback_url,app_key)
def escape(s):
    """Escape a URL including any /."""
    return urllib.quote(s, safe='~')

sina = sinaWeibo()
print sina.getToken('weidouwangluo4@126.com','weidou','3425828621','47951158a63baf53200fb37f8d24fc6e','http://www.hutouxie.com') 
    
    
        
        
        
        
