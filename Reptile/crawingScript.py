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
        # 获取可以爬取的数量

    def get_new_url_size(self):
        return len(self.new_url)

    # 获取已经爬取的数量
    def get_old_url_size(self):
        return len(self.old_url)


# 爬取
class Downloader:
    def download(self, url):
        response = requests.get(url, headers={"User-Agent": UserAgent().random})
        if response.status_code == 200:
            response.encoding = 'utf-8'
            return response.text
        else:
            return None


# 解析
class Parser:
    def parse(self, html):
        e = etree.HTML(html)
        datas = self.parse_info(e)
        #datas = [span.xpath('string(.)') for span in e.xpath('//div[@class="content"]/span[1]')]
        urls = self.parse_urls(e)
        #urls = [ 'https://www.qiushibaike.com{}'.format(url) for url in e.xpath('//ul[@class="pagination"]/li/a/@href')]
        return datas, urls

    def parse_info(self, e):
        spans = e.xpath('//div[@class="content"]/span[1]')
        datas = []
        for span in spans:
            datas.append(span.xpath('string(.)'))
        return datas

    def parse_urls(self, e):
        base_url = 'https://www.qiushibaike.com{}'
        urls = []
        for url in e.xpath('//ul[@class="pagination"]/li/a/@href'):
            urls.append(base_url.format(url))
        return urls


# 数据处理
class DataOutPut:
    def save(self, datas):
        with open('duanzi.txt', 'a', encoding='utf-8') as f:
            for data in datas:
                f.write(data)


# 调度
class DiaoDu:
    def __init__(self):
        self.downloader = Downloader()
        self.url_manager = URLManager()
        self.parser = Parser()
        self.data_saver = DataOutPut()

    def run(self, url):
        self.url_manager.add_new_url(url)
        while self.url_manager.has_new_url():
            url = self.url_manager.get_new_url()
            html = self.downloader.download(url)
            data, urls = self.parser.parse(html)
            self.data_saver.save(data)
            self.url_manager.add_new_urls(urls)


if __name__ == '__main__':
    diao_du = DiaoDu()
    diao_du.run('https://www.qiushibaike.com/text/page/1/')

# url管理器、爬取、解析、数据处理 --> 调度