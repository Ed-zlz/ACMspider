# -*- coding: utf-8 -*-
# @Time : 2018/11/1 15:54
# @Author : Ed
# @File : table_downloader.py

import requests
import re
import json


class TableDownloader(object):
    def download(self, root_url):
        password = input("Please press the ranklist's password:")
        headers = {
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'zh-CN,zh;q=0.9',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
        }
        try:
            r = requests.Session()
            r.post("https://vjudge.net/user/login", data={'username': 'zhbitACMspider', 'password': 'zhbitACMspider'})
            r.post(root_url, data={'password':password})
            relur = re.compile(r'[0-9]+')
            result = re.findall(relur, root_url)
            response = r.get('https://vjudge.net/contest/rank/single/' + "".join(result), headers=headers)
        except:
            print("Connection failed,please check and try again!")
        else:
            r.encoding = 'utf-8'
            data = json.loads(response.text)
            participants = data["participants"]
            submissions = data["submissions"]
            title=data["title"]
            # print(participants)
            # print(submissions)
            return participants, submissions,title
