'''
1. Открыть страницу http://suninjuly.github.io/redirect_accept.html
2. Нажать на кнопку
3. Переключиться на новую вкладку
4. Пройти капчу для робота и получить число-ответ
'''
import math
from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\Py_Projects\chromedriver\chromedriver.exe")
driver.get("http://suninjuly.github.io/redirect_accept.html")

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

driver.find_element_by_css_selector('.btn-primary').click()

new_window = driver.window_handles[1] #Определяем имя нового окна
driver.switch_to_window(new_window) #Переключаемся на новое окно

x = driver.find_element_by_id('input_value').text
driver.find_element_by_id('answer').send_keys(calc(x))
driver.find_element_by_css_selector('.btn-primary').click()