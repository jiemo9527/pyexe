# coding=utf-8
# version=python3.7.1
# Tools:Pycharm 2019.1
# _Date_=2020/10/13 20:41
import os
import webbrowser
import winreg

import requests

KEY_ProxyEnable = "ProxyEnable"
KEY_ProxyServer = "ProxyServer"
KEY_ProxyOverride = "ProxyOverride"
KEY_XPATH = "Software\Microsoft\Windows\CurrentVersion\Internet Settings"
API_Url=""

def getproxy():
    proxyIp = requests.get(API_Url).text
    return proxyIp


def setproxy(enable,proxyIp):
    hKey = winreg.OpenKey(winreg.HKEY_CURRENT_USER, KEY_XPATH, 0, winreg.KEY_WRITE)
    winreg.SetValueEx(hKey, KEY_ProxyEnable, 0, winreg.REG_DWORD, enable)
    winreg.SetValueEx(hKey, KEY_ProxyServer, 0, winreg.REG_SZ, proxyIp)
    winreg.SetValueEx(hKey, KEY_ProxyOverride, 0, winreg.REG_SZ, "localhost")
    winreg.CloseKey(hKey)


if __name__ == '__main__':
    open=input("是否打开浏览器http://zhimaruanjian.com/getapi/领取免费ip？(y/n):")
    if open=="y":
        print("完成领取后复制API地址，关闭网页以继续....")
        os.system('"chrome" h.zhimaruanjian.com/getapi/')
    API_Url=input("请输入API接入地址：")
    print("\n\n\n 0 : 清除代理 \n 1 : 设置代理(重复设置将刷新获取)\n -1 ： 退出程序\n\n\n")
    while True:
        enable=input("请输入指令：")
        if enable=="0":
            setproxy(int(enable), "")
            print("已清除代理设置!\n")
        elif enable=="1":
            setproxy(0, "")
            proxyIp = getproxy()
            setproxy(int(enable),proxyIp)
            print("已切换到代理→  "+proxyIp+"\n")
        elif enable=="-1":
            print("拜了个拜！")
            exit()
        else:
            print("请输入正确的开关指令!\n")
