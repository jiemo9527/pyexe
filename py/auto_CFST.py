# coding=utf-8
# version=python3.7.1
# Tools:Pycharm 2019.1
# _Date_=2021-06-16 10:38
import os
from logging import info





# 打开excel获取
#pandas打包太大，弃
# cfst_ip=pandas.read_csv("D:\\NETtool\GFW\\CloudflareST_windows_amd64\\result.csv").iloc[-1]["IP 地址"]
excel=open("D:\\NETtool\GFW\\CloudflareST_windows_amd64\\result.csv","r",encoding='utf8')
opened_file = excel.readlines()
cfst_ip=opened_file[1].split(',')[0]
print("获取优选ip("+cfst_ip+")成功.\n")


change_dns=cfst_ip+"		"

def clearline():
# 删除旧记录
    host_path="C:\WINDOWS\system32\drivers\etc\HOSTS"
    lines=open(host_path,'r').readlines()
    hosts= open(host_path, 'w')
    for i in lines:
       if 'cdnets.cyou' not in i:
          hosts.write(i)
print("已清除旧的dns记录.\n")
clearline()
def addline(change_dns):
#插入新的dns记录
    host_path="C:\WINDOWS\system32\drivers\etc\HOSTS"
    hosts=open(host_path,'a')
    hosts.write(change_dns)
    hosts.close()
    print("新增dns记录成功.\n")
addline(change_dns+"rn.cdnets.cyou\n"+change_dns+"ww.cdnets.cyou")
os.system('pause')