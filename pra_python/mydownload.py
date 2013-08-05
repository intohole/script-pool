#coding=utf8
import urllib
from threading import Thread
import os
import re

class DownTask(Thread):
    filenameReg = re.compile(r"\w*.(jpg|gif)")
    
    def __init__(self , url , storeDir):
        Thread.__init__(self)
        self.url = url
        self.storeDir = storeDir
        m = self.filenameReg.search(self.url)
        self.filename = """%s%s""" % (self.storeDir,m.group())
    def run(self):
        if not os.path.exists(self.storeDir):
            os.mkdir(self.storeDir)
        urldata = urllib.urlretrieve(self.url, self.filename)
        print '%s  现在完毕!!!' % self.filename
    def cbk(self,a, b, c):  
        '''''回调函数 
        @a: 已经下载的数据块 
        @b: 数据块的大小 
        @c: 远程文件的大小 
        '''  
        per = 100.0 * a * b / c  
        if per > 100:  
            per = 100  
        print '%.2f%%' % per 

class DownAllJpg(Thread):
    dw_poolUrl = []
    dw_workThread = []
    def __init__(self , jpgdict):
        Thread.__init__(self)
        self.dw_poolUrl = jpgdict
        self.maxThread = 5
    def __init__(self,jpgdict,maxThread,storeDir):
        Thread.__init__(self)
        self.dw_poolUrl = jpgdict
        self.maxThread = maxThread
        self.storeDir = storeDir
    def DownAll(self):
        if len(self.dw_poolUrl) < self.maxThread:
            self.maxThread = len(self.dw_poolUrl)
        for a in range(self.maxThread):
            self.dw_workThread.append(DownTask(self.dw_poolUrl.pop(),self.storeDir))
        for a in range(self.maxThread):
            self.dw_workThread[a].start()
        for a in range(self.maxThread):
            self.dw_workThread[a].join()
    def run(self):
        self.DownAll()
        bNotAll = True
        while bNotAll:
            for a in range(len(self.dw_workThread)):
                if not self.dw_workThread[a].isAlive():
                    del self.dw_workThread[a]
                    if len(self.dw_poolUrl):
                        tmpThread = DownTask(self.dw_poolUrl.pop() ,self.storeDir)
                        tmpThread.start()
                        tmpThread.join()
                        self.dw_workThread.append(tmpThread)
                    break
            if len(self.dw_workThread) == 0:
                bNotAll = False
        print 'finsh all the task'
            
        
class DownJpg(object):
    dw_thread = []
    def __init__(self, jpgdict):
        for k,v in jpgdict.items():
            print k
            self.dw_thread.append(DownTask(k,v))
    def download(self):
        for i in range(len(self.dw_thread)):
            self.dw_thread[i].start()
        for j in range(len(self.dw_thread)):
            self.dw_thread[j].join()
        
if __name__ == "__main__":

   dw = DownTask("http://ww1.sinaimg.cn/large/5e65ed94gw1dlni5yc20fj.jpg","/home/lixuze/11.jpg")
   dw.start()
   dw.join()
