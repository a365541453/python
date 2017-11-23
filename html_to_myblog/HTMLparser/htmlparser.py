#!/usr/bin/env python
# -*- coding: utf-8 -*-

from html.parser import HTMLParser
from get_html import get_html
print('========')
print(type(get_html.html_file_list))
print(get_html.html_file_list)

exit()

htmlfile = open('html/Linux 运维必备的 13 款实用工具,拿好了~.html', 'r', encoding='utf-8')
str_html = htmlfile.read()  # 将文件以str的类型读取出来
htmlfile.close()

##################################以上测试需要########################################

str_html_copy = str_html
# 因为HTMLParser转换出来的路径是tuple类型，
# tuple类型的值不能修改
# 所以复制一份出来，用来在后面步骤中进行str的替换操作

place_list = []
# 用来存放需要更换的路径名称

class my_html(HTMLParser):
    def handle_starttag(self, tag, attrs):
        # print("start:",tag)
        if tag == 'img':  # attrs是list，list里面放tuple，tuple（name，value）
            for name, value in attrs:
                if name == 'src':
                    place_list.append(value)
                    # 把匹配到需要更换图片的路径放进列表里

a = my_html()
a.feed(str_html)

for place in place_list:  # 遍历需要更换的图片地址
    str_html_copy = str_html_copy.replace(place, '2222222') #把22222替换成实际的路径

###################################以下测试需要######################################

out_file = open('C:\\Users\\zwh-pc\\Desktop\\1111.html', 'w', encoding='utf-8')
out_file.write(str_html_copy)
out_file.close()


