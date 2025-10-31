#双11.淘宝秒杀实战
import time
from selenium import webdriver
import datetime
import win32com.client
speaker = win32com.client.Dispatch('SAPI.SpVoice')
#1打开浏览器---借助模块（工具） selenium 模块
times = '2022-11-11 20:32:00.000000'  #秒杀时间
browser = webdriver.Chrome()
#time.sleep(3)
browser.get('https://www.taobao.com/') #打开淘宝网
browser.find_element_by_link_text("亲，请登录").click()
print('提示：请扫码登录--------')
time.sleep(10)
browser.get('https://cart.taobao.com/')
time.sleep(5)
#让程序多次尝试找到 “全选” 按钮
while True:
    if browser.find_element_by_id("J_SelectAll1"):
        browser.find_element_by_id("J_SelectAll1").click()
        break
#点上了“全选”之后---
#对比时间--当前的时间有没有到达秒杀时间
#取一下当前互联网的时间
while True:
    now = datetime.datetime.now().strftime('%Y%m-%d %H:%M:%S.%f')
    print(now)
    if now > times:
        #表示时间超过了秒杀时间
        while True:
            if browser.find_element_by_link_text("结 算"):
                browser.find_element_by_link_text("结 算").click()
                print(f'主人，恭喜您，抢到了该商品，真好玩！！')
                speaker.Speak(f'主人，恭喜您，抢到了该商品，真好玩！！')
                break








