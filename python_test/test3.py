        
#多进程但没有顺序

from netmiko import ConnectHandler
import time
import getpass
import sys
import os
from multiprocessing import Pool
from termcolor import colored
import pandas as pd

start_time=time.time()
device_list = pd.read_csv(r"C:\Users\ChemYS\learngit\python_test\W_IP_LIST.csv")  #中文会有错误
#ip_file = sys.argv[1]  #python3.8 test.py ip 3750.txt cmd 3750.txt #sys.argv[0] 指文件名，[1]后面携带的参数
log3 = open(r"C:\Users\ChemYS\learngit\python_test\log3.txt",mode="a",encoding="utf-8")
#iplist =open(ip_file, 'r')
'''
a=[]
for y in iplist:
    a.append(y)
'''
def login_device(ip,username,password,*cmd):
    huawei={
    'device_type':'huawei',
    'host': ip,
    'username':username,
    'password':password
    }
    huawei_connect=ConnectHandler(**huawei)
    time.sleep(1)
    print("You have successfully connect to", ip)
    print("You have successfully connect to", ip,file = log3)
    result=huawei_connect.send_config_set(cmd,enter_config_mode=False)
    print(result.split("lldp nei bri")[1].split("<")[1],file = log3)
    print(result.split("lldp nei bri")[1],file = log3)
    huawei_connect.disconnect()
if __name__ == '__main__':
    print(f"程序于{time.strftime('%X')}开始执行")
    p = Pool(1)
    for index,row in device_list.iterrows():
        ip = row['ip']
        username = row['username']
        password = row['password']
        test = p.apply_async(login_device,args=(ip,username,password,'screen-length 0 temporary','dis lldp nei bri'))
    p.close()
    p.join()
    #iplist.close()
    print( '总共运行了%d second' %(time.time()-start_time))
    print (f"程序于{time.strftime('%X')}执行结束")
'''
& C:/Users/ChemYS/AppData/Local/Programs/Python/Python311/python.exe c:/Users/ChemYS/learngit/python_test/test3.py c:/Users/ChemYS/learngit/python_test/ip_list3.txt
'''