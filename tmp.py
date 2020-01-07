#!/usr/bin/python
# -*- coding: utf-8  -*-

import os
dir = "./"
os.chdir(dir)
cwd = os.getcwd()

def del_by_size(minzize):
    dir_list = os.listdir(cwd)
    for file in dir_list:
        if os.path.getsize(fize) <= 10*minzize:
            os.remove(file)
            print('deleted: ' + file)
    return
def del_null():
    dir_list = os.listdir(cwd)
    for file in dir_list:
        if os.path.getsize(file) == 0:
            os.remove(file)
            print('deleted' + file)
    return
def creat():
    import time
    t = time.strftime('%Y-%m-%d',time.localtime())
    suf = '.docx'
    newfile = t+suf
    if not os.path.exists(file):
        f = open(newfile,'w')
        seq = ['diyihang\n','di2hang']
        f.writelines(seq)
        print(newfile)
        f.close()
        print(file +'created')
    else:
        print(file + 'already exist')
    return



