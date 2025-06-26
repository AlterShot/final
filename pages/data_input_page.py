from selenium.webdriver.common.by import By
from faker import Faker

from pages.base_page import BasePage


class DataInputPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def input_page_text_check(self):
        xpath = '//div[@class="navbar-brand" and contains(text(), "Оформление")]'
        return self.wait_for_element(By.XPATH, xpath)

    def get_current_url(self):
        return self.driver.current_url

    def name_input_box(self):
        xpath = '//input[@placeholder="Имя"]'
        return self.wait_for_element(By.XPATH, xpath)

    def surname_input_box(self):
        xpath = '//input[@placeholder="Фамилия"]'
        return self.wait_for_element(By.XPATH, xpath)

    def father_name_input_box(self):
        xpath = '//input[@placeholder="Отчество"]'
        return self.wait_for_element(By.XPATH, xpath)

    def address_input_box(self):
        xpath = '//input[@placeholder="Адрес доставки"]'
        return self.wait_for_element(By.XPATH, xpath)

    def card_number_input_box(self):
        xpath = '//input[@placeholder="Номер карты"]'
        return self.wait_for_element(By.XPATH, xpath)

    def back_to_shop_button(self):
        xpath = '//button[@class="btn btn-dark text-light text-end px-5"]'
        return self.wait_for_element(By.XPATH, xpath)

    def proceed_purchase_button(self):
        xpath = '//button[@class="btn btn-success text-light text-end px-5"]'
        return self.wait_for_element(By.XPATH, xpath)

    def back_to_shop_button_click(self):
        self.back_to_shop_button().click()

    def proceed_purchase_button_click(self):
        self.proceed_purchase_button().click()

    def fill_the_blanks(self):
        faker = Faker("ru_RU")
        self.name_input_box().send_keys(faker.first_name())
        self.surname_input_box().send_keys(faker.last_name())
        self.father_name_input_box().send_keys(faker.patronymic())
        self.address_input_box().send_keys(faker.street_address())
        self.card_number_input_box().send_keys(faker.credit_card_number())



