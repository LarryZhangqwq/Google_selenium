from selenium import webdriver
import time


# with open("name.txt", "r") as f:
#     NAME = f.read().split('\n')

class Search():
    def __init__( self ):  # 初始化
        self.driver = None
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_argument('--ignore-certificate-errors') # 忽略不安全网站提醒
        self.links = [] # 存放所有link
        self.f = open( 'result.txt', 'a' ) # 打开存放搜索结果的文件
        self.k = open( 'keyword.txt', encoding = "utf-8" ) # 打开存放关键词的文件
        self.KEYWORD = self.k.read() # 读取关键词
        self.KEYWORD = list(self.KEYWORD.split('\n')) # 提取每一个关键词


    def find_links( self ):
        urls = self.driver.find_elements("xpath",'*//a') # 提取网页中的所有link

        for url in urls:
            self.links.append(url.get_attribute("href")) # 转换网页中的所有link

        self.check_content() # 调用搜索关键词函数

    def check_content(self):
        cnt_1, cnt_2 = 0, 0
        # print(1)
        # print(self.links)
        for url in self.links:
            temp_url = str(url)
            if( temp_url.find('google') == -1 and temp_url.find('support') == -1 and temp_url != 'None' ):
                cnt_1 += 1 
        print(cnt_1)
        for url in self.links:
            # print(10086)
            # print(url)
            temp_url = str(url)
            if( temp_url.find('google') == -1 and temp_url.find('support') == -1 and temp_url != 'None'): # 剔除掉没用的link
                time.sleep(1)
                # print(temp_url)
                try:
                    # self.driver.close()
                    # self.driver = webdriver.Chrome(executable_path=r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe', options=self.chrome_options) 
                    self.driver.get(temp_url)
                    cnt_2 += 1
                    print(cnt_2)
                except:
                    # print("Error    ", temp_url)
                    pass
                text = self.driver.page_source # 获取网页源码
                text = (str)(text)
                mark = 0
                kw_list = []
                for kw in self.KEYWORD:
                    if(  text.find(kw) != -1 ): # 查找是否有关键词
                        kw_list.append(kw)
                    if( text.find(kw) != -1 and mark == 0 ):
                        mark = 1
                        title_name = self.driver.title
                        # print(title_name, )
                if( mark ):
                    self.f.write( title_name + '     ' )
                    for i in kw_list:
                        self.f.write( i + " " )
                    self.f.write( '\n' + url + '\n' )
                    self.f.close()
                    self.f = open( 'result.txt', 'a' )
        
        
        print( cnt_1, cnt_2 )

    def start( self, URL, name ):
        self.f.write( name + '\n' ) # 输出当前搜索的人名
        try:
            self.driver.quit()
        except:
            pass

        self.driver = webdriver.Chrome(executable_path=r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe', options=self.chrome_options)
        self.driver.get(URL) # 启动浏览器并跳转到“URL”页面


    def end( self ):
        self.f.write('\n' + '\n' ) 
        self.driver.quit() # 退出浏览器
        self.f.close() # 关闭文档



def main():
    f = open( "name.txt", encoding = "utf-8" ) # 打开存放人名的文档
    NAME = f.read()
    NAME = NAME.split('\n')
    # print(NAME)
    
    for name in NAME:
        if( name == '' ):
            continue
        kw = name
        URL = f"https://www.google.com/search?q={kw}" # 构建要搜索的网址
        try:
            search = Search()  # 定义变量，初始化
            search.start( URL, kw ) # 打开URL这个网站
            search.find_links() # 找所有link + 筛选
            search.end()
        except:
            pass


if __name__ == "__main__":
    main()
    
