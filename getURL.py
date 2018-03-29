#!/usr/bin/env python  
# encoding: utf-8 
# @Author    : w2n1ck
# @Time      : 2018/3/11 下午2:57
# @Introduce : 获取所有可用bugurl

import sys
import requests
import gevent
import time
from gevent import monkey, pool
monkey.patch_all()

reload(sys)
sys.setdefaultencoding('utf8')

import ssl
try:
    _create_unverified_https_context = ssl._create_unverified_context  # 忽略证书错误
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

timeout = 10
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:52.0) Gecko/20100101 Firefox/52.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
    "Upgrade-Insecure-Requests": "1",
    "Content-Type": "application/x-www-form-urlencoded"
}

NUM = 230305
url = 'https://wooyun.shuimugan.com/bug/view?bug_no='

def getURL(url):
    try:
        r = requests.get(url, timeout=timeout, headers=headers, allow_redirects=False)
        code =r.status_code
        if code == 200:
            print url
            with open('./url.txt', 'a+') as f:
                f.write('%s\n' % url)
    except Exception,e:
        print e

if __name__ == '__main__':
    timestart = time.time()
    jobs = []
    links = []
    p = pool.Pool(150)
    for i in range(NUM):
        _url = url + str(i)
        jobs.append(p.spawn(getURL, _url))
    gevent.joinall(jobs)
    timeend = time.time()
    _time = timeend - timestart
    print _time