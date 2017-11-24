#!/usr/bin/env python
# -*- coding: utf-8 -*-

from html.parser import HTMLParser
import re
from get_html import get_html
import sqlite3


class my_html(HTMLParser):
    def handle_starttag(self, tag, attrs):
        # print("start:",tag)
        if tag == 'img':  # attrs是list，list里面放tuple，tuple（name，value）
            for name, value in attrs:
                if name == 'src':
                    place_list.append(value)
                    # 把匹配到需要更换图片的路径放进列表里

for file in get_html.html_file_list:  # 遍历html文件列表
    htmlfile = open(file,'r',encoding='utf-8')
    str_html = htmlfile.read()  # 将文件以str的类型读取出来
    htmlfile.close()

    str_html_copy = str_html
    # 因为HTMLParser转换出来的路径是tuple类型，
    # tuple类型的值不能修改
    # 所以复制一份出来，用来在后面步骤中进行str的替换操作
    place_list = []
    # 用来存放需要更换的路径名称

    a = my_html()
    a.feed(str_html)

    for place in place_list:  # 遍历需要更换的图片地址
        new_place = '/static/upload/kindeditor/'+place
        str_html_copy = str_html_copy.replace(place, new_place)


    str_html_copy = re.search(r'<body>(.|\n)*</body>',str_html_copy).group()
    #寻找body之间的部分

    str_html_copy = str_html_copy.replace(r'<body>','')
    str_html_copy = str_html_copy.replace(r'</body>', '')
    #删除body头

    ###################################写入数据文件######################################
    db_file = 'C:\\Users\\Administrator\\Desktop\\db.sqlite3'
    #db = sqlite3.connect(db_file)
    db_tables = 'linux_part_linux_article'

    ###插入数据
    title = file.split('/')[2].split('.')[0]
    type = 5
    time = '2017-11-24'
    text = '222222222'
    sql = 'INSERT INTO %s (title,type,time,text) VALUES (%s,%s,%s,%s)'%(db_tables, title, type, time, text)
    print(sql)
    exit()

    db.execute(sql)
    db.commit()
    db.close()




