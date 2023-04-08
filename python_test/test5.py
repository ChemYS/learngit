        
#采集华为设备端口包详细

import time
import sys
from multiprocessing import Pool
from termcolor import colored

from napalm import get_network_driver
import json

start_time=time.time()
ip_file = sys.argv[1]  #python3.8 test.py ip 3750.txt cmd 3750.txt #sys.argv[0] 指文件名，[1]后面携带的参数
log5 = open(r"D:\Python_script\test\log5.txt",mode="a",encoding="utf-8")
iplist = open(ip_file, 'r')
driver=get_network_driver('huawei_vrp')

def login_device(ip):
    #sw1=driver(ip,'python','Huawei@123')
    sw1=driver(ip,'admin','Huawei12#$')
    sw1.open()
    #print("You have successfully connect to", ip)
    print("You have successfully connect to", ip,file = log5)
    output = sw1.get_interfaces_counters()
    output_json = json.dumps(output, indent=2)
    print(output_json)
    #print(output.items())
    for key,value in output.items():
        #print(value["speed"])
        if value["tx_unicast_packets"] != 0:
            print(key+ "    " + "tx_errors:" + str(value["tx_errors"]) + "    " + "rx_errors:" + str(value["rx_errors"]),file = log5)
    
if __name__ == '__main__':
    print(f"程序于{time.strftime('%X')}开始执行")
    p = Pool(10)
    for i in iplist:
        test = p.apply_async(login_device,args=(i,))
    p.close()
    p.join()
    iplist.close()
    log5.close()
    print( '总共运行了%d second' %(time.time()-start_time))
    print (f"程序于{time.strftime('%X')}执行结束")
'''
& C:/Users/ChemYS/AppData/Local/Programs/Python/Python311/python.exe d:/Python_script/test/test5.py d:/Python_script/test/ip_list5.txt
'''