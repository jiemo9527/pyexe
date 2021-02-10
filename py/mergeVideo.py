# coding=utf-8
# version=python3.7.1
# Tools:Pycharm 2019.1
# _Date_=2020/10/13 20:41


import subprocess


def merge():
    audio = input("声音来源：")
    video = input("图像来源：")
    subprocess.Popen('ffmpeg.exe -i %s -i %s -acodec copy -vcodec copy output.mp4' %(audio,video), shell=True)



if __name__ == '__main__':
    merge()