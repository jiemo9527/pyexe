# coding=utf-8
# version=python3.7.1
# Tools:Pycharm 2019.1
# _Date_=2020/9/19 15:35
import os
import subprocess


def shutdwon():
    subprocess.Popen('shutdown.exe -s -t 300', shell=True)


if __name__ == '__main__':
    shutdwon()