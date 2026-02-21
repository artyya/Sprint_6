import allure
import pytest
from pages.main_page import MainPage
from pages.order_page import OrderPage
from data import OrderData
from locators.main_page_locators import MainPageLocators


class TestOrderFlow:
    @allure.title("Позитивный сценарий заказа самоката")
    @allure.description("Полный e2e flow заказа с двумя точками входа и двумя наборами данных")
    @pytest.mark.parametrize(
        "open_order_method, order_data",
        [
            ("click_order_header", OrderData.user_1),
            ("click_order_bottom", OrderData.user_2),
        ],
    )
    def test_order_success(self, driver, open_order_method, order_data):
        main = MainPage(driver)
        main.click_if_present(MainPageLocators.COOKIES_BUTTON)

        # Открытие формы заказа без ветвления в тесте
        getattr(main, open_order_method)()

        order = OrderPage(driver)
        order.fill_personal_form(order_data)
        order.fill_rent_form(order_data)

        assert order.is_order_created()
