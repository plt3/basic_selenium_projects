from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener

from secrets import *

browser = webdriver.Chrome()
browser.get('https://www.instagram.com')

form = WebDriverWait(browser, 10).until(EC.element_to_be_clickable(
        (By.TAG_NAME, 'form')))

formlist = form.find_elements_by_tag_name('input')

for char in iguser:  # using both for loops seems to avoid having to click 'new posts'
    formlist[0].send_keys(char)

for char in igpwd:
    formlist[1].send_keys(char)

formlist[1].send_keys(Keys.RETURN)

notnow = WebDriverWait(browser, 10).until(EC.element_to_be_clickable(
        (By.CLASS_NAME, 'HoLwm')))

notnow.click()

myaccount = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/section/div[3]/div[1]/div/div[1]/a')
myaccount.click()

cssselector = 'a[href="/' + iguser + '/followers/"]'

myfollowers = WebDriverWait(browser, 10).until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, cssselector)))

numberoffollowers = int(myfollowers.find_element_by_tag_name('span').text)

myfollowers.click()

followerbox = WebDriverWait(browser, 10).until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, 'ul[class="jSC57  _6xe7A"]')))

followerlist = []

ef_driver = EventFiringWebDriver(browser, AbstractEventListener())

while len(followerlist) != numberoffollowers:
    ef_driver.execute_script("document.querySelector('div[class=\"isgrP\"]').scrollTop += 1000")
    followerlist = followerbox.find_elements_by_tag_name('li')

nameandhandlelist = []

for person in followerlist:
    allinfo = person.text.split()
    name = ' '.join(allinfo[1:-1])
    handle = allinfo[0]
    nameandhandlelist.append((name, handle))

print(nameandhandlelist)
print(len(nameandhandlelist))
