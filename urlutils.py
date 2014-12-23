#coding=utf-8


# import re

import urlparse




# __domain_reg = re.compile("(?<=//|)((\\w)+(\\.cn|\\.com.cn|\\.org.cn|\\.com|\\.net|\\.org|\\.cc|\\.biz|\\.uk|\\.info|\\.in|\\.eu))+")

def get_url_domain( url):
    if url and isinstance(url , (str , unicode)):
        class URL:
            
            def __init__(self , url):
                self.__url = urlparse.urldefrag(url)
            
            
            def get_domain(self):
                return self.__url['net_loc']
            
            def get_url(self):
                return self.__url.geturl()
            
            def get_port(self):
                return self.__url.port
            
            def get_scheme(self):
                return self.__url.scheme
            
            def get_net_loc(self):
                return self.__url.netloc
        return URL(url)
    return None
    



if __name__ == '__main__':
    from urlparse import urljoin
    print urljoin('http://www.36kr.com/' , '/p/215051.html')
    
    
