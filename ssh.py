#!/usr/bin/env python
# -*- coding: utf8 -*-

import paramiko,getpass  #getpass是隐藏密码

def ssh_connect(password):
    host_ip = '192.168.0.150'
    user_name = 'root'
    host_port ='22'

    # 待执行的命令
    blk_command = "blkid"
    ls_command = "ls /root"

    # 注意：依次执行多条命令时，命令之间用分号隔开
    command = sed_command+";"+ls_command

    # SSH远程连接
    ssh = paramiko.SSHClient()   #创建sshclient
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  #指定当对方主机没有本机公钥的情况时应该怎么办，AutoAddPolicy表示自动在对方主机保存下本机的秘钥
    ssh.connect(host_ip, host_port, user_name, password)

    # 执行命令并获取执行结果
    stdin, stdout, stderr = ssh.exec_command(command)
    out = stdout.readlines()
    err = stderr.readlines()
    
    ssh.close()

    return out,err

if __name__ == '__main__':
    pwd = getpass.getpass("请输入密码：")
    result = ssh_connect(pwd)
    print(result)