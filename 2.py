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
        self.f = open( 'result.txt', 'a' )
        self.k = open( 'keyword.txt', encoding = "utf-8" )
        self.KEYWORD = self.k.read()
        self.KEYWORD = list(self.KEYWORD.split('\n'))


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
                mark = 0
                kw_list = []
                for kw in self.KEYWORD:
                    if(  text.find(kw) != -1 ):
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

    def start( self, URL, kw ):
        self.f.write( kw + '\n' )
        try:
            self.driver.quit()
        except:
            pass

        self.driver = webdriver.Chrome(executable_path=r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe', options=self.chrome_options)
        self.driver.get(URL)


    def end( self ):
        self.f.write('\n' + '\n' )
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
    
