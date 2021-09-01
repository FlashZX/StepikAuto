import pytest, math, time
from selenium import webdriver
#from selenium.webdriver.common.by import By

links = ['236895', '236896', '236897', '236898',
         '236899', '236903', '236904', '236905']

def time_cod():
    return str(math.log(int(time.time())))

@pytest.fixture()
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome(executable_path="C:\Py_Projects\chromedriver\chromedriver.exe")
    browser.implicitly_wait(5)
    yield browser
    browser.quit()

@pytest.mark.parametrize('links', links)
def test_input_value_on_page(browser, links):
    browser.get(f'https://stepik.org/lesson/{links}/step/1')
    browser.find_element_by_css_selector(".ember-text-area").send_keys(time_cod())
    browser.find_element_by_css_selector(".submit-submission").click()
    temp = browser.find_element_by_css_selector(".smart-hints__hint").text
    assert temp == "Correct!", "А вот тут были инопланетяне!)"