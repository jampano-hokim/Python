import requests, sys, os
from bs4 import BeautifulSoup
from urllib.request import urlopen
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import urllib.request
import time
import re
from fake_useragent import UserAgent
from playsound import playsound

driver = webdriver.Chrome('./chromedriver')
driver.get('https://shopping.naver.com/')
time.sleep(1)

driver.find_element_by_xpath('//*[@id="autocompleteWrapper"]/input[1]').send_keys('어린왕자 손거울')
time.sleep(0.5)
driver.find_element_by_xpath('//*[@id="autocompleteWrapper"]/a[2]').click()
time.sleep(1)

driver.get(driver.current_url)
time.sleep(1)
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
sel = soup.select('a.basicList_link__1MaTN')
print(sel)