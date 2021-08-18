'''
Загрузка файла:
1. Открыть страницу http://suninjuly.github.io/file_input.html
2. Заполнить текстовые поля: имя, фамилия, email
3. Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
4. Нажать кнопку "Submit"
'''
import os, time
from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\Py_Projects\chromedriver\chromedriver.exe")
driver.get("http://suninjuly.github.io/file_input.html")

#Заполняем текстовые поля (ищем по значению атрибута name)
driver.find_element_by_name('firstname').send_keys('Игорь')
driver.find_element_by_name('lastname').send_keys('Насыров')
driver.find_element_by_name('email').send_keys('flashikk@inbox.ru')

''' 
Можно создать файл средствами питона
    with open("test.txt", "w") as file:
        content = file.write("automationbypython")  # create test.txt file
'''

#Получаем путь к директории текущего исполняемого файла
current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'test.txt') #добавляем к этому пути имя файла

#Находим кнопку и передаем ей путь к файлу file_path
driver.find_element_by_name('file').send_keys(file_path)

#Нажимаем кнопку Submit
driver.find_element_by_css_selector('.btn-primary').click()