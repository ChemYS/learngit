        
#多进程但没有顺序

from netmiko import ConnectHandler
import time
import getpass
import sys
import os
from multiprocessing import Pool
from termcolor import colored

start_time=time.time()
ip_file = sys.argv[1]
#rz_file = sys.argv[2]  #python3.8 test.py ip 3750.txt cmd 3750.txt #sys.argv[0] 指文件名，[1]后面携带的参数
log7 = open(r"D:\Python_script\test\log7.txt",mode="a",encoding="utf-8")
iplist =open(ip_file, 'r')
#rzlist =open(rz_file, 'w')

def login_device(ip,*cmd):
    huawei={
    'device_type':'huawei',
    'host': ip,
    'username':'admin',
    'password':'Huawei12#$'#FT
    #'password':'zsyyNS@2023'
    #'username':'python',#ensp测试
    #'password':'Huawei@123'#ensp测试
    }
    huawei_connect=ConnectHandler(**huawei)
    time.sleep(2)
    print("You have successfully connect to", ip)
    #print("You have successfully connect to", ip,file = log7)
    result=huawei_connect.send_config_set(cmd,enter_config_mode=False)
    #print(result)
    text = result.split("in Speed")[1].split("<")[0]#.split("Speed : ")[1].split(",")[0]
    a = []
    with open(rf"D:\Python_script\test\result{ip}.txt","w") as rzlist:
        print(text,file = rzlist)
        for s in rzlist.readlines():
            a.append(s.strip())
        print(a)
        text2 = result.split("in Speed")[1].split("<")[1]
        print(text2)
        for b in range(24):
            print(text2 + f"GigabitEthernet0/0/{b}"+ a[b],file=log7)
    huawei_connect.disconnect()
if __name__ == '__main__':
    print(f"程序于{time.strftime('%X')}开始执行")
    p = Pool(1)
    for i in iplist:
        #ip1 = a[i]
        #test = p.apply_async(login_device,args=(ip1,'screen-length 0 temporary','dis lldp nei bri'))
        test = p.apply_async(login_device,args=(i,'screen-length 0 temporary','dis interface xg | in Speed'))
    p.close()
    p.join()
    iplist.close()
    print( '总共运行了%d second' %(time.time()-start_time))
    print (f"程序于{time.strftime('%X')}执行结束")
'''
& C:/Users/ChemYS/AppData/Local/Programs/Python/Python311/python.exe d:/Python_script/test/test7.py d:/Python_script/test/ip_list7.txt d:/Python_script/test/result7.txt
'''

'''
for i in range(2,3470,26):
    for x in range(26):
        print(f"=$A{i}")
'''