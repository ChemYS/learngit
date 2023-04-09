        
#多进程但没有顺序
#采集华为设备up端口速率
# AD9431系列不支持

from netmiko import ConnectHandler
import time
import getpass
import sys
import os
from multiprocessing import Pool
from termcolor import colored

from napalm import get_network_driver
import json

start_time=time.time()
ip_file = sys.argv[1]  #python3.8 test.py ip 3750.txt cmd 3750.txt #sys.argv[0] 指文件名，[1]后面携带的参数
log4 = open(r"C:\Users\ChemYS\learngit\python_test\log4.txt",mode="a",encoding="utf-8")
iplist =open(ip_file, 'r')
driver=get_network_driver('huawei_vrp')

def login_device(ip):
    sw1=driver(ip,'python','Huawei@123')
    #sw1=driver(ip,'admin','Huawei12#$')
    #sw1=driver(ip,'admin','zsyyNS@2023')
    sw1.open()
    time.sleep(2)
    print("You have successfully connect to", ip)
    #print("You have successfully connect to", ip,file = log4)
    output = sw1.get_interfaces()
    output_json = json.dumps(output, indent=2)
    print(output_json)
    output2 = sw1.get_facts()
    output_json2 = json.dumps(output2, indent=2)
    print(output_json2)
    #print(output2["hostname"],file = log4)
    for key,value in output.items():
        #print(value["speed"])
        if value["is_up"] == True and (value["speed"] == 10 or value["speed"] == 100):
            print(output2["hostname"] + "    " + key + "    " + str(value["speed"]),file = log4)

    
if __name__ == '__main__':
    print(f"程序于{time.strftime('%X')}开始执行")
    p = Pool(10)
    for i in iplist:
        test = p.apply_async(login_device,args=(i,))
        #test = p.apply(login_device,args=(i,))
    p.close()
    p.join()
    iplist.close()
    print( '总共运行了%d second' %(time.time()-start_time))
    print (f"程序于{time.strftime('%X')}执行结束")
'''
& C:/Users/ChemYS/AppData/Local/Programs/Python/Python311/python.exe c:/Users/ChemYS/learngit/python_test/test4.py c:/Users/ChemYS/learngit/python_test/ip_list4.txt
'''