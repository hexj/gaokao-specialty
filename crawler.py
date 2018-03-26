#!/usr/bin/env python
#-*-coding:utf-8-*-

import controler
import downloader
import pageparser
import time
import sqlite3
import string
import os
import sys
reload(sys)
sys.setdefaultencoding('utf8')


main_url = 'http://gkcx.eol.cn'




def main(entrance):
    
    print "entrance:{}".format(entrance)

    entrance_html = downloader.get_html(entrance)
    specialty_code_spe_dict,specialty_code_url_dict = pageparser.get_specialty(entrance_html)
    for code in specialty_code_url_dict:
        title = specialty_code_spe_dict[code]
        url = specialty_code_url_dict[code]
        print title,code,url
        

        spe_url = main_url + url
        spe_html = downloader.get_html(spe_url)
        intro = pageparser.get_specialtyDetail(spe_html)

        # subject = detail['subject']
        # class_ = detail['class']
        # name = detail['name']
        # intro = detail['intro']        
        

        controler.write_data(title, code, intro)
        # print 'title:{},code:{},subject:{},class:{},name:{},intro:{}'.format(title, code,subject, class_, name, intro)



if __name__ == '__main__':
    main('http://gkcx.eol.cn/schoolhtm/specialty/10032/list.htm')
