import paramiko
from netmiko import ConnectHandler
import pandas as pd
import nmap
import requests
import time
from multiprocessing import Pool

device_list = pd.read_csv(r"C:\Users\ChemYS\learngit\python_test\list8.csv")
log8 = open(r"C:\Users\ChemYS\learngit\python_test\log8.txt",mode="a",encoding="utf-8")
start_time=time.time()

def login_device(ip,*cmd):
    huawei={
    'device_type':'huawei',
    'host': ip,
    #'username':'admin',
    #'password':'Huawei12#$'#FT
    #'password':'zsyyNS@2023'
    'username':'python',#ensp测试
    'password':'Huawei@123'#ensp测试
    }
    huawei_connect=ConnectHandler(**huawei)
    time.sleep(2)
    print("You have successfully connect to", ip)
    #print("You have successfully connect to", ip,file = log8)
    #result=huawei_connect.send_config_set(cmd,enter_config_mode=False)
    #print(result,file = log3)
    output = huawei_connect.send_config_set(cmd,enter_config_mode=False)
    interface_list = output.split('outErrors')[1].split("<")[0]
    print(interface_list,file = log8)
    for interface in interface_list:
        name = interface.split()[0]
        inErrors = interface.split()[5]
        outErrors = interface.split()[6]
    result = pd.DataFrame(columns=['IP', 'name', 'inErrors', 'outErrors'])
    result = result.append({'IP': ip, 'Interface': name, 'inErrors': inErrors, 'outErrors':outErrors}, ignore_index=True)
    result.to_csv('result8.csv', index=False)
    huawei_connect.disconnect()

if __name__ == '__main__':
    print(f"程序于{time.strftime('%X')}开始执行")
    p = Pool(1)
    for index,row in device_list.iterrows():
        ip = row['ip']
        #username = row['username']
        #password = row['password']
        test = p.apply_async(login_device,args=(ip,'screen-length 0 temporary','dis int bri'))
    p.close()
    p.join()
    print( '总共运行了%d second' %(time.time()-start_time))
    print (f"程序于{time.strftime('%X')}执行结束")

