import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="function")
def browser():
    print("\nstart chrome browser for test..")
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.maximize_window()
    browser.implicitly_wait(30)
    yield browser
    print("\nquit browser..")
    browser.quit()
