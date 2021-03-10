from fake_useragent import UserAgent
from urllib.parse import urlencode
from lxml import etree

import requests

rootUrl = "https://you.ctrip.com/searchsite/Traffic?{}"

headers = {
    "User-Agent": UserAgent().chrome
}

params = {
    'query': '北京',
    'trafficType': 'AIRPORT'
}

url = rootUrl.format(urlencode(params))

response = requests.get(url, headers=headers)

html = etree.HTML(response.text)

contents = html.xpath('/html/body/div[2]/div[2]/div[2]/div/div[1]/ul/text()')

cityStation = {
    '北京':[]
}

for i in range(1, len(contents)):

    station = html.xpath('/html/body/div[2]/div[2]/div[2]/div/div[1]/ul/li[{}]/dl/dt/a[1]/text()'.format(i))
    stationLocal = html.xpath('/html/body/div[2]/div[2]/div[2]/div/div[1]/ul/li[{}]/dl/dt/a[2]/text()'.format(i))
    print(station, ':', stationLocal, ':', type(station))
    if len(stationLocal) != 0:
        cityStation['北京'].append(station[0])

print(cityStation)






