# coding=utf-8
# version=python3.7.1
# Tools:Pycharm 2019.1
# _Date_=2021-06-16 10:38
import os
from logging import info




host_path="C:\WINDOWS\system32\drivers\etc\HOSTS"
# 打开excel获取
#pandas打包太大，弃
# cfst_ip=pandas.read_csv("D:\\NETtool\GFW\\CloudflareST_windows_amd64\\result.csv").iloc[-1]["IP 地址"]
excel=open("D:\\NETtool\GFW\\CloudflareST_windows_amd64\\result.csv","r",encoding='utf8')
opened_file = excel.readlines()
cfst_ip=opened_file[1].split(',')[0]
print("获取优选ip("+cfst_ip+")成功.\n")
change_dns=cfst_ip+"		st.rn.cdnets.cyou"
hosts= open(host_path, 'rb+')
line = hosts.readline()
# 删除最后一行
pos = [0, hosts.tell()]
while line != b'':
    line = hosts.readline()
    temp = hosts.tell()
    if temp != pos[1]:
        pos[0] = pos[1]
        pos[1] = temp
hosts.seek(pos[0], 0)
hosts.truncate()
hosts.close()
print("已清除旧的dns记录.\n")
#插入新的dns记录
hosts=open(host_path,'a')
hosts.write(change_dns)
hosts.close()
print("新增dns记录成功.\n")
os.system('pause')