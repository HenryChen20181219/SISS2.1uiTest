# coding=utf-8
import os

import time
from lxml import etree

import requests

from config import globalparam


# 截图放到report下的img目录下
def get_img(dr, filename):
    path = globalparam.img_path + '\\' + filename
    dr.take_screenshot(path)


# 上传图片
def upload_photo():
    os.system("D:\AutoIt3\sendfile.exe")


# 采集人员信息
def get_person_info(n):
    url = "https://www.tiebazhushou.com/index/id.html/id/513436/year/2000/month/06/day/21/sex/%E7%94%B7"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"}
    res = requests.get(url, headers=headers, verify=False)
    result = res.content.decode("utf-8")
    # 获取身份证和姓名列表
    page = etree.HTML(result)

    info_list = page.xpath("//table[@class='table table-hover table-bordered']/tbody/tr")
    name_list = []
    id_card_list = []
    for i in range(1, n):
        name = info_list[i].xpath("./td[1]/text()")[0]
        id_card = info_list[i].xpath("./td[2]/text()")[0]
        name_list.append(name)
        id_card_list.append(id_card)
    return name_list, id_card_list


# 获取当前日期并格式化补0
def get_currentTime():
    t = time.strftime("%Y-%m-%d", time.localtime())
    date_from = "-".join(map(str, map(int, t.split("-"))))
    date_to = str(int(date_from[:4]) + 2) + date_from[4:]
    return date_from,date_to

if __name__ == "__main__":
    print(get_currentTime())
