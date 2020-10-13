import os
import win32api
import win32process


def ww():
    win32api.ShellExecute(0, 'open', r'D:\webserver\cyou88.exe', '', '', 1)
    win32api.ShellExecute(0, 'open', r'D:\webserver\EasyWebSvr.exe', '', '', 1)
    os.system('"C:/Users/JIEMO.JIEMO-PC/AppData/Local/Vivaldi/Application/vivaldi.exe" http://miaowu.cyou:88/iwg8guefigfewyf/')

if __name__ == '__main__':
    ww()


