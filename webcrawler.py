# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException 
from urllib.request import urlopen
from urllib.request import urlretrieve
from bs4 import BeautifulSoup
import time
import csv
import os

#放網址的地方 如果是檔案就這樣寫"file:web.html"
weburl = "https://fred.stlouisfed.org/series/W520RC1A027NBEA" 

#設定webdriver參數
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")
options.add_argument("--window-size=1500,800")
# options.add_argument("--headless")

#設定下載路徑&禁止popup
prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': r'.\download'}
options.add_experimental_option('prefs', prefs)

driver = webdriver.Chrome('./chromedriver',chrome_options=options)
driver.get(weburl)

#click download button
download_button = driver.find_elements_by_xpath('//*[@id="download-button"]')[0]
print("clicked")
download_button.click()
time.sleep(3)

#click csv button
driver.find_eleme
