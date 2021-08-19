'''
1. Открыть страницу http://suninjuly.github.io/explicit_wait2.html
2. Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
3. Нажать на кнопку "Book"
4. Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение
'''

import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

browser = webdriver.Chrome(executable_path="C:\Py_Projects\chromedriver\chromedriver.exe")
browser.get("http://suninjuly.github.io/explicit_wait2.html")

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

#Дожидаемся когда цена упадет до 100 баксов и кликаем на кнопку покупки
WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
browser.find_element_by_id('book').click()

#Высчитываем значение и нажимаем кнопку
x = browser.find_element_by_id('input_value').text
browser.find_element_by_id('answer').send_keys(calc(x))
browser.find_element_by_id('solve').click()

'''
Пример негативного правила с методом until_not
# говорим Selenium проверять в течение 5 секунд пока кнопка станет неактивной

button = WebDriverWait(browser, 5).until_not(
        EC.element_to_be_clickable((By.ID, "verify")))

Другие правила ожидания для expected_conditions:
https://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.support.expected_conditions
'''