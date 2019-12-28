#!/usr/bin env python
#-*- coding: utf8 -*

import paramiko
import getpass
def ssh_connect(pwd):
    ssh_host = ''
    ssh_port = ''
    ssh_user = ''

    ls_command = "ls /root"
    blk_command = "blkid"
    command = ls_command+";"+blk_command

    ssh =  paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ssh_host, ssh_port, ssh_user, pwd)

    stdin, stdout, stderr = ssh.exec_command(command)
    out = stdout.readlines()
    err = stderr.readlines()

    ssh.close()
    return out, err

if __name__ == '__main__':
    pwd = getpass.getpass("input secret:")
    result = ssh_connect(pwd)
    print(result)