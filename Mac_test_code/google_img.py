from selenium import webdriver

browser = webdriver.Chrome() #声明要模拟的浏览器是Chrome

url = 'https://www.baidu.com/' #要访问的网页链接，这里以baidu为例

browser.get(url) #通过get方式获取网页

text = browser.page_source #获得网页源代码

print(text) #打印出源代码
