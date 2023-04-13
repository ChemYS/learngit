        
#采集华为设备端口包详细
#将输出结果制表或者录入excel
import time
from multiprocessing import Pool
from termcolor import colored

from napalm import get_network_driver
import json
import pandas as pd

start_time=time.time()
device_list = pd.read_csv(r"C:\Users\ChemYS\learngit\python_test\list5.csv")
log5 = open(r"C:\Users\ChemYS\learngit\python_test\log5.txt",mode="a",encoding="utf-8")
driver=get_network_driver('huawei_vrp')

def login_device(ip,username,password):
    sw1=driver(ip,username,password)
    sw1.open()
    #print("You have successfully connect to", ip)
    print("You have successfully connect to", ip,file=log5)
    output = sw1.get_interfaces_counters()
    output_json = json.dumps(output, indent=2)
    output2 = sw1.get_facts()
    #output_json2 = json.dumps(output2, indent=2)
    print(output_json)
    #print(output.items())
    for key,value in output.items():
        #print(value["speed"])
        if value["tx_unicast_packets"] != 0:
            print(output2["hostname"] + "    " + key+ "    " + "tx_err:" + str(value["tx_errors"]) + "    " + "rx_err:" + str(value["rx_errors"]),file=log5)
    
if __name__ == '__main__':
    print(f"程序于{time.strftime('%X')}开始执行")
    p = Pool(1)
    for index,row in device_list.iterrows():
        ip = row['ip']
        username = row['username']
        password = row['password']
        test = p.apply_async(login_device,args=(ip,username,password))
    p.close()
    p.join()
    log5.close()
    print( '总共运行了%d second' %(time.time()-start_time))
    print (f"程序于{time.strftime('%X')}执行结束")
