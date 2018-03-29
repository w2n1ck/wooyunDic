#!/usr/bin/env python  
# encoding: utf-8
# @Author    : w2n1ck
# @Time      : 2018/3/12 下午8:11
# @Introduce : 简单处理re匹配结果

import urlparse

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def iterate_path(ori_str):
    # parser = urlparse.urlparse(ori_str)
    # _path_list = parser.path.replace('//', '/').strip('/').split('/')
    # print _path_list
    _ans_list = set()
    _ans_list.add(ori_str)
    _ans_list = list(_ans_list)
    for i in range(len(_ans_list)):
        p = urlparse.urlparse(_ans_list[i])
        return urlparse.urlunsplit(['', '', p.path, p.query, p.fragment])

print iterate_path('http:///pic.asp?id=454')