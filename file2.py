#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import json
import re
'''
本程序旨在将练习基础知识部分，包括：
列表，元组，字典，文件，函数，字符串等知识
实现的功能：
1.查询
2.删除
3.更改G
4.增加
'''

#定义的文档存储格式
mes_style = '''bankend    www.baidu.org
           server 192.168.50.21   wight 100   maxconn 300
bankend    www.oldboy.org
           server 192.168.99.31   wight 50   maxconn 100\n
'''

#用户只能修改这些字段的值
updateable ={
    1:"server",
    2:"wight",
    3:"maxconn"
}

#菜单
menu_info = '''
1.查询
2.删除
3.修改
4.添加
5.退出
'''



#展示菜单
def show_menu():
    '''
    to display the menu ,I chosed the str to show it

    '''
    print(menu_info)

#初始化操作，往文件里边添加格式文件
def before_start():
    '''
    before start,you can call this func to create a file
    and then you should explanatory(注释) this method before calling
    the main method
    '''
    f = open("web.property","a+",encoding="utf-8")
    for i in mes_style:
        f.writelines(i)
    f.close()
#before_start()
#查询记录
def search(user_enter):
    '''
    this function can be used when search function needed
   user can select the listed item and then,the corresponding
   entry will be display
    '''
    #查询并打印出用户查询关键字所在的行和下一行
    f = open("web.property","r",encoding="utf-8")
    list = f.readlines()
    for i,line in enumerate(list):
        if user_enter in line:
            print(line)
            print(list[i+1])
        elif i == len(list)-1:
            print("查无结果")
    f.close()

#查出所有的文件内容，并包装成字典返回
def searchall():
    '''
    this function is a common function ,it can used in delete and update,so add
    '''
    f = open("web.property", "r", encoding="utf-8")
    list = f.readlines()
    #用来存储找到value为空所对应的key
    list1 =[]
    mapc = {}
    for i,line in enumerate(list):
        if line == "\n" or line == "":
            list.pop(i)
    for i in range(0,len(list),2):
        mapc[int(i/2)+1] =list[i:i+2]
    f.close()
    return mapc
#删除
def delete():
    '''
    this function is used to delete the record user selected
    '''
    flag = True
    while flag:
        maps = searchall()
        for i in maps.items():
            print(i)
        user_selected = input("请选择要删除的对象(输入b返回)：")
        if user_selected.isdigit():
            user_selected = int(user_selected)
            #print(list)
            for j in maps.keys():
                if user_selected == j:
                    temp = j
            for m in maps.items():
                if user_selected == m:
                    temp = m
                    #删除文件中对应的该条记录
                    for line in list(maps.keys()):
                        if temp== line:
                            maps.pop(temp)
                            file_path = "C:/Users/Administrator/PycharmProjects/pythondemo/web.propertybak"
                            if os.path.exists(file_path):
                                os.remove(file_path)
                            os.renames("web.property", "web.propertybak")
                            f6 = open("web.property", "w")
                            for line in maps.values():
                                f6.write(line[0])
                                f6.write(line[1])
                            f6.close()
                            break
                        else:
                            break
                    print(maps)
                    #询问是否继续
                    conti = input("是否继续删除？（y/n）:")
                    if conti == "y":
                        continue
                    else:
                        flag = False
                        break
        elif user_selected == "b":
            break
        else:
            print("输入有错误，请重新选择")


#添加
def add():
    '''
    you can execute add funciton to add a node to file
    but you should according to those forms
    1:"server",
    2:"wight",
    3:"maxconn"
    '''
    #regs ={"bankend":"www.\w.com","server":"\d.\d.\d.\d"}


    while True:
        print("请依次填入下列选项中的值")
        bankend = input("bankend:")
        server = input("server:")
        wight = input("wight:")
        maxconn = input("maxconn:")
        # 正则表达式检查输入是否符合格式要求
        if re.compile(r"www\.(\w+)(\.com|\.cn|\.org|\.net)").match(bankend):
            print("bankend ok")
            if re.compile(r"\d+\.\d+\.\d+\.\d").match(server):
                print("server ok")
                if re.compile(r"\d").match(wight):
                    print("wight ok")
                    if re.compile(r"\d").match(maxconn):
                        print("maxconn ok")
                        #条件都符合
                        write_date =["bankend    %s\n"%bankend,"           server %s   wigth %d   maxconn %d"%(server,int(wight),int(maxconn))]
                        f = open("web.property", "a", encoding="utf-8")
                        for line in write_date:
                            f.writelines(line)
                        f.close()
                        break
                    else:
                        print("maxconn invalid")
                        continue
                else:
                    print("wight invalid")
                    continue
            else:
                print("server invalid")
                continue
        else:
            print("bankend invalid")
            continue


#更新
def update():
    '''
    this function is designed for update the file message,content
    '''
    state = 0
    while True:
        mapa = searchall()
        for i,m in enumerate(mapa):
            print(str(i+1)+"."+str(mapa[m]))
        it = input("请选择要更改的条目:(b 返回)")
        if it.isdigit():
            it = int(it)
            for i in mapa.keys():
                if it == i:
                    print("check pass")
                    while True:
                        for member in updateable:
                            print(str(member)+":"+updateable[member])
                        user_se = input("请选择要修改的字段(按b返回)：")
                        if user_se.isdigit():
                            user_se =int(user_se)
                            for j in updateable.keys():
                                if user_se == j:
                                    print("check pass2")
                                    while True:
                                        update_to = input("请输入值：")
                                        if update_to==None or update_to=="":
                                            pass
                                        else:
                                            break
                                    print(user_se)
                                    #获得选择的字段
                                    map_attr = updateable[user_se]
                                    li =[]
                                    for  l in mapa[it]:
                                        if map_attr in l:
                                            li.append(l.split("   "))
                                        print(l)
                                    #print(li)
                                    for i,ind in enumerate(li[0]):
                                        if(map_attr in ind and map_attr == "server"):
                                            ind = "           "+map_attr+" "+(str(update_to) if update_to.isdigit() else update_to)
                                        elif (map_attr in ind ):
                                            ind = "  " + map_attr + " " + (str(update_to) if update_to.isdigit()  else update_to)
                                            li[0][i]=ind
                                            break
                                    #同步到mapa
                                    final_str =""
                                    for i in li[0]:
                                        if "server" in i:
                                            final_str += "          "+i+"   "
                                        elif "wight" in i:
                                            final_str +=i+"   "
                                        else:
                                            final_str += i
                                    #print(final_str)
                                    for i,n in enumerate(mapa[it]):
                                        if "server" in n:
                                            mapa[it][i] =final_str+"\n"
                                    print(mapa)
                                    with open("web.property","w") as f:
                                        for line in mapa.values():
                                            f.writelines(line)
                                    f.close()
                                    print(mapa)
                                    print(li)
                                    print("修改成功")
                                    break
                                elif j == len(updateable):
                                    print("不在选项内，请重新选择")
                        elif user_se == "b":
                            break
                elif i ==len(mapa):
                    print("输入选项不在列表中，请重新选择")
        elif it == "b":
            state = 1
            break
        else:
            print("输入有误")
    if state == 1:
        return

#主程序
while True:
    show_menu()
    selected = input("请选择:(1,2，3，4，5):")
    if selected.isdigit():
        selected = int(selected)
        if selected == 1:
            search(input("请输入要查询的网址："))
        if selected == 2:
            delete()
        if selected == 3:
            update()
        if selected == 4:
            add()
        if selected == 5:
            break
    else:
        print("你输入了其他字符，请输入数字")
        continue