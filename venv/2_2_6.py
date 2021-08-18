'''
1. Открыть страницу http://SunInJuly.github.io/execute_script.html.
2. Считать значение для переменной x.
3. Посчитать математическую функцию от x.
4. Проскроллить страницу вниз.
5. Ввести ответ в текстовое поле.
6. Выбрать checkbox "I'm the robot".
7. Переключить radiobutton "Robots rule!".
8. Нажать на кнопку "Submit".
'''
import math
from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\Py_Projects\chromedriver\chromedriver.exe")
driver.get("https://SunInJuly.github.io/execute_script.html")

#решаем задачу со страницы - "What is ln(abs(12*sin(x)))" и возвращаем в виде строки
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

#Находим эелемент и присваеваем переменной x его атрибут .text
x = driver.find_element_by_css_selector('#input_value').text
#Находим инпут и вводим в него результат вычесления функции от x
driver.find_element_by_css_selector('.form-control').send_keys(calc(x))
#Скроллим страницу вниз (сколл до элемента button), чтобы футер уехал с кнопки
button = driver.find_element_by_tag_name("button")
driver.execute_script("return arguments[0].scrollIntoView(true);", button)
#Отмечаем checkbox "I'm the robot"
driver.find_element_by_css_selector('#robotCheckbox').click()
#Выбраем radiobutton "Robots rule!" и нажимаем кнопку Submit
driver.find_element_by_css_selector('#robotsRule').click()
button.click()

'''
Варианты без JS кода:
1.  try:
        button = driver.find_element_by_tag_name("button")
        _ = button.location_once_scrolled_into_view
       button.click()
        assert True
    finally:
        driver.quit()
2. Скрыть ненужный элемент
    browser.execute_script('arguments[0].style.visibility = \'hidden\'', footer)

3. Проскроллить вверх или низ страницы можно и питоном для тега body
    from selenium.webdriver.common.keys import Keys
    driver.find_element_by_tag_name('body').send_keys(Keys.END) #или Home если наверх
'''