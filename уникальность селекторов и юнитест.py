from selenium import webdriver
import time
import unittest


class TestAbs(unittest.TestCase):
    def test_abs1(self):
        try:
            link = "http://suninjuly.github.io/registration1.html"
            browser = webdriver.Chrome()
            browser.get(link)

            input1 = browser.find_element_by_css_selector('.first_block>.form-group.first_class> input')
            input1.send_keys("Yev")
            input2 = browser.find_element_by_css_selector('.first_block>.form-group.second_class> input')
            input2.send_keys("Mot")
            input3 = browser.find_element_by_css_selector('.first_block>.form-group.third_class> input')
            input3.send_keys("mot@gm")

            # Отправляем заполненную форму
            button = browser.find_element_by_css_selector("button.btn")
            button.click()

            # Проверяем, что смогли зарегистрироваться
            # ждем загрузки страницы
            time.sleep(1)

            # находим элемент, содержащий текст
            welcome_text_elt = browser.find_element_by_tag_name("h1")
            # записываем в переменную welcome_text текст из элемента welcome_text_elt
            welcome_text = welcome_text_elt.text

            # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
            self.assertEqual (browser.find_element_by_tag_name("h1").text, "Congratulations! You have successfully registered!", 'Error Registration 1')

        finally:
            # ожидание чтобы визуально оценить результаты прохождения скрипта
            time.sleep(10)
            # закрываем браузер после всех манипуляций
            browser.quit()

    def test_abs2(self):
        try:
            link = "http://suninjuly.github.io/registration2.html"
            browser = webdriver.Chrome()
            browser.get(link)

            input1 = browser.find_element_by_css_selector('.first_block>.form-group.first_class> input')
            input1.send_keys("Yev")
            input2 = browser.find_element_by_css_selector('.first_block>.form-group.second_class> input')
            input2.send_keys("Mot")
            input3 = browser.find_element_by_css_selector('.first_block>.form-group.third_class> input')
            input3.send_keys("mot@gm")

            # Отправляем заполненную форму
            button = browser.find_element_by_css_selector("button.btn")
            button.click()

            # Проверяем, что смогли зарегистрироваться
            # ждем загрузки страницы
            time.sleep(1)

            # находим элемент, содержащий текст
            welcome_text_elt = browser.find_element_by_tag_name("h1")
            # записываем в переменную welcome_text текст из элемента welcome_text_elt
            welcome_text = welcome_text_elt.text

            # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
            self.assertEqual (browser.find_element_by_tag_name("h1").text, "Congratulations! You have successfully registered!", 'Error Registration 1')

        finally:
            # ожидание чтобы визуально оценить результаты прохождения скрипта
            time.sleep(10)
            # закрываем браузер после всех манипуляций
            browser.quit()


if __name__ == "__main__":
    unittest.main()