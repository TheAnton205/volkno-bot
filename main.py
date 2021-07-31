from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait
import pyautogui
from random import randint

#open website and maximize in chrome
driver = webdriver.Chrome("D:/Users/Anton/Desktop/programming/chromedriver")
driver.get("http://www.volkno.com")
driver.fullscreen_window()

#check xpath function
def check_xpath(xpath):
    try:
        driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True

#sign in
sign_in = driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/section[1]/div[2]/div/div[1]/div/div[1]/a[2]")
sign_in.click()
time.sleep(0.5)

email = driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/section[1]/div[2]/div/div[1]/div/div[2]/div/div[1]/form/div[1]/div/div/div/input")
email.send_keys("user")

time.sleep(0.5)
password = driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/section[1]/div[2]/div/div[1]/div/div[2]/div/div[1]/form/div[2]/div/div/div/input")
password.send_keys("pass")

time.sleep(0.5)
password.send_keys(Keys.ENTER)

counter = 0

def init_movie():
    time.sleep(3)
    Flow = driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[3]/div/div[2]/div[1]/div/div[2]/ul/li[2]/div[2]/div[2]")
    print(Flow.text)

    if Flow.text == "Flow Earned 200":
        pyautogui.click(x=606, y=640)
        time.sleep(2)
        x = randint(1,2)
        if x == 1:  
            pyautogui.click(x=520, y=535)
        time.sleep(10)

    else:
        pyautogui.click(x=600, y=590)
        time.sleep(2)
        x = randint(1,2)
        if x == 1:
            pyautogui.click(x=528, y=544)
        if x == 2:
            pyautogui.click(x=530, y=530)
        time.sleep(10)

time.sleep(5)
init_movie()


while True:

#initialize movie

    time.sleep(10)
    prevFlow = driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[1]/div/div[2]/div[2]/span")
    prevlow = prevFlow.text
    prevlow = int(prevFlow.replace(',',''))
    #-------------------check for all reactions--------------------

    #check for hot-or-not
    if (check_xpath("/html/body/div[1]/div/div/div/div[3]/div/div[2]/div[1]/div/div/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]")) == True:
        hot = driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[3]/div/div[2]/div[1]/div/div/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]").click()

    #check emoji
    if (check_xpath("/html/body/div[1]/div/div/div/div[3]/div/div[2]/div[1]/div/div/div[2]/div[2]/div[2]/div[1]/div[2]/div/div[5]/div/div")) == True:
        emoji = driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[3]/div/div[2]/div[1]/div/div/div[2]/div[2]/div[2]/div[1]/div[2]/div/div[5]/div/div").click()

    #love it
    if (check_xpath("/html/body/div[1]/div/div/div/div[3]/div/div[2]/div[1]/div/div/div[2]/div[2]/div[2]/div[1]/div[2]/div/div[2]/div/div[3]/div[1]")):
        love_it = driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[3]/div/div[2]/div[1]/div/div/div[2]/div[2]/div[2]/div[1]/div[2]/div/div[2]/div/div[3]/div[1]").click()

    #--------------------------------------------------------------
    time.sleep(200)


    demand = driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[3]/div/div[2]/div[1]/div/div/div[1]/div[1]/div/div[1]/div/div[2]/div[3]/div/button[1]").click()
    time.sleep(1)
    demand2 = driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div/div[2]/div[2]/div[11]").click()
    time.sleep(1)
    demand3 = driver.find_element_by_xpath("/html/body/div[4]/div/div/div/button/span").click()
    time.sleep(1)
    tag = driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[3]/div/div[2]/div[1]/div/div/div[1]/div[1]/div/div[1]/div/div[2]/div[3]/div/button[2]").click()
    time.sleep(1)
    tag2 = driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div/div/div/div/div/div[3]/div[2]").click()
    time.sleep(1)
    exit2 = driver.find_element_by_xpath("/html/body/div[4]/div/div/div/button/span").click()
    time.sleep(1)
    rate = driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[3]/div/div[2]/div[1]/div/div/div[1]/div[1]/div/div[1]/div/div[2]/div[3]/div/button[3]").click()
    time.sleep(1) 
    rate2 = driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div/form/div[1]/textarea").send_keys("cool!")
    time.sleep(1)
    send = driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div/form/div[3]/button").click()
    time.sleep(1)

    rate = driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[3]/div/div[2]/div[1]/div/div/div[1]/div[1]/div/div[2]/div[2]/div/div[1]/div[4]").click()

    time.sleep(2)

    newFlow = driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[1]/div/div[2]/div[2]/span")
    newlow = newFlow.text
    newlow = int(newFlow.replace(',',''))

    y = newFlow - prevFlow
    prevFlow = newFlow
    print("Current Flow = " + str(newFlow) + ". You gained " + str(y) + " flow.")

    counter += 1

    if (check_xpath("/html/body/div[1]/div/div/div/div[3]/div/div[2]/div[1]/div/div/div[1]/div[2]/a[1]")) == True:
        next_round = driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[3]/div/div[2]/div[1]/div/div/div[1]/div[2]/a[1]").click()
        time.sleep(5)
    elif (check_xpath("/html/body/div[1]/div/div/div/div[3]/div/div[2]/div[1]/div/div/div[1]/div[2]/a[2]")) == True:
        next_vid = driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[3]/div/div[2]/div[1]/div/div/div[1]/div[2]/a[2]")
    else:
        next = driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[3]/div/div[2]/div[1]/div/div/div[2]/div[2]/div[1]/a/img").click()
        time.sleep(2)


