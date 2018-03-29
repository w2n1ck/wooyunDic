#!/usr/bin/env python
# encoding: utf-8
# @Author    : w2n1ck
# @Time      : 2018/3/9 下午6:27
# @Introduce : 数据处理

import re
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from getPathDic import iterate_path

def subReplace_1(line):
    regex = re.compile(ur"[\u4e00-\u9fa5]")
    _ = regex.sub("\n", line.decode('utf-8'))
    return _

def subReplace_2(line):
    if len(line) == 0 :
        pass
    elif '/' not in str(line) or '.' not in str(line):
        pass
    else:
        print u'正在写入：', line
        with open('./dicc1.txt', 'a+') as f:
            f.write('%s\n' % line)

def subRepalce_3():
    with open('./dicc1.txt', 'r') as f1:
        while True:
            link  = f1.readline().strip()

            if len(link) == 0 :
                pass
            elif '/' not in str(link) or '.' not in str(link):
                pass
            else:
                print u'正在写入：', link
                with open('./dicc2.txt', 'a+') as f2:
                    f2.write('%s\n' % link)

def subReplace_4():
    flag = 126877
    with open('./dicc2.txt', 'r') as f1:
        while flag:
            link  = f1.readline()
            try:
                if link.startswith('http'):
                    _link = iterate_path(link)
                    print u'处理前：', link
                    print u'处理后：', _link
                    with open('./dicc3.txt', 'a+') as f2:
                        f2.write('%s\n' % _link)
                else:
                    print u'未处理：', link
                    with open('./dicc3.txt', 'a+') as f3:
                        f3.write('%s\n' % link)
                flag = flag-1
            except Exception:
                print u'无法处理的url：', link
                with open('./bad_url.txt', 'a+') as f4:
                    f4.write('%s\n' % link)
                pass

def subReplace_5():
    with open('./dicc3.txt', 'r') as f1:
        while True:
            link  = f1.readline().strip()
            if len(link) <= 4 :
                pass
            else:
                print u'正在写入：', link
                with open('./dicc4.txt', 'a+') as f2:
                    f2.write('%s\n' % link)

def subReplace_6():
    with open('./dicc5.txt', 'r') as f1:
        while True:
            link  = f1.readline()
            if 'bugs/' in str(link) or '**' in str(link) or 'tcp' in str(link) or 'jdbc' in str(link) or 'xmlns' in str(link) or '，' in str(link) or 'ldap' in str(link) or 'rl:h' in str(link) or 'ssh://' in str(link) or 'rmi://' in str(link) or 'url-' in str(link) or 'URL:' in str(link) or 'soap:' in str(link) or 't.cn' in str(link) or 'inurl' in str(link) or 'dir:' in str(link) or '【' in str(link) or 'ftp:' in str(link) or 'HTTP/1.1' in str(link) or ':/bin' in str(link) or 'smb:' in str(link) or 'Location:' in str(link):
                print link
            else:
                with open('./dicc6.txt', 'a+') as f2:
                    f2.write('%s' % link)


def _pathParser():
    with open('./dicc.txt', 'r') as f:
        while True:
            link  = f.readline()
            if link:
                try:
                    print u'处理前：', link
                    _ = subReplace_1(link)
                    subReplace_2(_)

                except Exception:
                    pass

# _pathParser()
# subReplace_6()