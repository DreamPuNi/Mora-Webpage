""" 数据爬取脚本 """

import json
import time
from datetime import datetime
from lxml import etree
from app.database.database import *
from selenium import webdriver

async def get_USDCNY_exrate_from_web(start_time, end_time):
    """
    获取美元兑人民币的历史数据，主要是用来从网页爬取的。因速度较慢，已经换成用来更新数据库的了

    :param start_time: 开始时间，格式为2023-12-25
    :param end_time: 结束时间，格式为2023-12-25
    :return:
    """
    # Selenium浏览器设置
    options = webdriver.EdgeOptions()
    options.add_argument('--headless')  # 无头模式
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    driver = webdriver.Edge(options=options)
    # 加载网页
    url = f"https://www.kylc.com/huilv/d-boc-usd.html?datefrom={start_time}&dateto={end_time}"  # 替换为目标网址
    driver.get(url)
    time.sleep(3)
    # 获取页面渲染后的HTML
    page_source = driver.page_source
    driver.quit()
    # 使用 lxml 解析HTML并提取数据
    tree = etree.HTML(page_source)
    rows = tree.xpath('/html/body/div[2]/form/div[4]/div[1]/div[3]/table/tbody/tr') # debug首先看这，这狗东西一直在变
    data = []
    for row in rows:
        date = row.xpath('./td[1]/text()')
        rate = row.xpath('./td[2]/span[@class="td_rate"]/text()')
        if date and rate:
            data.append({
                "date": date[0].strip(),
                "rate": rate[0].strip()
            })
    json_data = json.dumps(data, ensure_ascii=False, indent=4)
    print(json_data)

async def get_USDCNY_exrate_from_json(start_time, end_time):
    """
    从本地的json获取指定时间范围内的美元兑人民币汇率。

    :param start_time: 开始时间，格式为 'YYYY-MM-DD'
    :param end_time: 结束时间，格式为 'YYYY-MM-DD'
    :return: 符合条件的数据列表
    """
    # 转换时间字符串为 datetime 对象然后进行比较
    try:
        start_date = datetime.strptime(start_time, '%Y-%m-%d')
        end_date = datetime.strptime(end_time, '%Y-%m-%d')
    except ValueError:
        raise ValueError("Invalid date format. Please use 'YYYY-MM-DD'.")
    if start_date > end_date:
        raise ValueError("Start time cannot be after end time.")
    USDCNY_exrate = read_json_file('USDCNY_exrate.json')
    result = [
        entry for entry in USDCNY_exrate
        if start_date <= datetime.strptime(entry["date"], '%Y-%m-%d') <= end_date
    ]
    return result

if __name__ == "__main__":
    get_USDCNY_exrate_from_web(start_time="2024-12-25", end_time="2024-12-25")