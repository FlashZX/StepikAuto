'''
Пишем юниттесты:
1. Перепишите в стиле unittest тест для страницы http://suninjuly.github.io/registration1.html
2. Перепишите в стиле unittest второй тест для страницы http://suninjuly.github.io/registration2.html
3. Оформите финальные проверки в тестах в стиле unittest, например, используя проверочный метод assertEqual
4. Запустите получившиеся тесты из файла
5. Просмотрите отчёт о запуске и найдите сообщение об ошибке
'''
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
browser = webdriver.Chrome(executable_path="C:\Py_Projects\chromedriver\chromedriver.exe")

link1 = "http://suninjuly.github.io/registration1.html"
link2 = "http://suninjuly.github.io/registration2.html"

# Тестовый класс, наследник TestCase. Имена тестовых методов в нем должны начинаться с test_
class TestReg(unittest.TestCase):
    def test_reg1(self):
        browser.get(link1)
        self.assertEqual(input_values(),
                         "Congratulations! You have successfully registered!", "Welcome text is wrong!")
    def test_reg2(self):
        browser.get(link2)
        self.assertEqual(input_values(),
                         "Congratulations! You have successfully registered!", "Welcome text is wrong!")

# Метод с логикой выполнения на странице
def input_values():
    browser.find_element(By.XPATH, "//*[@placeholder='Input your first name']").send_keys("Иван")
    browser.find_element(By.XPATH, "//*[@placeholder='Input your last name']").send_keys("Петров")
    browser.find_element(By.XPATH, "//*[@placeholder='Input your email']").send_keys("1@1.ru")
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()
    return browser.find_element_by_tag_name("h1").text

# Указываем точку входа (скрипт запускается на прямую, а не вызван в качестве модуля)
if __name__ == "__main__":
    unittest.main()