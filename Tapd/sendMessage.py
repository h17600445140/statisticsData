import base64
import hashlib
import requests
from fake_useragent import UserAgent

def sendPNGMessage(png_path):
    headers = {
        "User-Agent": UserAgent().chrome,
        "Content-Type": "application/json"
    }
    # url = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=f24732df-c9fc-4719-9860-e52a67adcfa4"
    url = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=77a5ea6c-fbd2-43c3-b053-3fc0f026514b"

    # params = {
    #     "msgtype": "text",
    #     "text": {
    #         "content": "广州今日天气：29度，大部分多云，降雨概率：60%",
    #         "mentioned_list":[""]
    #     }
    # }
    # params = {
    #     "msgtype": "image",
    #     "image": {
    #         "base64": "DATA",
    #         "md5": "MD5"
    #     }
    # }

    with open(png_path, 'rb') as file:  # 转换图片成base64格式
        data = file.read()
        encodestr = base64.b64encode(data)
        image_data = str(encodestr, 'utf-8')

    with open(png_path, 'rb') as file:  # 图片的MD5值
        md = hashlib.md5()
        md.update(file.read())
        image_md5 = md.hexdigest()

    data = {
        "msgtype": "image",
        "image": {
            "base64": image_data,
            "md5": image_md5
        }
    }

    response = requests.post(url, headers=headers, json=data)

