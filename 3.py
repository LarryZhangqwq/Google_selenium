from selenium import webdriver


driver = webdriver.Chrome(executable_path=r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
driver.get("www.baidu.com")
driver.get("www.google.com")
