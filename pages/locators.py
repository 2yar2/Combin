from selenium.webdriver.common.by import By

class MainPageLocators():
# выключаем плашку с сообщением про кукис
    COOKIES_CLOSE = (By.CLASS_NAME, "icon__ic-cross")
    GROWTH = (By.ID, "0")
    ADVANCED = (By.ID, "1")
    GENDER = (By.ID, "2")
    MACHINE = (By.ID, "3")
    AUDIENCE = (By.ID, "4")
    REPETITIVE = (By.ID, "5")
    MULTIPLE = (By.ID, "6")
