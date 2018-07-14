import requests
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException
from xvfbwrapper import Xvfb
import re

from bs4 import BeautifulSoup

#hiding web driver
#display = Xvfb()
#display.start()

def getWordsFromURL(url):
    return re.compile(r'[\:/?=\-&]+', re.UNICODE).split(url)


path = "/home/rohith/ICFOSS-KeyWord-Extractor/POSTagging"
scrap = open('/home/rohith/ICFOSS-KeyWord-Extractor/Tokenise/scrapped_text.txt', 'w', encoding='utf-8')
f = open("/home/rohith/ICFOSS-KeyWord-Extractor/Features/head_url.txt", 'w', encoding='utf-8')
driver = webdriver.Firefox(path)
driver.get('http://olam.in/Transliterate/')

def getdata(i):
    url = str(i)
    resp = requests.get(url)
    if resp.status_code == 200:
        soup = BeautifulSoup(resp.text, 'html.parser')
        links = soup.findAll("p")
        if len(links) != 1:
            head = soup.findAll("h1")[0].text
            f.write(head)
            txt=""
            # path = 'E:\Work\ICFOSS\ICFOSS-KeyWord-Extractor\Tokenise'

            for t in links:
                txt += t.text
            # filename = path + "\scrapped_text.txt"
            scrap.write(str(txt))
    else:
        print("error")


def main(url1):
    # print("enter the link\n")
    # ll=input()
    getdata(url1)

    # print(getWordsFromURL(url1))
    urls = getWordsFromURL(url1)
    # change this according to news url pattern
    urls = urls[2:len(urls) - 1]
    a = driver.find_element_by_id('transliterate')
    for u in urls:
        if len(u) > 3:
            a.send_keys(u, Keys.ENTER)
            sleep(3)
    mal_u = a.get_attribute('value')
    f.write("\n" + mal_u)


def scrapper(url):
    main(url)
    return 1
