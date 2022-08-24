from selenium import webdriver
import time

# driver = webdriver.Chrome(executable_path=r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')

# print(driver)
# 打印的是selenium对象 驱动

keyword = input("请输入要搜索的内容:")
URL = f"https://www.google.com/search?q={keyword}"

driver = webdriver.Chrome(executable_path=r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
# 用谷歌浏览器打开一个网站
driver.get(URL)

# urls = driver.find_elements_by_xpath("//a")
urls = driver.find_elements("xpath","//a")

links = []

for url in urls:
    # print(url.get_attribute("href"))
    links.append(url.get_attribute("href"))

# print(links)