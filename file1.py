#!/usr/bin/python
#-*-coding:utf-8-*-       #指定编码格式，python默认unicode编码
 
import os
directory = "./dir"
os.chdir(directory)  #切换到directory目录
cwd = os.getcwd()  #获取当前目录即dir目录下
print("------------------------current working directory------------------")
 
def deleteBySize(minSize):
    """删除小于minSize的文件（单位：K）"""
    files = os.listdir(os.getcwd())  #列出目录下的文件
    for file in files:
        if os.path.getsize(file) < minSize * 1000:
            os.remove(file)    #删除文件
            print(file + " deleted")
    return
 
def deleteNullFile():
    '''删除所有大小为0的文件'''
    files = os.listdir(os.getcwd())
    for file in files:
        if os.path.getsize(file)  == 0:   #获取文件大小
            os.remove(file)
            print(file + " deleted.")
    return
 
def create():
    '''根据本地时间创建新文件，如果已存在则不创建'''
    import time
    t = time.strftime('%Y-%m-%d',time.localtime())  #将指定格式的当前时间以字符串输出
    suffix = ".docx"
    newfile= t+suffix
    if not os.path.exists(newfile):
        f = open(newfile,'w')
        print newfile
        f.close()
        print newfile + " created."
    else:
        print newfile + " already existed."
    return


hint = '''
funtion:
create new file
delete null file
delete by size
please input number:
'''
while True:
    option = raw_input(hint)  #获取IO输入的值
    if cmp(option,'1') == 0:
        create()
    elif cmp(option,'2') == 0:
        deleteNullFile()
    elif cmp(option,'3') == 0:
        minSize = raw_input("minSize(K):")
        deleteBySize(minSize)
    elif cmp(option,'q') == 0:
        print "quit !"
        break
    else:
        print ("disabled input ,please try again....")