import json
from urllib.parse import urlencode

import requests
from fake_useragent import UserAgent
from lxml import etree

# url管理
class URLManager(object):
    def __init__(self):
        self.new_url = []
        self.old_url = []

    # 获取一个url
    def get_new_url(self):
        url = self.new_url.pop()
        self.old_url.append(url)
        return url

    # 增加一个url
    def add_new_url(self, url):
        if url not in self.new_url and url and url not in self.old_url:
            self.new_url.append(url)

    # 增加多个url
    def add_new_urls(self, urls):
        for url in urls:
            self.add_new_url(url)

    # 判断是否还有可以爬取的url
    def has_new_url(self):
        return self.get_new_url_size() > 0
        # 获取可以爬取的网页数量

    def get_new_url_size(self):
        return len(self.new_url)

    # 获取已经爬取的数量
    def get_old_url_size(self):
        return len(self.old_url)



# 爬取
class Downloader:

    def download(self, url):
        headers = {
            "User-Agent": UserAgent().random}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            response.encoding = 'utf-8'
            return response.text
        else:
            return None



# 解析
class Parser:

    def parse(self, html, *args, **kwargs):

        city = args[0]

        e = etree.HTML(html)
        datas = self.parse_info(e, city)
        return datas

    def parse_info(self, e, *args, **kwargs):

        city = args[0]

        contents = e.xpath('/html/body/div[2]/div[2]/div[2]/div/div[1]/ul/text()')

        cityStation = []

        for i in range(1, len(contents)):
            station = e.xpath('/html/body/div[2]/div[2]/div[2]/div/div[1]/ul/li[{}]/dl/dt/a[1]/text()'.format(i))
            stationLocal = e.xpath(
                '/html/body/div[2]/div[2]/div[2]/div/div[1]/ul/li[{}]/dl/dt/a[2]/text()'.format(i))
            if len(stationLocal) != 0 and stationLocal[0] == city:
                cityStation.append(station[0])

        return cityStation


    def parse_urls(self, e):
        base_url = 'https://www.qiushibaike.com{}'
        urls = []
        for url in e.xpath('//ul[@class="pagination"]/li/a/@href'):
            urls.append(base_url.format(url))
        return urls



# 数据处理
class DataOutPut:

    def save(self, datas):

        with open('cityStation.json', "r", encoding="UTF-8") as f:
            Rdata = json.load(f)
            Rdata.update(datas)
            data = Rdata
            with open('cityStation.json', "w", encoding="UTF-8") as f:
                json.dump(data, f)

# 调度
class DiaoDu:

    def __init__(self):
        self.downloader = Downloader()
        self.url_manager = URLManager()
        self.parser = Parser()
        self.data_saver = DataOutPut()

    def run(self, url, *args, **kwargs):

        cityList = args[0]

        crawlUrls = []
        params = {
            'query': '',
            'trafficType': 'AIRPORT'
        }
        for i in range(len(cityList)):
            params.update({'query' : cityList[i]})
            formatUrl = url.format(urlencode(params))
            crawlUrls.append(formatUrl)
        self.url_manager.add_new_urls(crawlUrls)

        cityList.reverse()

        count = 0
        while self.url_manager.has_new_url():
            url = self.url_manager.get_new_url()
            html = self.downloader.download(url)
            data = self.parser.parse(html, cityList[count])
            self.data_saver.save({cityList[count]:data})
            count += 1

        with open('cityStation.json', "r", encoding="UTF-8") as f:
            Rdata = json.load(f)
            print(Rdata)



if __name__ == '__main__':
    city = ['广州', '北京', '上海', '长沙', '石家庄', '太原', '呼和浩特', '沈阳', '长春', '哈尔滨', '南京', '杭州', '合肥', '福州',
            '南昌', '济南', '郑州', '武汉', '南宁', '海口', '成都', '贵阳', '昆明', '拉萨', '西安', '兰州', '西宁', '银川',
            '乌鲁木齐', '遵义']
    baseUrl = 'https://you.ctrip.com/searchsite/Traffic?{}'
    diao_du = DiaoDu()


    diao_du.run(baseUrl, city)

# url管理器、爬取、解析、数据处理 --> 调度