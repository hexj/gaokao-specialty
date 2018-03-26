#!/usr/bin/env python
#-*-coding:utf-8-*-

from bs4 import BeautifulSoup
import downloader
import time
from lxml import etree
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def get_specialty(html):



    selector = etree.HTML(html)
    code_xpath = ".//*[@id='seachtab']/tbody/tr[{}]/td[{}]"
    spe_xpath = ".//*[@id='seachtab']/tbody/tr[{}]/td[{}]/div/a"
    specialty_code_spe_dict = {}
    specialty_code_url_dict = {}

    for tr_num in range(1,287): #1-286
        td_nums= [2,5]
        if tr_num in [13,38,56,103,131,135,146,234,254,284]:
            continue
        if tr_num in [1,14,39,57,104,132,136,147,235,255,285]: #first line
            td_nums = [3,6]

        if tr_num in [37,102,130,145,253]:#last line but only one
            td_nums = [2]

        for td_num in td_nums:
            try:
                code = selector.xpath(code_xpath.format(str(tr_num),str(td_num)))[0].text.split()[0]
                spe = selector.xpath(spe_xpath.format(str(tr_num),str(td_num-1)))[0].text.split()[0]
                url = selector.xpath(spe_xpath.format(str(tr_num),str(td_num-1)))[0].get('href')
            except IndexError,e:
                print tr_num,td_num
            
            specialty_code_spe_dict[code] = spe
            specialty_code_url_dict[code] = url



    return specialty_code_spe_dict,specialty_code_url_dict


def get_specialtyDetail(html):
    detail = {}
    soup = BeautifulSoup(html,"html.parser")
    text = str(soup.select('div[class="li-majorMess"]')[0].text)
    # subject_index = text.find('学科：') # -1 not found
    # class_index = text.find('门类：')
    # name_index = text.find('专业名称：')
    # target_index = text.find('业务培养目标：')
    

    # detail['subject'] = text[subject_index+9:class_index-8] if not subject_index == -1 and not class_index == -1 else ''
    # detail['class'] = text[class_index+9:name_index-8] if not class_index == -1 and not name_index == -1 else ''
    # detail['name'] = text[name_index+15:target_index-10] if not name_index == -1 and not target_index == -1 else ''
    # detail['intro'] = text[target_index:] if not target_index == -1 else text

    return  text
