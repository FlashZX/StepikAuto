'''
Ваша программа должна выполнить следующие шаги:
1. Открыть страницу http://suninjuly.github.io/math.html.
2. Считать значение для переменной x.
3. Посчитать математическую функцию от x (код для этого приведён ниже).
4. Ввести ответ в текстовое поле.
5. Отметить checkbox "I'm the robot".
6. Выбрать radiobutton "Robots rule!".
7. Нажать на кнопку Submit.
'''

import math
from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\Py_Projects\chromedriver\chromedriver.exe")
driver.get("http://suninjuly.github.io/math.html")

#решаем задачу со страницы - "What is ln(abs(12*sin(x)))" и возвращаем в виде строки
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

#Находим эелемент и присваеваем переменной x его атрибут .text
x = driver.find_element_by_css_selector('#input_value').text
#Находим инпут и вводим в него результат вычесления функции от x
driver.find_element_by_css_selector('.form-control').send_keys(calc(x))
#Отмечаем checkbox "I'm the robot"
driver.find_element_by_css_selector('#robotCheckbox').click()
#Выбраем radiobutton "Robots rule!" и нажимаем кнопку Submit
driver.find_element_by_css_selector('#robotsRule').click()
driver.find_element_by_css_selector('.btn-default').click()