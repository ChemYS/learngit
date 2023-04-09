#链接需要等待 不然命令不完整   
#多进程
import paramiko
import time
import getpass
import sys

username = input('username:')
password = getpass.getpass ('password:')
ip_file = sys.argv[1]  #python3.8 test.py ip 3750.txt cmd 3750.txt #sys.argv[0] 指文件名，[1]后面携带的参数
cmd_file= sys.argv[2]
iplist=open(ip_file, 'r')
for line in iplist.readlines():
    ip=line.strip()
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname=ip,username=username,password=password)
    #time.sleep(1)
    log = open(r"C:\Users\ChemYS\learngit\python_test\log1.txt",mode="a",encoding="utf-8")
    print("You have successfully connect to", ip,file = log)
    command= ssh_client.invoke_shell()
    cmdlist =open(cmd_file, 'r')
    cmdlist.seek(0)
    for line in cmdlist.readlines():
        command.send(line+"\n")
        time.sleep(1)
        cmdlist.close()
    output = command.recv(65535)
    print (output.decode("ascii"),file = log)
    log.close()
    iplist.close()
    ssh_client.close


'''
& C:/Users/ChemYS/AppData/Local/Programs/Python/Python311/python.exe c:/Users/ChemYS/learngit/python_test/test.py c:/Users/ChemYS/learngit/python_test/ip_list1.txt c:/Users/ChemYS/learngit/python_test/cmd_list1.txt
'''