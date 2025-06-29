from selenium.webdriver.common.by import By
from faker import Faker

from pages.base_page import BasePage


class DataInputPage(BasePage):

    INPUT_PAGE_TEXT_CHECK = '//div[@class="navbar-brand" and contains(text(), "Оформление")]'
    NAME_INPUT_BOX = '//input[@placeholder="Имя"]'
    SURNAME_INPUT_BOX = '//input[@placeholder="Фамилия"]'
    FATHER_NAME_INPUT_BOX = '//input[@placeholder="Отчество"]'
    ADDRESS_INPUT_BOX = '//input[@placeholder="Адрес доставки"]'
    CARD_NUMBER_INPUT_BOX = '//input[@placeholder="Номер карты"]'
    BACK_TO_SHOP_BUTTON = '//button[@class="btn btn-dark text-light text-end px-5"]'
    PROCEED_PURCHASE_BUTTON = '//button[@class="btn btn-success text-light text-end px-5"]'

    def __init__(self, driver):
        super().__init__(driver)

    def get_current_url(self):
        return self.driver.current_url

    def input_page_text_check(self):
        return self.wait_for_element(By.XPATH, self.INPUT_PAGE_TEXT_CHECK)

    def name_input_box(self):
        return self.wait_for_element(By.XPATH, self.NAME_INPUT_BOX)

    def surname_input_box(self):
        return self.wait_for_element(By.XPATH, self.SURNAME_INPUT_BOX)

    def father_name_input_box(self):
        return self.wait_for_element(By.XPATH, self.FATHER_NAME_INPUT_BOX)

    def address_input_box(self):
        return self.wait_for_element(By.XPATH, self.ADDRESS_INPUT_BOX)

    def card_number_input_box(self):
        return self.wait_for_element(By.XPATH, self.CARD_NUMBER_INPUT_BOX)

    def back_to_shop_button(self):
        return self.wait_for_element(By.XPATH, self.BACK_TO_SHOP_BUTTON)

    def back_to_shop_button_click(self):
        self.back_to_shop_button().click()

    def proceed_purchase_button(self):
        return self.wait_for_element(By.XPATH, self.PROCEED_PURCHASE_BUTTON)

    def proceed_purchase_button_click(self):
        self.proceed_purchase_button().click()

    def generate_patronymic(self, faker):
        father_name = faker.first_name_male()
        if father_name.endswith("й"):
            return father_name[:-1] + "евич"
        elif father_name.endswith("а"):
            return father_name[:-1] + "ич"
        else:
            return father_name + "ович"

    def fill_the_blanks(self):
        faker = Faker("ru_RU")
        self.name_input_box().send_keys(faker.first_name_male())
        self.surname_input_box().send_keys(faker.last_name_male())
        self.father_name_input_box().send_keys(self.generate_patronymic(faker))
        self.address_input_box().send_keys(faker.street_address())
        self.card_number_input_box().send_keys(faker.credit_card_number())
