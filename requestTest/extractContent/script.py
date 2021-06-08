# -*- coding:utf-8 -*-

import requests
import json
import csv

def login(request):

    loginUrl = 'http://192.168.0.200/sys/auth/login'
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36"
    }
    data = {
        "multiGroup":"true",
        "loginPlatform":"PC",
        "loginKey":"UI02",
        "password":"a+7f8bQolvs3XI5DfwYf8Q=="
    }

    resp = request.post(loginUrl, headers=headers, data=data)

    return resp

def waitApprove(request):

    loginUrl = 'http://192.168.0.200/sys/boe/boeList/waitApprove'
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36"
    }
    data = {
        "queryType":"20",
        "page":"1",
        "limit":"10000"
    }

    resp = request.post(loginUrl, headers=headers, data=data)

    return resp

def handleDate(datas):

    with open('./data.csv', 'w') as f:
        for index,data in enumerate(datas):
            f.write(data)
            if index != len(datas)-1:
                f.write('\n')

if __name__ == '__main__':
    session = requests.Session()

    assert login(session).status_code == 200

    datas =[dict["boeNo"] for dict in waitApprove(session).json()["page"]["list"] ]

    handleDate(datas)