'''
Напишите код, который реализует следующий сценарий:
1. Открыть страницу http://suninjuly.github.io/selects1.html
2. Посчитать сумму заданных чисел
3. Выбрать в выпадающем списке значение равное расчитанной сумме
4. Нажать кнопку "Submit"
'''
from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(executable_path="C:\Py_Projects\chromedriver\chromedriver.exe")
driver.get("http://suninjuly.github.io/selects1.html")

#Находим значения элементов num1 и num2
num1 = int(driver.find_element_by_id('num1').text)
num2 = int(driver.find_element_by_id('num2').text)

#Выбираем из списка вариант == сумме num1 и num2
select = Select(driver.find_element_by_tag_name('select'))
select.select_by_value(str(num1 + num2))

#Кликаем по кнопке
driver.find_element_by_css_selector('.btn-default').click()