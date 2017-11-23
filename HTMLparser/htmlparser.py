#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from html.parser import HTMLParser

htmlfile = open('html/Linux 运维必备的 13 款实用工具,拿好了~.html','r',encoding= 'utf-8')
str_html = htmlfile.read()
htmlfile.close()


class my_html(HTMLParser):
	
	def handle_starttag(self,tag,attrs):
		#print("start:",tag)
		if tag == 'img':  #attrs是list，list里面放tuple，tuple（name，value）
			for name,value in attrs:
				if name == 'src':
					print(value)
					value = '2222222222222222222222222222222'
					print(value)
			print("=========")
		#print("attrs:",attrs)

	#def handle_endtag(self,tag):
		#print("end:",tag)


	#def handle_data(self,data):
		#print("data:",data)


a = my_html()

#print(type(str_html))

#str_html = "<div style='background:1'> div-1div-1div-1div-1 <a>213</a> div-2div-2div-2div-2 </div>"

str_html_copy = str_html

a.feed(str_html_copy)

out_file = open('C:\\Users\\Administrator\\Desktop\\1111.html','w',encoding= 'utf-8')
out_file.write(str_html_copy)
out_file.close()

