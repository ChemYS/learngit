        
#多进程但没有顺序

from netmiko import ConnectHandler
import time
import getpass
import sys
import os
from multiprocessing import Pool
from termcolor import colored

start_time=time.time()
ip_file = sys.argv[1]  #python3.8 test.py ip 3750.txt cmd 3750.txt #sys.argv[0] 指文件名，[1]后面携带的参数
log3 = open(r"D:\Python_script\test\log3.txt",mode="a",encoding="utf-8")
iplist =open(ip_file, 'r')
'''
a=[]
for y in iplist:
    a.append(y)
'''
def login_device(ip,*cmd):
    huawei={
    'device_type':'huawei',
    'host': ip,
    'username':'admin',
    #'password':'Huawei12#$'#FT
    'password':'zsyyNS@2023'
    #'username':'python',#ensp测试
    #'password':'Huawei@123'#ensp测试
    }
    huawei_connect=ConnectHandler(**huawei)
    time.sleep(2)
    print("You have successfully connect to", ip)
    print("You have successfully connect to", ip,file = log3)
    result=huawei_connect.send_config_set(cmd,enter_config_mode=False)
    print(result,file = log3)
    huawei_connect.disconnect()
if __name__ == '__main__':
    print(f"程序于{time.strftime('%X')}开始执行")
    p = Pool(20)
    for i in iplist:
        #ip1 = a[i]
        #test = p.apply_async(login_device,args=(ip1,'screen-length 0 temporary','dis lldp nei bri'))
        test = p.apply_async(login_device,args=(i,'screen-length 0 temporary','dis lldp nei bri'))
    p.close()
    p.join()
    iplist.close()
    print( '总共运行了%d second' %(time.time()-start_time))
    print (f"程序于{time.strftime('%X')}执行结束")
'''
& C:/Users/ChemYS/AppData/Local/Programs/Python/Python311/python.exe d:/Python_script/test/test3.py d:/Python_script/test/ip_list3.txt d:/Python_script/test/cmd_list3.txt
'''