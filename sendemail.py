from selenium import webdriver
import time
from secrets import *

useremail = input('Enter your email address: ')
usersubject = input('Enter the subject of your email: ')
usertext = input('Enter the body of your email: ')

browser = webdriver.Chrome()
browser.get('https://gmail.com')

login = browser.find_element_by_class_name('whsOnd')
login.send_keys(username)

loginnext = browser.find_element_by_class_name('RveJvd')
loginnext.click()

time.sleep(2)

pwd = browser.find_element_by_class_name('whsOnd')
pwd.send_keys(password)

pwdnext = browser.find_element_by_class_name('RveJvd')
pwdnext.click()

time.sleep(4)

compose = browser.find_element_by_class_name('z0')
compose.click()

time.sleep(2)

recipient = browser.find_element_by_class_name('vO')
recipient.send_keys(useremail)

subject = browser.find_element_by_class_name('aoT')
subject.send_keys(usersubject)

body = browser.find_element_by_class_name('Am')
body.send_keys(usertext)

sendit = browser.find_element_by_class_name('dC')
sendit.click()
