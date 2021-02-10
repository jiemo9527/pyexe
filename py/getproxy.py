# coding=utf-8
# version=python3.7.1
# Tools:Pycharm 2019.1
# _Date_=2020/7/27 17:20
import os
import sys
import time

import requests
from bs4 import BeautifulSoup


# setdelay=input('筛选延时上限数值(默认1000)[100-1500]:')
# setanonymity=input('筛选具体匿名保护的(默认N)[N/Y]:')
# setcountry=input('筛选国家(默认ALL)[CN/US/JP/HK/ALL]：')
# if(setdelay==''):
#     setdelay=1000
# if(setanonymity==''):
#     setanonymity='N'
# if(setcountry==''):
#     setcountry='ALL'
setdelay=1000
print('请耐心等待....')
purl = []

for i in range(1, 30):
    purl.append('https://www.freeproxy.world/?type=&anonymity=4&country=&speed=1000&port=&page=' + str(i))
session_proxy = requests.Session()
for x in range(len(purl)):
    ip_list = []
    port_list = []
    delay_list = []
    type_list = []
    country_list = []
    Anonymity_list = []
    ip_port = []
    useful_index = []
    data = []

    html = session_proxy.get(purl[x])
    soup = BeautifulSoup(html.text, 'lxml')
    trs1 = soup.select('tbody .show-ip-div')
    trs2 = soup.select('tbody tr td a')
    trs3 = soup.select('tbody tr td a span')
    trs = soup.select('strong')

    for tr in enumerate(trs):
        total = str(tr).split('currently ')[1].split('proxy')[0].strip()
    for i, tr in enumerate(trs1):
        # if i%2==1:
        ip_list.append(str(tr).split('">')[1].split('</')[0].strip())

    for i, tr in enumerate(trs2):
        if i % 5 == 0:
            port_list.append(str(tr).split('">')[1].split('</')[0])

    for i, tr in enumerate(trs2):
        if i % 5 == 2:
            delay_list.append(str(tr).split('">')[1].split('</')[0].strip())

    for i, tr in enumerate(trs3):
        if i % 2 == 1:
            country_list.append(str(tr).split('">')[1].split('</')[0])
    for i, tr in enumerate(trs2):
        if i % 5 == 3:
            type_list.append(str(tr).split('">')[1].split('</')[0].strip())

    for i, tr in enumerate(trs2):
        if i % 5 == 4:
            Anonymity_list.append(str(tr).split('">')[1].split('</')[0].strip())

    for i in range(0, 50):
        ip_port.append(ip_list[i] + ":" + port_list[i])

    # 延时筛检
    for i in range(0, 50):
        if int(delay_list[i].split('ms')[0].strip()) < int(setdelay):
            useful_index.append(i)
    for i in range(len(useful_index)):
        data.append({ip_port[useful_index[i]],
                     delay_list[useful_index[i]],
                     Anonymity_list[useful_index[i]],
                     type_list[useful_index[i]],
                     country_list[useful_index[i]],
                     })

    file = open("getproxy.txt", 'a')
    file.write(str(data))
    file.close()
    print('\r 本次总数量：' + str(total) + '已完成约：' +
          str(format(int(x * 50 + 50) * 100 / int(total), '.2f')) + '%',
          end='')
    sys.stdout.flush()
    time.sleep(0.1)
print('\n数据已写入文件！')

os.system('pause')