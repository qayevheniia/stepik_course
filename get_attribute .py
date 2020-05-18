from selenium import webdriver
import time
import math

from selenium.webdriver.remote.webelement import WebElement


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id("treasure")
    x = x_element.get_attribute("valuex")
    # print("x=", x)
    print(x)
    y = calc(x)
    # print("y=", y)

    answer = browser.find_element_by_id("answer")
    answer.send_keys(y)


    option1 = browser.find_element_by_id("robotCheckbox")
    option1.click()

    option2 = browser.find_element_by_id("robotsRule")
    option2.click()

    button = browser.find_element_by_css_selector(".btn.btn-default")
    button.click()



finally:
    time.sleep(10)
    browser.quit()
