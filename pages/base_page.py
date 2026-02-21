import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    ElementClickInterceptedException,
    StaleElementReferenceException,
)
from selenium.webdriver.common.keys import Keys


class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    @allure.step("Ожидать видимость элемента: {locator}")
    def wait_visibility(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step("Ожидать кликабельность элемента: {locator}")
    def wait_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    @allure.step("Ожидать исчезновение элемента: {locator}")
    def wait_invisibility(self, locator):
        return self.wait.until(EC.invisibility_of_element_located(locator))

    @allure.step("Скролл к элементу (центр экрана): {locator}")
    def scroll_to(self, locator):
        element = self.wait_visibility(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        return element

    @allure.step("Клик по элементу (safe click): {locator}")
    def click(self, locator):
        element = self.scroll_to(locator)
        try:
            self.wait_clickable(locator).click()
        except ElementClickInterceptedException:
            self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Клик по элементу, если он есть на странице: {locator}")
    def click_if_present(self, locator):
        try:
            elements = self.driver.find_elements(*locator)
            if not elements:
                return False

            try:
                elements[0].click()
            except ElementClickInterceptedException:
                self.driver.execute_script("arguments[0].click();", elements[0])

            return True
        except StaleElementReferenceException:
            elements = self.driver.find_elements(*locator)
            if not elements:
                return False
            try:
                elements[0].click()
            except ElementClickInterceptedException:
                self.driver.execute_script("arguments[0].click();", elements[0])
            return True

    @allure.step("Ввести текст в поле {locator}: {value}")
    def set_value(self, locator, value):
        element = self.wait_visibility(locator)
        element.clear()
        element.send_keys(value)

    @allure.step("Нажать Enter в поле {locator}")
    def press_enter(self, locator):
        self.wait_visibility(locator).send_keys(Keys.ENTER)

    @allure.step("Получить текст элемента: {locator}")
    def get_text(self, locator):
        return self.wait_visibility(locator).text

    @allure.step("Получить текущий URL")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Переключиться на новую вкладку")
    def switch_to_new_tab(self):
        self.wait.until(lambda d: len(d.window_handles) == 2)
        self.driver.switch_to.window(self.driver.window_handles[1])

    @allure.step("Ожидать URL содержит '{text}'")
    def wait_url_contains(self, text: str):
        self.wait.until(EC.url_contains(text))
