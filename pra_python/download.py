#from urllib.request import *
import urllib
from threading import Thread

import os

import time

from datetime import datetime

 

class DownTask(Thread):

    def __init__(self, url, file, start, end):

        Thread.__init__(self)

        self.url = url

        self.startpos = start + file.tell()

        self.endpos = end

        self.file = file

        self.length = self.endpos - self.startpos + 1

        self.nread = 0

        r = urllib.request.Request(url = self.url)

        r.add_header("Range", "bytes=%d-%d"%(self.startpos, self.endpos))

        self.con = urllib.urlopen(r)

        print(self.file.name, "start")

        print("need read %d bytes"%self.length)

        print(self.con.info().as_string())

    def run(self):

        if self.startpos >= self.endpos:

            print(self.file.name, "is already completed")

            return

        while self.nread < self.length:

            nleft = self.length - self.nread

            if nleft > 1024:

                d = self.con.read(1024)

            else:

                d = self.con.read(nleft)

            if d:

                self.nread += len(d)

                self.file.write(d)

                self.file.flush()

            else:

                break

        self.file.flush()

        self.con.close()

        print(self.file.name, "complete len/size:%d/%d, read %d byte"%(self.file.tell(), self.endpos-self.startpos+1, self.nread))

 

 

def download(url, nthread = 4, filename = None):

    if filename is None:

        filename = os.path.split(url)[1]

    con = urllib.urlopen(url)

    #print(con.info().as_string())

    supp = con.headers.get("Accept-Ranges")

    length = int(con.headers.get("Content-length"))

    con.close()

 

    if not supp:

        nthread = 1

    ranges = [0]

    isize = length // nthread

    for i in range(nthread - 1):

        ranges.append((i + 1) * isize)

    ranges.append(length)

 

    print("ranges", ranges)

    files = []

    tasks = []

    for i in range(len(ranges) - 1):

        file = open("%s_part%d"%(filename, i), "ab+")

        files.append(file)

        task = DownTask(url, file, ranges[i], ranges[i + 1] - 1)

        tasks.append(task)

    for t in tasks:

        t.start()

 

    while any(map(lambda t:t.isAlive(), tasks)):

        nread = sum(map(lambda t:t.nread, tasks))

        print("/rcomplete(%%%04.1f) len/size:%d/%d"%(nread * 100.0 / length, nread, length), datetime.now(), "", sys.stdout)

        sys.stdout.flush()

        time.sleep(0.5)

    for t in tasks:

        t.join()

    file = open(filename, "wb")

    for f in files:

        f.seek(0)

        file.write(f.read())

        f.close()

        os.remove(f.name)

    file.flush()

    print(file.name, "complete")

    file.close()

 

 

 

 

 

if __name__ == "__main__":

    url = "http://nchc.dl.sourceforge.net/project/xlslib/xlslib-1.6.0.zip"

    download(url, 4)

 
