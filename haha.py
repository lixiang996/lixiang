#!/usr/bin/python
# -*- coding: UTF-8 -*-

f = open('hahaaaaa.txt','w')
print('文件名称',f.name)
seq = ['这是第一段\n','这是第二段']
f.writelines(seq)
f.close()