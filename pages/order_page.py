import allure
from selenium.webdriver.common.keys import Keys

from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators
from locators.main_page_locators import MainPageLocators


class OrderPage(BasePage):

    @allure.step("Заполнить форму 'Для кого самокат'")
    def fill_personal_form(self, data: dict):
        self.click_if_present(MainPageLocators.COOKIES_BUTTON)

        self.set_value(OrderPageLocators.NAME, data["name"])
        self.set_value(OrderPageLocators.LAST_NAME, data["last_name"])
        self.set_value(OrderPageLocators.ADDRESS, data["address"])

        self.click(OrderPageLocators.METRO)
        self.set_value(OrderPageLocators.METRO, data["metro"])
        self.click(OrderPageLocators.METRO_OPTION)

        self.set_value(OrderPageLocators.PHONE, data["phone"])
        self.click(OrderPageLocators.NEXT_BUTTON)

    @allure.step("Выбрать цвет самоката: {color}")
    def select_color(self, color: str):
        color_locator = {
            "black": OrderPageLocators.COLOR_BLACK,
            "grey": OrderPageLocators.COLOR_GREY,
        }
        self.click(color_locator[color])

    @allure.step("Заполнить форму 'Про аренду'")
    def fill_rent_form(self, data: dict):
        self.click_if_present(MainPageLocators.COOKIES_BUTTON)

        self.click(OrderPageLocators.DATE)
        self.set_value(OrderPageLocators.DATE, data["date"])
        self.press_enter(OrderPageLocators.DATE)

        self.click(OrderPageLocators.RENT_PERIOD)
        self.click(OrderPageLocators.DROPDOWN_OPTION(data["rent_period"]))

        self.select_color(data["color"])

        self.set_value(OrderPageLocators.COMMENT, data["comment"])

        self.click(OrderPageLocators.ORDER_BUTTON)

        self.wait_visibility(OrderPageLocators.CONFIRM_YES)
        self.click(OrderPageLocators.CONFIRM_YES)

    @allure.step("Проверить, что заказ успешно создан")
    def is_order_created(self):
        self.wait_visibility(OrderPageLocators.STATUS_BUTTON)
        return True
