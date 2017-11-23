#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os


dir = '../html_folder/'

list = os.listdir(dir)
html_file_list = []

for i in range(0,len(list)):
    path = os.path.join(dir,list[i])
    if os.path.isfile(path) and str(path).find('html'):
        html_file_list.append(path)
