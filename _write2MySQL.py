#!/usr/bin/env python  
# encoding: utf-8 
# @Author    : w2n1ck
# @Time      : 2018/3/28 下午2:00
# @Introduce : 数据库操作


def subReplace_4():
    with open('./dicc7.txt', 'r') as f1:
        while True:
            link  = f1.readline().strip()
            try:
                if link.startswith('/'):
                    with open('./dicc8.txt', 'a+') as f2:
                        f2.write('%s\n' % link.strip())
                else:
                    print link
            except:
                pass

subReplace_4()
'''
def wreite2Mysql():

    host = '127.0.0.1'
    username = 'root'
    password = '123456'
    db_name = 'wooyun'

    insert_table_sql = "INSERT INTO dicc2(urls) VALUES('{0}')"

    connection = pymysql.connect(host=host,
                                 user=username,
                                 password=password,
                                 charset='utf8mb4',
                                 db=db_name)
    try:
        with connection.cursor() as cursor:
            # 插入数据
            sql_lines = []
            with open('./dicc7.txt', 'r') as f:
                while True:
                    _url = f.readline().strip()
                    if _url:
                        print _url
                    else:
                        pass
    except:
        pass

    finally:
        connection.close()

wreite2Mysql()
'''