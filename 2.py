from selenium import webdriver
import time


# with open("name.txt", "r") as f:
#     NAME = f.read().split('\n')

class Search():
    def __init__( self ):
        self.driver = None
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_argument('--ignore-certificate-errors')
        self.links = []
        self.f = open( 'result.txt', 'w' )


    def find_links( self ):
        urls = self.driver.find_elements("xpath",'*//a')

        for url in urls:
            self.links.append(url.get_attribute("href"))

        self.check_content()

    def check_content(self):
        cnt_1, cnt_2 = 0, 0
        # print(1)
        # print(self.links)
        for url in self.links:
            temp_url = str(url)
            if( temp_url.find('google') == -1 and temp_url.find('support') == -1 and temp_url != 'None'):
                cnt_1 += 1
        print(cnt_1)
        for url in self.links:
            # print(10086)
            # print(url)
            temp_url = str(url)
            if( temp_url.find('google') == -1 and temp_url.find('support') == -1 and temp_url != 'None'):
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
                text = self.driver.page_source
                text = (str)(text)
                if( text.find("外國") != -1 ):
                    print("!!!!!", url)
                    self.f.write( url + '\n' )
        
        
        print( cnt_1, cnt_2 )
                # print(22222)
                # self.driver.get('www.baidu.com')
                # print(1)
                # newwindow = f'window.open("{temp_url}")'
                # self.driver.execute_script(newwindow)
                # self.driver.switch_to_window(self.driver.window_handles[1])
                # self.driver.close() 
                # pass
     #            self.driver.get(url)
       #          text = self.driver.page_source
                # print(type(text))
                # print(url)
                #if( text.find("黑暴") ):
                #    print(text.)
           #  else:
         #        pass

    def start( self, URL, kw ):
        self.f.write( kw + '\n' )
        try:
            self.driver.quit()
        except:
            pass

        self.driver = webdriver.Chrome(executable_path=r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe', options=self.chrome_options)
        self.driver.get(URL)


    def end( self ):
        self.f.write('\n')
        self.driver.quit()
        self.f.close()



def main():
    f = open( "name.txt", encoding = "utf-8" )
    NAME = f.read()
    NAME = NAME.split('\n')
    print(NAME)
    
    for name in NAME:
        if( name == '' ):
            continue
        kw = name
        URL = f"https://www.google.com/search?q={kw}"
        try:
            search = Search() 
            search.start( URL, kw )
            search.find_links()
            search.end()
        except:
            pass


if __name__ == "__main__":
    main()
    
