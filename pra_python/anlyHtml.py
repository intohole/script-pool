#!/user/bin/env python
#coding=utf8
import urllib
import re
import os
from mydownload import DownAllJpg


class downHtml:
    webfile = None
    def __init__(self,weburl):
        self.weburl = weburl

    def downloadHtml(self):
        webItem = urllib.urlopen(self.weburl)
        self.webfile = webItem.read()
        webItem.close()
    def getHtmlCode(self):
        if  self.webfile:
            return self.webfile
        else:
            self.downloadHtml()
            return self.webfile

class findJpg:
    jpgContainer = []
    jpgdict = {}
    filenameReg = re.compile(r"\w*.(jpg|gif)")
    
    def __init__(self,htmlCode):
        if len(htmlCode):
            self.htmlCode = htmlCode.getHtmlCode()
            self.jpgReg = re.compile(r"""http://imgsrc\.baidu\.com/forum/pic/item/\w*.jpg""")
    def findJpg(self):
        for p in self.jpgReg.finditer(self.htmlCode):
            self.jpgContainer.append(p.group())
    def getJpgUrl(self):
        if not len(self.jpgContainer):
            self.findJpg()
        return self.jpgContainer
'''
    def splitUrl(self):
        for p in self.jpgContainer:
           m = self.filenameReg.search(p)
            if m:
                self.jpgdict[p] = """%s%s""" %(self.dir,m.group())
'''
class downTB:
    jpgUrl = []
    pageSumReg = re.compile("""all_page_num:[1-9][0-9]*""") 
    def __init__(self , url_ , storeDir ,pageCode = 0 ):
        self.url_ = url_
        self.pageCode = pageCode
        self.storeDir = storeDir
    def work(self):
        ht = downHtml(url_)
        m = None
        if self.pageCode == 0:
            m = self.pageSumReg.match(ht.getHtmlCode())
            if not m:
                print 'wrong'
                return
            self.pageCode = m.group().split(':')[1]
        fg = findJpg(ht)
        self.jpgUrl.extend(fg.getJpgUrl())
        for pc in range(2,self.pageCode):
            newUrl = "%s?pn=%d" % (self.url_,pc)
            tmpDH = downHtml(newUrl)
            tmpfg= findJpg(tmpDH)
            self.jpgUrl.extend(tmpfg.getJpgUrl())
        dw = DownAllJpg(self.jpgUrl,self.storeDir)
        dw.start()
        dw.join()
        
        
    
url_ = str(raw_input('贴吧地址 :').strip())
pageCode = int(raw_input('贴吧页数 :').strip())
dt = downTB(url_ , '/home/lixuze/ssssss/')
dt.work()
'''
ht  = downHtml(url_)
fg = findJpg(ht.getHtmlCode())
dw = DownAllJpg(fg.getJpgUrl(),5,'/home/lixuze/kkkk/')
dw.start()
dw.join()
'''
