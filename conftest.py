import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from urls import BASE_URL


@pytest.fixture(scope="function")
def driver():
    options = Options()
    driver = webdriver.Firefox(options=options)
    driver.set_window_size(1280, 720)

    driver.get(BASE_URL)
    yield driver
    driver.quit()
