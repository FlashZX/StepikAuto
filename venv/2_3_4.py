'''
1. Открыть страницу http://suninjuly.github.io/alert_accept.html
2. Нажать на кнопку
3. Принять confirm
4. На новой странице решить капчу для роботов, чтобы получить число с ответом
'''
import math
from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\Py_Projects\chromedriver\chromedriver.exe")
driver.get("http://suninjuly.github.io/alert_accept.html")

#решаем задачу со страницы - "What is ln(abs(12*sin(x)))" и возвращаем в виде строки
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

driver.find_element_by_css_selector('.btn-primary').click()
#Переключаемся на алерт окно и акцептуем
driver.switch_to.alert.accept()

x = driver.find_element_by_id('input_value').text
driver.find_element_by_id('answer').send_keys(calc(x))
driver.find_element_by_css_selector('.btn-primary').click()