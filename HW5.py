# -*- coding: utf-8 -*-
import my_login
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from pymongo import MongoClient

client = MongoClient()
mongo_db = client.mail_ru

driver = webdriver.Firefox(executable_path='/snap/bin/firefox.geckodriver')
driver.implicitly_wait(15)
driver.get('https://e.mail.ru/spam/')

WebDriverWait(driver, 15).until(ec.presence_of_element_located((By.NAME, 'username')))
element = driver.find_element(By.NAME, 'username')
element.send_keys(my_login.login)
element.send_keys(webdriver.common.keys.Keys.ENTER)
WebDriverWait(driver, 15).until(ec.presence_of_element_located((By.NAME, 'password')))
element = driver.find_element_by_name('password')
ActionChains(driver).move_to_element(element).click(element).send_keys(my_login.password).perform()
element.send_keys(my_login.password)
element.send_keys(webdriver.common.keys.Keys.ENTER)

goods = driver.find_elements(By.XPATH, "//div[@class='product-card item']")
for good in goods:
    good_name = good.find_element(By.XPATH, "//div[@class='item-name']").text
    collection = mongo_db['emails']
    if not len(list(collection.find({'link' : good['link']}))):
        collection.insert_one(good_name)

