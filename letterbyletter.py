import sys

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from secrets import iguser, igpwd

# run from terminal by doing python3 letterbyletter.py accountname wordtocomment


def postcomment(browser, letter):
    commentbox = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, 'textarea[class="Ypffh"]')))

    commentbox.click()

    boxtwo = browser.find_element_by_css_selector('textarea[class="Ypffh focus-visible"]')

    boxtwo.send_keys(letter)

    send = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[1]/article/div[2]/section[3]/div/form/button')

    send.click()


handle = sys.argv[1]

comment = sys.argv[2]

driver = webdriver.Chrome()
driver.get('https://www.instagram.com')

form = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
        (By.TAG_NAME, 'form')))

formlist = form.find_elements_by_tag_name('input')

for char in iguser:
    formlist[0].send_keys(char)

for char in igpwd:
    formlist[1].send_keys(char)

formlist[1].send_keys(Keys.RETURN)

notnow = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
        (By.CLASS_NAME, 'HoLwm')))

notnow.click()

driver.get(f'https://www.instagram.com/{sys.argv[1]}/')

recentpost = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
    (By.CSS_SELECTOR, 'article a')))

postlink = recentpost.get_attribute('href')

driver.get(postlink)

for char in comment:
    postcomment(driver, char)
