import datetime
import os
import random
import time

def get_time(start_t, end_t): #随机生成时间戳
    a1=(start_t,1,1,0,0,0,0,0,0)       #设置开始日期时间元组（1976-01-01 00：00：00）
    a2=(end_t,12,31,23,59,59,0,0,0)  #设置结束日期时间元组（1990-12-31 23：59：59）
    start=time.mktime(a1)  #生成开始时间戳
    end=time.mktime(a2)   #生成结束时间戳
    #随机生成10个日期字符串

    t=random.randint(start,end)  #在开始和结束时间戳中随机取出一个
    date_touple=time.localtime(t)     #将时间戳生成时间元组
    date=time.strftime("%Y-%m-%d %H:%M:%S",date_touple) #将时间元组转成格式化字符串（1976-05-21）
    time_array = time.strptime(date, "%Y-%m-%d %H:%M:%S")
    timestamp = int(time.mktime(time_array))

    return timestamp


for i in range(1, 600):  #控制上传文件数量
    filename = r"test" + str(i) + ".txt"
    file = open(filename, 'w')
    file.write("a test") #创建文件
    file.close()
    command_add = "git add " + filename
    print(command_add)
    result = os.system(command_add) #git add操作

    time_stamp = str(get_time(2014, 2019)) #设置日期区间

    command_commit = "git commit --date=" + time_stamp + " -m " + '"this is a commit"'
    print(command_add,"   ",command_commit)
    result = os.system(command_commit) #git commit操作


# 将本地文件push到你的github
result = os.system('git config --global http.sslVerify "false"')
time.sleep(1)
result = os.system("git push -u origin master")
