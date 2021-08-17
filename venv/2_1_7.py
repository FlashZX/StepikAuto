'''
Ваша программа должна выполнить следующие шаги:
1. Открыть страницу http://suninjuly.github.io/get_attribute.html.
2. Найти на ней элемент-картинку, который является изображением сундука с сокровищами.
3. Взять у этого элемента значение атрибута valuex, которое является значением x для задачи.
4. Посчитать математическую функцию от x (сама функция остаётся неизменной).
5. Ввести ответ в текстовое поле.
6. Отметить checkbox "I'm the robot".
7. Выбрать radiobutton "Robots rule!".
8. Нажать на кнопку "Submit".
'''
import math, time
from selenium import webdriver
driver = webdriver.Chrome(executable_path="C:\Py_Projects\chromedriver\chromedriver.exe")
driver.get("http://suninjuly.github.io/get_attribute.html")

#решаем задачу со страницы - "What is ln(abs(12*sin(x)))" и возвращаем в виде строки
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

treasure = driver.find_element_by_id('treasure')
#Достаем значение X из сундука по аттрибуту valuex
x = treasure.get_attribute('valuex')
#дальше кликаем в инпут, чекбокс, радиобатон и по кнопке
driver.find_element_by_id('answer').send_keys(calc(x))
driver.find_element_by_id('robotCheckbox').click()
driver.find_element_by_id('robotsRule').click()
driver.find_element_by_css_selector('.btn-default').click()