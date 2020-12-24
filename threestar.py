# coding=utf-8
# version=python3.7.1
# Tools:Pycharm 2019.1
# _Date_=2020/12/8 9:33
import os
from collections import Counter
from time import sleep

import requests
from bs4 import BeautifulSoup

purl = []
num_li = []
stime_li = []
sta = []
total = []
Cookie_input=input("请输入Cookie信息：")
xxx = input("请输入当前网站期号页最大值【1-120】：")

headers = {"User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9.1.6) ",
           "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
           "Accept-Language": "en-us",
           "Connection": "keep-alive",
           "Accept-Charset": "GB2312,utf-8;q=0.7,*;q=0.7",
           "Cookie": Cookie_input}
for i in range(1, int(xxx)):
    purl.append("https://www.lezhuan.com/fast/?p=" + str(i))
for x in range(len(purl)):
    html = requests.post(purl[x], headers=headers)
    html.encoding = "GBK"
    soup = BeautifulSoup(html.text, 'lxml')
    num = soup.select(".kjhm .color_ball")
    for m in range(len(num)):
        num[m] = num[m].text
        if (int(num[m]) >= 10) and (int(num[m]) <= 17):
            num[m] = "中"
        else:
            num[m] = "边"
    num_li.append(num)

for num in range(len(num_li)):
    sta += num_li[num]

print("开始分析数据")

for flag in range(0, len(sta) - 6):
    if sta[flag] != sta[flag + 1] and sta[flag] != sta[flag - 1]:
        total.append(sta[flag] + "*1")
    if sta[flag] == sta[flag + 1] and sta[flag + 1] != sta[flag + 2] and sta[flag] != sta[flag - 1]:
        total.append(sta[flag] + "*2")
    if sta[flag] == sta[flag + 1] == sta[flag + 2] and sta[flag + 2] != sta[flag + 3] and sta[flag] != sta[flag - 1]:
        total.append(sta[flag] + "*3")
    if sta[flag] == sta[flag + 1] == sta[flag + 2] == sta[flag + 3] and sta[flag + 3] != sta[flag + 4] and sta[flag] != \
            sta[flag - 1]:
        total.append(sta[flag] + "*4")
    if sta[flag] == sta[flag + 1] == sta[flag + 2] == sta[flag + 3] == sta[flag + 4] and sta[flag + 4] != sta[
        flag + 5] and sta[flag] != sta[flag - 1]:
        total.append(sta[flag] + "*5")
    if sta[flag] == sta[flag + 1] == sta[flag + 2] == sta[flag + 3] == sta[flag + 4] == sta[flag + 5] \
            and sta[flag + 5] != sta[flag + 6] and sta[flag] != sta[flag - 1]:
        total.append(sta[flag] + "*6")
    if sta[flag] == sta[flag + 1] == sta[flag + 2] == sta[flag + 3] == sta[flag + 4] == sta[flag + 5] == sta[flag + 6] \
            and sta[flag + 6] != sta[flag + 7] and sta[flag] != sta[flag - 1]:
        total.append(sta[flag] + "*7")
    if sta[flag] == sta[flag + 1] == sta[flag + 2] == sta[flag + 3] == sta[flag + 4] == sta[flag + 5] == sta[
        flag + 6] == sta[flag + 7] \
            and sta[flag + 7] != sta[flag + 8] and sta[flag] != sta[flag - 1]:
        total.append(sta[flag] + "*8")
    if sta[flag] == sta[flag + 1] == sta[flag + 2] == sta[flag + 3] == sta[flag + 4] == sta[flag + 5] == sta[
        flag + 6] == sta[flag + 7] == sta[flag + 8] \
            and sta[flag + 8] != sta[flag + 9] and sta[flag] != sta[flag - 1]:
        total.append(sta[flag] + "*9")
    if sta[flag] == sta[flag + 1] == sta[flag + 2] == sta[flag + 3] == sta[flag + 4] == sta[flag + 5] == sta[
        flag + 6] == sta[flag + 7] == sta[flag + 8] == sta[flag + 9] \
            and sta[flag + 9] != sta[flag + 10] and sta[flag] != sta[flag - 1]:
        total.append(sta[flag] + "*10")
    if sta[flag] == sta[flag + 1] == sta[flag + 2] == sta[flag + 4] == "边" and \
            sta[flag] != sta[flag - 1] and sta[flag + 3] == sta[flag - 1]:
        total.append("三切全败")
    if sta[flag] == sta[flag + 1] ==sta[flag + 3] == "边" and \
            sta[flag] != sta[flag - 1] and sta[flag + 2] == sta[flag + 4]==sta[flag-1]:
        total.append("双切全败")
    if sta[flag] == sta[flag + 2] ==sta[flag + 4] == "边" and \
            sta[flag] != sta[flag - 1] and sta[flag + 1] == sta[flag + 3]==sta[flag-1]:
        total.append("单切全败")

print("统计样本次数  ：  " + str(len(total)))
A = Counter(total).most_common()
print("详细情况  ：  \n" + str(A) + "\n概率转化：")
for i in range(len(A)):
    if A[i][0].find("全败") == -1:
        yu = int(A[i][0].split("*")[1]) - 1
        print(A[i][0] + "  :  " + str(round((int(A[i][1]) / int(len(total) - yu) * 100), 2)) + "%")
    else:
        print(A[i][0] + "  :  " + str(round((int(A[i][1]) / int(len(total) - 4) * 100), 2)) + "%")

os.system('pause')
