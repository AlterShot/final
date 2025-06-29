from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.remote.webelement import WebElement


class LoginPage(BasePage):

    AT_SHOP_PAGE = '//a[@class="router-link-active router-link-exact-active navbar-brand"]'
    LOGIN_FIELD = '//input[@placeholder="Логин"]'
    PASSWORD_FIELD = '//input[@placeholder="Пароль"]'
    LOGIN_BUTTON = '//button[@class="btn btn-primary shadow-none rounded-1"]'

    def __init__(self, driver):
        super().__init__(driver)

    def at_shop_page(self) -> bool:
        return self.wait_for_text_element(By.XPATH, self.AT_SHOP_PAGE, 'Магазин')

    def login_field(self) -> WebElement:
        return self.driver.find_element(By.XPATH, self.LOGIN_FIELD)

    def password_field(self) -> WebElement:
        return self.driver.find_element(By.XPATH, self.PASSWORD_FIELD)

    def login_button(self) -> WebElement:
        return self.driver.find_element(By.XPATH, self.LOGIN_BUTTON)

    def login_button_click(self) -> None:
        self.login_button().click()

    def enter_username(self, username: str) -> None:
        username_field = self.login_field()
        username_field.clear()
        username_field.send_keys(username)

    def enter_password(self, password: str) -> None:
        password_field = self.password_field()
        password_field.clear()
        password_field.send_keys(password)

    def full_login_process(self, username, password) -> None:
        self.enter_username(username)
        self.enter_password(password)
        self.login_button_click()

