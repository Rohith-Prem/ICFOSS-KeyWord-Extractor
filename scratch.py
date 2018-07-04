import requests
import codecs
from selenium import webdriver
from bs4 import BeautifulSoup
import codecs
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Firefox()
driver.get('http://www.iiitmk.ac.in/MalayalamPOSTagger/index1.jsp')

a = driver.find_element_by_id('mal_text')
a.send_keys('txt')



driver.find_element_by_xpath("//input[@value='Tag The Sentence']").click();

sleep(4)
s=""
page_source = driver.page_source
soup = BeautifulSoup(page_source, 'html.parser')
for line in soup.find_all(attrs ={"size":"3"}):
				print(line.string)
				s+=line.string+'\n'

path= '/home/sid/icfoss/final_scrap/'
filename=path+"sai1234"+".utf8"
f=codecs.open(str(filename),'a','utf-8')

f.write("" + s + "")



