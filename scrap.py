import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import codecs
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException
import re

from bs4 import BeautifulSoup

def getWordsFromURL(url):
	    return re.compile(r'[\:/?=\-&]+',re.UNICODE).split(url)


def getdata(i):
    url = str(i)
    resp = requests.get(url)
    if resp.status_code == 200:
        soup = BeautifulSoup(resp.text, 'html.parser')
        links = soup.findAll("p")
        if len(links) != 1:
            head = soup.findAll("h1")[0].text
            head_path = 'E:\Work\ICFOSS\ICFOSS-KeyWord-Extractor\Features\\'
            filename = head_path + "head_url" + ".utf8"
            f = codecs.open(str(filename), 'a', 'utf-8')
            f.write(head)
            txt = soup.findAll("h1")[0].text
            txt += "\n"
            #path = 'E:\Work\ICFOSS\ICFOSS-KeyWord-Extractor\Tokenise'

            for t in links:
                txt += t.text
            #filename = path + "\scrapped_text.txt"
            f = open('E:\Work\ICFOSS\ICFOSS-KeyWord-Extractor\Tokenise\\scrapped_text.txt', 'a', encoding='utf-8')
            f.write(str(txt))
    else:
        print("error")


def main():
    path = "E:\Work\ICFOSS\ICFOSS-KeyWord-Extractor\POSTagging"
    # print("enter the link\n")
    # ll=input()
    url1 = "http://www.mathrubhumi.com/news/kerala/malayalam/prof-t-j-joseph-abhimanyu-murder-maharajas-college-sfi-popular-front-sdpi-1.2945324"
    getdata(url1)

    # print(getWordsFromURL(url1))
    urls = getWordsFromURL(url1)
    # change this according to news url pattern
    urls = urls[2:len(urls) - 1]
    head_path = 'E:\Work\ICFOSS\ICFOSS-KeyWord-Extractor\Features\\'
    filename = head_path + "head_url" + ".utf8"
    f = codecs.open(str(filename), 'a', 'utf-8')
    f.write("\n")
    for u in urls:
        if len(u) > 3:
	    
		driver = webdriver.Firefox(path)
		driver.get('http://olam.in/Transliterate/')

		a = driver.find_element_by_id('transliterate')
		a.send_keys(u,Keys.ENTER)
		sleep(2)
		b = driver.find_element_by_id('transliterate')

		mal_u = driver.find_element_by_id('transliterate').get_attribute('value')
	        f.write(" " + mal_u)

  
if __name__ == "__main__":
    main()
