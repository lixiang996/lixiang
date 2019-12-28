#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
def file_handler(backend_data,res = None,type = 'fetch'):   #文件处理函数
    if type == 'fetch':   #查询操作
        with open('haproxy.conf','r') as read_f:
            tag = False           #初始状态标识
            ret = []              #用于放置查询结果
            for read_line in read_f:
                if read_line.strip() == backend_data:  #用strip()去除读取的末尾回车、空格
                    tag = True
                    continue  #查询到需要查询的数据则继续执行下次循环
                if tag and read_line.startswith('backend'):break #防止跳到下一条记录（以backend开头的）
                if tag:
                    print(read_line, end = '')
                    ret.append(read_line)
            else:
                print('未查询到你所要找的记录！')
        return ret
    elif type == 'change':
        with open('haproxy.conf','r') as read_f,\
            open('haproxy.conf_new','w') as write_f: #因为文件没有修改一说，所以相当于创建副本
            tag = False  #状态标识
            has_write = False  #用于标记已经写入的内容
            for read_line in read_f:
                if read_line.strip() == backend_data:
                    tag = True
                    write_f.write('%s\n'%backend_data)   #写入需要修改的backend标题
                    continue
                if tag and read_line.startswith('backend'): #防止跳到下一条记录（以backend开头的）
                    tag = False  #遇到其他backend记录，不会出现修改
                if not tag:   #尚未读取到需要修改的部分，则直接读写
                    write_f.write(read_line)
                else:
                    if not has_write:
                        for record in res:
                            write_f.write(record)
                        has_write = True   #将修改的内容全部写好，则改变已经写入的状态
        os.rename('haproxy.conf','haproxy.conf.bak')  #将原文件备份为备份文件
        os.rename('haproxy.conf_new','haproxy.conf')  #覆盖原文件
def fetch(data): #查询
    print('查询的数据为：%s'%data)
    backend_data = 'backend %s' %data         #拼接出关键词
    return file_handler(backend_data)


def add(data): #添加
    pass
def change(data): #修改
    backend = data[0]['backend']  #文件中的一条记录www.oldboy1.org，需要修改，先执行查找，如果没有，则不能修改
    backend_data = 'backend %s'%backend   #backend www.oldboy1.org
    old_server_record = '%sserver %s weight %s maxconn %s\n'%(
                                                            ' '*8,data[0]['record']['server'],
                                                            data[0]['record']['weight'],
                                                            data[0]['record']['maxconn'],
                                                            )
    new_server_record = '%sserver %s weight %s maxconn %s\n'%(
                                                        ' '*8,data[1]['record']['server'],
                                                        data[1]['record']['weight'],
                                                        data[1]['record']['maxconn'],
                                                        )
    print('用户想要修改的记录是：',old_server_record)
    res = fetch(backend)   #返回指定backend记录的列表
    if not res or old_server_record not in res:  #没找到(1 backend没找到 2 server没找到)
        return '你要修改的记录不存在！'
    else:
        index = res.index(old_server_record)
        res[index] = new_server_record   #获取到修改的值列表
    return file_handler(backend_data,res = res , type = 'change')
def delete(): #删除
    pass


if __name__ == '__main__':   #执行可执行的语句
    msg = '''
        1:查询
        2:添加
        3:修改
        4:删除
        5:退出
    '''
    msg_dic = {
        '1' : fetch,
        '2' : add,
        '3' : change,
        '4' : delete
    }
    while True:
        print(msg)
        choice = input('请输入你的选项：').strip()
        if not choice : continue   #用户输入为空时
        if choice == '5':break     #输入5则退出程序

        if choice != '1':
            data = eval(input('输入数据：').strip())   #有用户输入，并过滤掉前后空格及回车;在修改增加等操作传入的是字典格式
            fetch_res = msg_dic[choice](data)        #根据选项字典获取函数名，加()则运行相关选项函数
        else:
            data = input('输入数据：').strip()  #有用户输入，并过滤掉前后空格及回车;在修改增加等操作传入的是字典格式
            fetch_res = msg_dic[choice](data)        #根据选项字典获取函数名，加()则运行相关选项函数
