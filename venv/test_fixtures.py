# Пример использования автофикстур pytest и меток
# Запуск по меткам pytest -s -v --tb=line -m smoke ..имя файла..
# Описание меток в файле pytest.ini в корне
import pytest
from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture
def browser():
    print("\nstart browser for test..")
    driver = webdriver.Chrome(executable_path="C:\Py_Projects\chromedriver\chromedriver.exe")
    yield driver
    print("\nquit browser..")
    driver.quit()

@pytest.fixture(scope='class', autouse=True)
def prepare_data():
    print()
    print("preparing some critical data for every test")


class TestMainPage1():
    @pytest.mark.smoke
    def test_guest_should_see_login_link(self, browser):
        # не передаём как параметр фикстуру prepare_data, но она все равно выполняется
        browser.get(link)
        browser.find_element_by_css_selector("#login_link")

    @pytest.mark.regress
    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector(".basket-mini .btn-group > a")