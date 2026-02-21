from selenium.webdriver.common.by import By


class MainPageLocators:
    # Кнопки "Заказать"
    ORDER_BUTTON_HEADER = (By.XPATH, "//div[contains(@class,'Header_Nav')]/button[text()='Заказать']")
    ORDER_BUTTON_BOTTOM = (By.XPATH, "//div[contains(@class,'Home_FinishButton')]/button")
    COOKIES_BUTTON = (By.ID, "rcc-confirm-button")

    # FAQ
    FAQ_SECTION = (By.XPATH, "//div[contains(@class,'Home_FAQ')]")
    FAQ_QUESTION = lambda index: (By.ID, f"accordion__heading-{index}")
    FAQ_ANSWER = lambda index: (By.ID, f"accordion__panel-{index}")

    # Логотипы
    LOGO_SCOOTER = (By.XPATH, "//a[contains(@class,'Header_LogoScooter')]")
    LOGO_YANDEX = (By.XPATH, "//a[contains(@class,'Header_LogoYandex')]")

    # Признак главной страницы
    MAIN_HEADER = (By.XPATH, "//div[contains(@class,'Home_Header')]")

