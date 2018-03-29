#!/usr/bin/env python  
# encoding: utf-8
# @Author    : w2n1ck
# @Time      : 2018/3/9 下午6:27
# @Introduce : 乌云字典

'''
获取一份乌云漏洞目录字典

爬取来源：
https://wooyun.shuimugan.com/bug/view?bug_no=1

乌云爬虫
获取所有漏洞的漏洞详情中的地址
根据地址，得到路径字典
'''

import re
import threading

import gevent
import requests
from gevent import monkey, pool
from lxml import etree

from wooyunDic.getPathDic import iterate_path
monkey.patch_all()
import multiprocessing

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import ssl
try:
    _create_unverified_https_context = ssl._create_unverified_context  # 忽略证书错误
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:52.0) Gecko/20100101 Firefox/52.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
    "Upgrade-Insecure-Requests": "1",
    "Content-Type": "application/x-www-form-urlencoded"
}
timeout = 3
NUM = 230305

def download2parser(bugURL):
    try:
        res = requests.get(bugURL, timeout=timeout, headers=headers, allow_redirects=False)
        res_code = res.status_code
        res_content = res.content
        # print len(res_content)
        if res_code == 200:
            html = etree.HTML(res_content, parser=etree.HTMLParser(encoding='utf-8'))
            # _xpath = '//*[@id="w0"]/tr[21]/td/fieldset//text()'
            # ((http|ftp|https)://)?[-A-Za-z0-9+&@#/%?=~_|!:,.;]+[-A-Za-z0-9+&@#/%=~_|]
            _xpath = '//*[@id="w0"]/tr[21]/td//text()'
            result = html.xpath(_xpath)
            r = re.compile(r'(?i)\b((?:[a-z][\w-]+:(?:/{1,3}|[a-z0-9%])|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:\'".,<>?«»“”‘’]))')
            # print len(result), type(result)
            for i in range(len(result)):
                _list_content = result[i]
                # print i, _list_content
                flag = r.findall(_list_content)
                _a = '('
                _b = ')'
                if _a in flag or _b in flag:
                    return
                else:
                    for i in range(len(flag)):
                        try:
                            _flag = flag[i][0]
                            if len(_flag) == 0:
                                pass
                            else:
                                __ = iterate_path(_flag)
                                writeFile(__)
                        except:
                            pass
    except Exception:
        pass

def writeFile(str):
    with open('./dicc.txt', 'a+') as f:
        f.write('%s\n' % str)


if __name__ == '__main__':
    with open('./url.txt', 'r') as f:
        while True:
            link  = f.readline()
            if link:
                try:
                    print link
                    threadNum = 150
                    thread_arr = []
                    for i in range(threadNum):
                        t = threading.Thread(target=download2parser, args=(link,))
                        t.daemon = True
                        thread_arr.append(t)
                        for t in thread_arr:
                            t.start()
                        for t in thread_arr:
                            t.join()
                except Exception:
                    pass