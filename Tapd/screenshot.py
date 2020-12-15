import os

from PIL import Image
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def createPng(html_path, screenshot_path, png_path):
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    realPath = "file://" + html_path
    driver.get(realPath)
    driver.save_screenshot(screenshot_path)

    # 获取验证码图片位置
    ce = driver.find_element_by_xpath('/html/body/table')
    left = (ce.location['x'])
    top = (ce.location['y'])
    right = (ce.size['width']) + left
    height = (ce.size['height']) + top

    # 获取屏幕缩放比例
    dpr = driver.execute_script('return window.devicePixelRatio')

    # 抠图
    im = Image.open(screenshot_path)
    img = im.crop((left * dpr, top * dpr, right * dpr, height * dpr))

    # 保存
    img.save(png_path)

if __name__ == '__main__':
    html_path = os.path.realpath("html/testerHtml.html")
    screenshot_path = "./png/test.png"
    png_path = './png/tester.png'
    createPng(html_path, screenshot_path, png_path)