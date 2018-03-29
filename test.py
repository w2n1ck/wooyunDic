#!/usr/bin/env python  
# encoding: utf-8 
# @Author    : w2n1ck
# @Time      : 2018/3/22 下午9:21
# @Introduce : 多进程+协程

from multiprocessing import Process, cpu_count, Queue, JoinableQueue
from gevent import monkey; monkey.patch_all();
import gevent
import datetime
from Queue import Empty

import requests

timeout = 5
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:52.0) Gecko/20100101 Firefox/52.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
    "Upgrade-Insecure-Requests": "1",
    "Content-Type": "application/x-www-form-urlencoded"
}

def getURL(url):
    try:
        r = requests.get(url,verify=False, timeout=timeout, headers=headers, allow_redirects=False)
        code =r.status_code
        if code == 200:
            print url
            with open('./url.txt', 'a+') as f:
                f.write('%s\n' % url)
    except Exception,e:
        print e

class Consumer(object):
    def __init__(self, q, no_tasks, name):
        self._no_tasks = no_tasks
        self._queue = q
        self.name = name
        self._rungevent(self._queue, self._no_tasks)

    def _rungevent(self, q, no_tasks):
        jobs = [gevent.spawn(self._printq) for x in xrange(no_tasks)]
        gevent.joinall(jobs)

    def _printq(self):
        while 1:
            value = self._queue.get()
            if value is None:
                self._queue.task_done()
                break
            else:
                print("{0} time: {1}, value: {2}".format(self.name,\
                                 datetime.datetime.now(), value))
        return

class Producer(object):
    def __init__(self, q, num_tasks, name, consumers_tasks):
       print(name)
       self._q = q
       self._num_tasks = num_tasks
       self.name = name
       self.consumer_tasks = consumers_tasks
       self._rungevent()

    def _rungevent(self):
        jobs = [gevent.spawn(self.produce) for x in xrange(self._num_tasks)]
        gevent.joinall(jobs)
        for x in xrange(self.consumer_tasks):
            self._q.put_nowait(None)
        self._q.close()

    def produce(self):
        for num in xrange(10000):
            print num
            self._q.put(num, block = False)
        return

def main():
    total_cores = cpu_count()
    total_processes = total_cores * 2
    q = JoinableQueue()
    print  111
    producer_gevents = 10
    consumer_gevents = 7
    jobs = []
    start = datetime.datetime.now()
    for x in xrange(total_cores):
        if not x % 2 :
            p = Process(target = Producer, args=(q, producer_gevents,"producer %d"%1, consumer_gevents))
            p.start()
            jobs.append(p)
        else:
            p = Process(target = Consumer, args=(q, consumer_gevents,"consumer %d"%x))
            p.start()
            jobs.append(p)

    for job in jobs:
        job.join()

if __name__ == '__main__':
    main()