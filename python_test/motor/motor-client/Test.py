import  urllib, urllib2, fnmatch
from api.weibo import APIClient # api from:http://michaelliao.github.com/sinaweibopy/
from api.http_helper import *
from api.retry import *


def make_access_token(self,username, password):
        '''请求access token'''

        params = urllib.urlencode({'action':'submit','withOfficalFlag':'0','ticket':'','isLoginSina':'', \
            'response_type':'code', \
            'regCallback':'', \
            'redirect_uri':self.CALLBACK_URL, \
            'client_id':self.APP_KEY, \
            'state':'', \
            'from':'', \
            'userId':username, \
            'passwd':password, \
            })

        login_url = 'https://api.weibo.com/oauth2/authorize'

        url = self.client.get_authorize_url()
        content = urllib2.urlopen(url)
        if content:
            headers = { 'Referer' : url }
            request = urllib2.Request(login_url, params, headers)
            opener = get_opener(False)
            urllib2.install_opener(opener)
            try:
                f = opener.open(request)
                print f.headers.headers
                return_callback_url = f.geturl
                print f.read()
            except urllib2.HTTPError, e:
                return_callback_url = e.geturl()
            # 取到返回的code
            code = return_callback_url.split('=')[1]
        #得到token
        token = self.client.request_access_token(code)
        self.save_access_token(username,token)
        
    