from selenium import webdriver
import time


def main():
    processtime = 0.038

    print('How many approximate words per minute would you like this bot to')
    print('type? (enter "max" for maximum speed or "turbo" for ultra speed)', end=': ')

    while True:
        try:
            userwpm = input()

            if userwpm == 'max':
                sleeptime = 0
            elif userwpm == 'turbo':
                sleeptime = 'no'
            else:
                sleeptime = 60 / (int(userwpm) * 5) - processtime
                if sleeptime < 0 or int(userwpm) < 0:
                    raise Exception
            break
        except ValueError:
            print('Please enter a number', end =': ')
        except Exception:
            maxspeed = int(12 / processtime)
            print(f'Please enter a number between 0 and {maxspeed}', end =': ')

    browser = webdriver.Chrome()
    browser.get('https://typing-speed-test.aoeu.eu/?lang=en')

    typing = browser.find_element_by_css_selector('#wordsbox #input')

    while True:
        try:
            word = browser.find_element_by_class_name('currentword').text + ' '

            if sleeptime == 'no':
                typing.send_keys(word)
            else:
                for letter in word:
                    time.sleep(sleeptime)
                    typing.send_keys(letter)
        except:
            break

    result = browser.find_element_by_css_selector('#result').text[4:]
    print('This bot\'s' + result)

    time.sleep(4)


main()
