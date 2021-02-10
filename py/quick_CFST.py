import os
import subprocess



def quick_CFST():
    print("请确保在'CloudflareST.exe'目录下\n\n")
    mm=input("默认筛选低于200ms高于10M/s的4个ip地址(y默认/n自定义)：")

    if mm.strip(" ").strip("y")=="":
        t1=200
        s1=10
        dn=4
    elif mm.strip(" ")=="n":
        t1=input("请输入最高延时[ms]：")
        s1=input("请输入最低速度[M/s]：")
        dn=input("请输入筛选个数：")
    else:
        print("输入错误.")
        os.system('pause')
    subprocess.Popen("CloudflareST.exe -tl %s -sl %s -dn %s" %(t1,s1,dn),shell=True)
if __name__ == '__main__':
   quick_CFST()


