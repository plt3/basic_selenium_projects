from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
from secrets import *


def getlist(driver, totalnum, type):
    box = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, 'ul[class="jSC57  _6xe7A"]')))

    print(f'Scraping Instagram {type} page...')

    rawlist = []

    while True:
        driver.execute_script("document.querySelector('div[class=\"isgrP\"]').scrollTop += 1000")
        rawlist = box.find_elements_by_tag_name('li')

        if len(rawlist) > totalnum - 15:
            time.sleep(.5)  # short wait avoids StaleElementError on last element
            if len(rawlist) == totalnum:
                break

    print(f'Parsing {type} list...')

    finallist = []

    for person in rawlist:
        try:
            allinfo = person.text.split()
            name = ' '.join(allinfo[1:-1])
            handle = allinfo[0]
            finallist.append((name, handle))
        except:
            print('Problematic account detected. Moving on...')
            continue

    print()

    return finallist


def main():
    print()

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

    followerlist = getlist(browser, numberoffollowers, 'followers')

    browser.back()

    newcssselector = 'a[href="/' + iguser + '/following/"]'

    myfollowing = browser.find_element_by_css_selector(newcssselector)

    numberoffollowing = int(myfollowing.find_element_by_tag_name('span').text)

    myfollowing.click()

    followinglist = getlist(browser, numberoffollowing, 'following')

    browser.quit()

    badfollowerlist = [tup for tup in followinglist if tup not in followerlist]

    badfollowerlist.sort(key=lambda x: x[1])

    filename = iguser + '_badfollowers.txt'

    with open(filename, 'w') as endfile:
        print(f'People who @{iguser} follows but who do not follow back:\n\n', file=endfile)
        print('Instagram handle: name\n', file=endfile)

        for name, handle in badfollowerlist:
            print(f'{handle}: {name}', file=endfile)

        print('\n\nTotal:', str(len(badfollowerlist)), file=endfile)  # maybe delete?

    print(f'Done. Look for a "{filename}" file in your current directory.')


main()
