#!/usr/bin/env python
# encoding: utf-8
# @Author    : w2n1ck
# @Time      : 2018/3/11 下午6:35
# @Introduce : 线程引擎池

from gevent import monkey, pool
monkey.patch_all()
from wooyun import download2parser

import Queue
import threading
import time

exitFlag = 0

class myThread (threading.Thread):
    def __init__(self, bugurl, q):
        threading.Thread.__init__(self)
        self.bugurl = bugurl
        self.q = q
    def run(self):
        print "Starting " + self.bugurl
        process_data(self.bugurl, self.q)
        print "Exiting " + self.bugurl

def process_data(bugurl,q):
    while not exitFlag:
        queueLock.acquire()
        if not workQueue.empty():
            data = q.get()
            download2parser(data)
            queueLock.release()
        else:
            queueLock.release()
        time.sleep(0.1)

queueLock = threading.Lock()
workQueue = Queue.Queue(100)
threads = []

'''
# 填充队列
queueLock.acquire()
for word in nameList:
    workQueue.put(word)
queueLock.release()

'''

with open('./url-1.txt','r') as f:
    bugurl = f.readlines()
    queueLock.acquire()
    for _ in bugurl:
        workQueue.put(_)
        thread = myThread(_)
        thread.start()
        threads.append(thread)
    queueLock.release()

# 通知线程是时候退出
exitFlag = 1

# 等待所有线程完成
for t in threads:
    t.join()

# 等待队列清空
while not workQueue.empty():
    pass

