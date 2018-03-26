#!/usr/bin/env python
#-*-coding:utf-8-*-

import pymysql
import sys
reload(sys)
sys.setdefaultencoding('utf8')


#用来处理用Python的sqlite3操作数据库要插入的字符串中含有中文字符的时候报错处理，配合map
def _decode_utf8(str):
    try:
        return str.encode('utf-8','ignore').decode('utf-8')
    except UnicodeDecodeError as e:
        return ''.encode('utf-8','ignore').decode('utf-8')


def write_data(title, code, intro):
    '''write_data(dict_jav, uncensored)'''

    conn = pymysql.connect(host='127.0.0.1',port=3306,user='root',passwd='pass',db='edu',charset='utf8')
    cursor = conn.cursor()
    #对数据解码为unicode
    title, code, intro = map(_decode_utf8, (title, code, intro))

    #插入数据
    try:

        cursor.execute("INSERT INTO edu_spider_ch (title, code, intro)VALUES('{}','{}','{}')".format(title, code, intro))
    except Exception as e:
        print e
        pass
    cursor.close()
    conn.commit()
    conn.close()

