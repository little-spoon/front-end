#coding:utf-8
import webbrowser 
import time

while True:
    print('一小时休息提醒已开启~'+time.ctime())
    time.sleep(60 * 60)  # time.sleep():sleep time(sec) ,60 min
    webbrowser.open("file:///D:/document/rest/rest.html")  # 开网页
    
  
