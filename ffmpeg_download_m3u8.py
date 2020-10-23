# coding=utf-8
# version=python3.7.1
# Tools:Pycharm 2019.1
# _Date_=2020/10/13 20:41


import subprocess


def ffmpeg_download_m3u8():
    url = input("输入m3u8链接：")
    subprocess.Popen('ffmpeg -threads 32 -i %s -c copy -movflags +faststart out.mp4' % (url), shell=True)


if __name__ == '__main__':
    ffmpeg_download_m3u8()
