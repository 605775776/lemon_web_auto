# coding:utf-8
# 2021/2/5 11:36
# Author:dsw
from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get("https://www.oschina.net/blog")
time.sleep(5)
for i in range(3):
    # 鼠标拉动滚动条
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight); var lenOfPage=document.body.scrollHeight; return lenOfPage")
    time.sleep(3)