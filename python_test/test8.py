import paramiko
import netmiko
import pandas as pd
import nmap
import requests


device_list = pd.read_csv(r"C:\Users\ChemYS\learngit\python_test\list8.csv")

for index,row in device_list.iterrows():
    ip = row['ip']
    username = row['username']
    password = row['password']
    print(ip)
    print(username)
    print(password)
    print(type(ip))
    print(type(username))
    print(type(password))
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=ip,username=username,password=password)
    stdin,stdout,stderr = ssh.exec_command("dis inter")
    output = stdout.read().decode("utf-8")
    interface_list = output.split('----------------------------------------------------')[1:-1]

    for interface in interface_list:
        name = interface.split()[0]
        status = interface.split()[1]
        speed = interface.split()[3]
        utilization = interface.split()[4]
    ssh.close()

result = pd.DataFrame(columns=['IP', 'Interface', 'Status', 'Speed', 'Utilization'])
result = result.append({'IP': ip, 'Interface': name, 'Status': status, 'Speed': speed, 'Utilization': utilization}, ignore_index=True)
result.to_csv('result.csv', index=False)