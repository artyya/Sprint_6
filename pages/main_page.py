import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):

    @allure.step("Скролл к FAQ")
    def scroll_to_faq(self):
        self.scroll_to(MainPageLocators.FAQ_SECTION)

    @allure.step("Клик по вопросу FAQ с индексом {index}")
    def click_faq_question(self, index: int):
        self.click(MainPageLocators.FAQ_QUESTION(index))

    @allure.step("Получить текст ответа FAQ с индексом {index}")
    def get_faq_answer_text(self, index: int):
        return self.get_text(MainPageLocators.FAQ_ANSWER(index))

    @allure.step("Клик по кнопке 'Заказать' в шапке")
    def click_order_header(self):
        self.click(MainPageLocators.ORDER_BUTTON_HEADER)

    @allure.step("Клик по кнопке 'Заказать' внизу страницы")
    def click_order_bottom(self):
        self.click(MainPageLocators.ORDER_BUTTON_BOTTOM)

    @allure.step("Клик по лого Самокат")
    def click_logo_scooter(self):
        self.click(MainPageLocators.LOGO_SCOOTER)

    @allure.step("Клик по лого Яндекс")
    def click_logo_yandex(self):
        self.click(MainPageLocators.LOGO_YANDEX)

    @allure.step("Проверка, что открыта главная страница")
    def is_main_opened(self):
        self.wait_visibility(MainPageLocators.MAIN_HEADER)
        return True
