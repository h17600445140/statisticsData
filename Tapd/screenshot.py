import os

from PIL import Image
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def createPng(path):
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    realPath = "file://" + path
    driver.get(realPath)
    driver.save_screenshot("./png/test.png")

    # 获取验证码图片位置
    ce = driver.find_element_by_xpath('/html/body/table')
    left = (ce.location['x'])
    top = (ce.location['y'])
    right = (ce.size['width']) + left
    height = (ce.size['height']) + top

    # 获取屏幕缩放比例
    dpr = driver.execute_script('return window.devicePixelRatio')

    # 抠图
    im = Image.open('./png/test.png')
    img = im.crop((left * dpr, top * dpr, right * dpr, height * dpr))

    # 保存
    img.save('./png/tester.png')

if __name__ == '__main__':
    path = os.path.realpath("html/testerHtml.html")
    createPng(path)