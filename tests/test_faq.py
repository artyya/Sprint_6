import allure
import pytest
from pages.main_page import MainPage
from data import FaqData


class TestFaq:
    @allure.title("FAQ: при клике на вопрос показывается корректный ответ")
    @allure.description("Проверка текста ответа для каждого вопроса в разделе 'Вопросы о важном'.")
    @pytest.mark.parametrize("index, expected", FaqData.expected_answers)
    def test_faq_answer_text(self, driver, index, expected):
        page = MainPage(driver)
        page.scroll_to_faq()
        page.click_faq_question(index)
        assert page.get_faq_answer_text(index) == expected
