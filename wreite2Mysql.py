#!/usr/bin/env python  
# encoding: utf-8
# @Author    : w2n1ck
# @Time      : 2018/3/9 下午6:27
# @Introduce : 数据库操作
import pymysql

def wreite2Mysql():

    host = '127.0.0.1'
    username = 'root'
    password = '123456'
    db_name = 'wooyun'

    create_table_sql = "CREATE TABLE dicc(id INT AUTO_INCREMENT PRIMARY KEY, bugid INT(255) NOT NULL, urls VARCHAR(255))"

    insert_table_sql = "INSERT INTO dicc(bugid, urls) VALUES({0}, '{1}')"

    query_table_sql = "SELECT id, bugid, urls FROM dicc "

    delete_table_sql = "DELETE FROM dicc "

    drop_table_sql = "DROP TABLE dicc"

    connection = pymysql.connect(host=host,
                                 user=username,
                                 password=password,
                                 charset='utf8mb4',
                                 db=db_name)
    try:
        with connection.cursor() as cursor:
            # cursor.execute(create_table_sql)
            # connection.commit()
            # 插入数据
            sql_lines = []
            for bugID in range(100435):
                with open('./dicc6.txt', 'r') as f:
                    url = f.readline()
                    sql_lines.append([bugID, url.strip()])
            print len(sql_lines)
            for i in range(len(sql_lines)):
                _bugID = sql_lines[i][0]
                _url = str(sql_lines[i][1])
                print _bugID, _url
                _insert_table_sql = insert_table_sql.format(_bugID,_url)
                print _insert_table_sql
                cursor.execute(_insert_table_sql)
            # cursor.execute(insert_table_sql.format(bugID, _urls))
            connection.commit()

            # 查询数据
            cursor.execute(query_table_sql)
            results = cursor.fetchall()
            print(u'id\tbugid\turls')
            '''
            for row in results:
                print(row[0], row[1], row[2], row[3])
                # 清除数据
                cursor.execute(delete_table_sql)
                connection.commit()

                # 删除表
                # cursor.execute(drop_table_sql)
                # connection.commit()
            '''
    except:
        pass

    finally:
        connection.close()

wreite2Mysql()