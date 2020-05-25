from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
from secrets import *


def findbyclass(name, driver, keys='click'):
    elem = driver.find_element_by_class_name(name)

    if keys == 'click':
        elem.click()
    else:
        elem.send_keys(keys)


def explicitwait(attribute, driver, keys='click'):
    try:
        elem = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
                (By.CLASS_NAME, attribute)))
    except:
        driver.quit()

    if keys == 'click':
        elem.click()
    else:
        elem.send_keys(keys)


def main():
    useremail = input('Enter your email address: ')
    usersubject = input('Enter the subject of your email: ')
    usertext = input('Enter the body of your email: ')

    browser = webdriver.Chrome()
    browser.get('https://gmail.com')

    login = browser.find_element_by_id('identifierId')
    login.send_keys(username)

    findbyclass('RveJvd', browser)

    try:
        pwd = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#password .aCsJod .aXBtI .Xb9hP .whsOnd')))
    except:
        browser.quit()

    pwd.send_keys(password)

    findbyclass('RveJvd', browser)

    explicitwait('z0', browser)

    explicitwait('vO', browser, useremail)

    findbyclass('aoT', browser, usersubject)

    findbyclass('Am', browser, usertext)

    findbyclass('dC', browser)

    time.sleep(5)


main()
