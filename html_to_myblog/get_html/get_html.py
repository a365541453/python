#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import shutil

dir = '../html_folder/'

list = os.listdir(dir)

html_file = []
html_dir_list = []

for i in range(0,len(list)):
    path = os.path.join(dir,list[i])

    if os.path.isfile(path) and str(path).find('html'):
        html_file.append(path)


    if os.path.isdir(path):
        html_dir_list.append(path)


for dir in html_dir_list:
    new_dir = r'F:\github\django\django\blog\static\upload\kindeditor'
    shutil.move(dir,new_dir)


html_file_list = html_file