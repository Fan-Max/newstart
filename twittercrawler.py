import requests  #导入requests 库
from bs4 import BeautifulSoup  #导入BeautifuoSoup
from selenium import webdriver                      #导入selenium 的 webdriver
from selenium.webdriver.common.keys import Keys     #导入keys
from selenium.webdriver.chrome.options import Options
import io
from DBConnection import SqlConn
import os
import re
from utility import utility

class twitterCrawler():

    def __init__(self):

        self.headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '

                                      '(KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134'} #给定义一个请求头来模拟EDGE

        self.web_url = 'https://twitter.com/realDonaldTrump'

        module_path = os.path.dirname(__file__)

        path = module_path + '/config.xml'

        configfile = io.open(path, encoding='utf-8')

        pathinfo = BeautifulSoup(configfile, 'xml')

        self.photo_path = pathinfo.find('picpath').text.strip()

        #self.crawlerlogging = crawlerlog

        self.sqlcusor = SqlConn('Btest')

    def request(self, url):

        r = requests.get(url, headers=self.headers)

        return r

    def get_twitter_content(self):  #获取twitter内容

        print("开始网页get请求")

        chrome_options = Options()

        chrome_options.add_argument('--headless')

        driver = webdriver.Chrome(chrome_options=chrome_options)   #无头模式

        driver.get(self.web_url)

        utility_1 = utility() #实例化utility类

        utility_1.scoll_down(driver, 3)   #下拉滚动条

        print('begin to retrieve twitter content')

        tw = BeautifulSoup(driver.page_source, 'lxml')

        print("parsing text container")

        twlist = tw.find_all("div", {"class": "js-stream-tweet"})  # 获取twitter content 标签

        #RetwCount = tw.find_all_next("span", {"ProfileTweet-actionCount": "Retweet"})

        twRetwitter = tw.find_all("button", {"class": "js-actionRetweet"})

        twRetwitter = twRetwitter.find_all("button",{"aria-describedby": re.compile(r".*")})

        twRetwitter = tw.find_all("button", {"class": "js-actionRetweet"} and {"aria-describedby": re.compile(r".*")})

        print("connecting DB")

        DBConnect = SqlConn('Btest')

        #utility_1.mkdir(self.photo_path)# 创建文件夹

        for tw1 in twlist:   # 遍历所有img标签

            tw_text = tw1.get_text()

            self.sqlcusor.get_i_sql('twitter_content',[])

