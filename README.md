# Google_selenium

本repo介绍了使用selenium自动搜索并且提取含有的关键词网站的title和link。

## 1. Environment

* Win10
* Chrome(103.0.5060.53) 
* ChromeDriver(103.0.5060.53)
* selenium

## 2. Installation

### 2.1 Chrome

There is no official Chromedriver for the latest version of the Chrome, so you need to **return Chrome to the previous version** and **turn off the automatic update function**.

#### Download previous vesion

* https://www.chromedownloads.net/

#### turn off the automatic update

Method 1:

* Win10是在服务器左下角右键点击鼠标，然后选择运行。
  或者直接快捷键(Windows键+字母R）----此方法通用于windows操作系统的机器。
  在运行窗口输入services.msc 进到服务管理窗口
  找到Google的两个更新的服务

  ​	Google更新服务(gupdate)
  ​	Google更新服务(gupdatem)

* 双击其中的某一个，将其启动类型设置为禁用
  再双击其中的另外一个，将其设置为禁用。

Method 2:

* 按下Win+R，打开运行对话框，输入taskschd.msc
* 打开"任务计划程序"，展开左侧功能树到"任务计划程序库"
* 分两次选择右侧两个GoogleUpdate的任务计划，右键菜单选择"禁用"。

### 2.2 ChromeDriver

Download the same version of your Chrome

https://chromedriver.storage.googleapis.com/index.html

### 2.3 Selenium

Install by pip3:

````
pip3 install selenium
````

## 3. 一些基本操作

### 3.1 初始化

Selenium 支持非常多的浏览器，如 Chrome、Firefox、Edge 等，还有 Android、BlackBerry 等手机端的浏览器。

````python
from selenium import webdriver
browser = webdriver.Chrome() 
browser = webdriver.Firefox() 
browser = webdriver.Edge() 
browser = webdriver.Safari()
browser = webdriver.Android()
browser = webdriver.Ie()
browser = webdriver.Opera()
browser = webdriver.PhantomJS()
````

**在括号中写入下载的Chromediver的路径**

example:

````python
driver = webdriver.Chrome(executable_path=r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
````

#### 忽略不安全网站提醒：

````python
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--ignore-certificate-errors')
driver = webdriver.Chrome(executable_path=xxx, options=chrome_options) 
````



### 3.2 打开网站

````python
driver.get('http://www.baidu.com/')
````

### 3.3 搜索关键词

使用selenium通过id，name或class的方式来获取到这个input标签，输入内容并提交：

````python
input_element = driver.find_element_by_name('wd')
````

### 3.4 收集网页内所有Link

````python
links = []
urls = driver.find_elements("xpath",'*//a')
for url in urls:
    links.append(url.get_attribute("href"))
````

### 3.5 获取网页Title

````python
title = driver.title
````

### 3.6 获取网页所有源代码

````python
text = driver.page_source
text = (str)(text)
````

