#aim:crawl google images

from selenium import webdriver
import time
import os
import requests

# agent
# browserOptions = webdriver.ChromeOptions()
# browserOptions.add_argument('--proxy-server=ip:port)
# browser = webdriver.Chrome(chrome_options=browserOptions)

#keywords
#keyword = 'meter reading'
keyword = 'gas meter digit'
#keyword = 'leitura do medidor de gás'
#keyword = '煤气表' #cn
#keyword = '煤气表 读数' #cn1
#keyword = 'read gas meter'
#keyword = 'gas reading'
#keyword = 'gas reading metric'
url = 'https://www.google.com/search?q='+keyword+'&tbm=isch'


class Crawler_google_images:
    # init
    def __init__(self):
        self.url = url

    # get chromedriver and visit url
    def init_browser(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--disable-infobars")
        browser = webdriver.Chrome(chrome_options=chrome_options)
        # visit url
        browser.get(self.url)
        # maxmize window
        browser.maximize_window()
        return browser

    #download
    def download_images(self, browser,round=20):
        picpath = 'D:/LYIT/repository/dataset/crawl/'
        # check directory
        if not os.path.exists(picpath): os.makedirs(picpath)
        # urls
        img_url_dic = []

        count = 0 #no
        pos = 0
        for i in range(round):
            pos += 500
            # scroll down
            js = 'var q=document.documentElement.scrollTop=' + str(pos)
            browser.execute_script(js)
            time.sleep(1)
            # find images
            # html = browser.page_source#
            # get by tagname

            img_elements = browser.find_elements_by_tag_name('img')
            #webElement
            for img_element in img_elements:
                img_url = img_element.get_attribute('src')
                if isinstance(img_url, str):
                        if 'images' in img_url:
                            #check duplication
                            if img_url not in img_url_dic:
                                try:
                                    img_url_dic.append(img_url)
                                    #download and save
                                    filename = picpath +  str(count) + "_gas_meter_digit.jpg"
                                    r = requests.get(img_url)
                                    with open(filename, 'wb') as f:
                                        f.write(r.content)
                                    f.close()
                                    count += 1
                                    print('this is '+str(count)+'st img')
                                    #sleep
                                    time.sleep(0.2)
                                except:
                                    print('failure')

    def run(self):
        self.__init__()
        browser = self.init_browser()
        self.download_images(browser,200) #crawl pages
        browser.close()
        print("done")


if __name__ == '__main__':
    craw = Crawler_google_images()
    craw.run()