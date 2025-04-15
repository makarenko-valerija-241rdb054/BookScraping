import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

import time

options = Options()

# Setup service and driver
service = Service()
driver = webdriver.Chrome(service=service, options=options)

url="https://old.reddit.com/"
driver.get(url)

input()
