import allure
from pages.main_page import MainPage
from data import RedirectData


class TestLogoRedirect:
    @allure.title("Лого Самоката возвращает на главную страницу")
    def test_logo_scooter_redirect_to_main(self, driver):
        page = MainPage(driver)
        page.click_order_header()
        page.click_logo_scooter()
        assert page.is_main_opened()

    @allure.title("Лого Яндекса открывает Дзен в новой вкладке")
    def test_logo_yandex_redirect_to_dzen(self, driver):
        page = MainPage(driver)
        page.click_logo_yandex()
        page.switch_to_new_tab()
        page.wait_url_contains("dzen")
        assert RedirectData.DZEN_URL_PART in page.get_current_url()
