#!/usr/bin/python
# -*- coding: UTF-8 -*-

import urllib2
import threading
import time

exitFlag = 0


class myThread(threading.Thread):
    def __init__(self, threadID, name, url, count, i, k, pic_count):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.url = url
        self.count = count
        self.i = i
        self.k = k
        self.pic_count = pic_count
        self.thread_stop = False

    def run(self):
        print "Starting " + self.name
        # print_time(self,self.name, self.count, 2)
        downloadPic(self, self.url, self.count, self.i, self.k, self.pic_count)
        print "Exiting " + self.name

    def stop(self):
        self.thread_stop = True


def print_time(thread, threadName, delay, counter):
    while counter >= 0:
        if counter == 0:
            thread.stop()
        time.sleep(delay)
        print "%s: %s" % (threadName, time.ctime(time.time()))
        counter -= 1


def downloadPic(thread, url, count, i, k, pic_count):
    pic = urllib2.urlopen(url)
    buf = pic.read()
    f = open(
        'F:\sexy\mmrentiyishu' + '/' + str(i) + '_' + str(k + 1) + '_' + str(pic_count) + '_' + str(count) + '.jpg',
        "wb")
    f.write(buf)
    f.close()
    print "page  %d de di  %d pic list de di %d pic craw sucess" % (i, k + 1, pic_count)
    print (count)
    thread.stop()
