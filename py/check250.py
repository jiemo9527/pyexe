# coding=utf-8
# version=python3.7.1
# Tools:Pycharm 2019.1
# _Date_=2021-06-17 8:44


import os

host = "192.168.0.250"
result = os.popen('ping %s' % (host)).read()

if 'TTL' in result:
 print(host+' 在线')
else:
 print(host+' 不在线')
 os.system('pause')
