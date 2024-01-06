#!/usr/bin/python
#coding:utf-8
import requests;
from bs4 import BeautifulSoup;
import time;
import schedule;
isSuccessful = [False]

def requestData():
  print('------------------------------------------------------------------')
  # 获取时间
  nowDate = time.strftime('%Y/%m/%d %H:%M:%S', time.localtime())
  print(nowDate)
  try:
    request_url = 'https://www.apple.com.cn/shop/refurbished/mac';
    headers = {
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
    }
    response = requests.get(request_url, headers=headers, timeout=5)
    response.encoding = 'utf-8'
    res = response.text
    print('Request: https://www.apple.com.cn/shop/refurbished/mac success')
    # 数据处理
    soup = BeautifulSoup(res, 'html.parser')
    allGoods = soup.find("div", attrs={"class": "rf-refurb-category-grid-no-js"})
    allGoodsLI = allGoods.find_all('li')
  except Exception:
    print('请求失败');
  # 找数据
  for goods in allGoodsLI:
    name = goods.find('a').contents
    price = goods.find("div", attrs={"class": "as-producttile-currentprice"}).contents
    item = " ".join([name[0], price[0]]).replace(" ", "").replace("\n", "")
    if '翻新14英寸MacBookProAppleM1Pro芯片(配备8核中央处理器和14核图形处理器)-深空灰色RMB13,849' in item:
        isSuccessful[0] = True
        print('Success!')
        print('Schedule任务结束')
        break
pass
    

if __name__ == '__main__':
  # schedule.every(30).seconds.do(requestData)
  schedule.every(1).minutes.do(requestData)
  print('Start')
  while not isSuccessful[0]:
    schedule.run_pending()
  schedule.clear()
  time.sleep(1)