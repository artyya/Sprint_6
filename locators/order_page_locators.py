from selenium.webdriver.common.by import By


class OrderPageLocators:
    # Форма "Для кого самокат"
    NAME = (By.XPATH, "//input[@placeholder='* Имя']")
    LAST_NAME = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO = (By.XPATH, "//input[@placeholder='* Станция метро']")
    METRO_OPTION = (By.XPATH, "//li[contains(@class,'select-search__row')]")
    PHONE = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")

    # Форма "Про аренду"
    DATE = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENT_PERIOD = (By.XPATH, "//div[contains(@class,'Dropdown-placeholder')]")
    DROPDOWN_OPTION = lambda text: (
        By.XPATH,
        f"//div[contains(@class,'Dropdown-menu')]//div[text()='{text}']"
    )

    COLOR_BLACK = (By.XPATH, "//label[@for='black']")
    COLOR_GREY = (By.XPATH, "//label[@for='grey']")

    COMMENT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")

    #  кнопка "Заказать"
    ORDER_BUTTON = (
        By.XPATH,
        "//div[contains(@class,'Order_Buttons')]//button[text()='Заказать']"
    )

    # Модальное окно подтверждения
    MODAL = (By.XPATH, "//div[contains(@class,'Order_Modal')]")
    CONFIRM_YES = (By.XPATH, "//div[contains(@class,'Order_Modal')]//button[text()='Да']")

    # Успешное создание заказа
    STATUS_BUTTON = (By.XPATH, "//button[text()='Посмотреть статус']")

    # (опционально) куки, если всплывают и перекрывают клики
    COOKIES_BUTTON = (By.XPATH, "//button[contains(.,'да все привыкли')]")
