from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class AdminPage(BasePage):

    EDIT_PAGE_TEXT = "//div[@class='navbar-brand' and contains(., 'Редактирование: Товары')]"
    EDIT_PRODUCT_TEXT = "//div[@class='navbar-brand' and contains(., 'Редактирование: Товар')]"

    NEW_PRODUCT_INPUT_NAME = "//input[@placeholder='Наименование']"
    NEW_PRODUCT_INPUT_DESCRIPTION = "//input[@placeholder='Описание']"
    NEW_PRODUCT_INPUT_EXP_CATEGORY = "//input[@placeholder='Ожидаемая категория']"
    NEW_PRODUCT_INPUT_PRICE = "//input[@placeholder='Цена']"
    NEW_PRODUCT_PIC_URL = "//input[@placeholder='Image Source']"

    ADD_PRODUCT_BUTTON = "//button[contains(., 'Добавить товар')]"
    BACK_TO_PRODUCT_EDIT_BUTTON = "//button[contains(., 'Обратно к товарам')]"
    CREATE_PRODUCT_BUTTON = "//button[contains(., 'Создать товар')]"
    CONFIRM_REFRESHING_BUTTON = "//button[contains(., 'Обновить товар')]"

    def __init__(self, driver):
        super().__init__(driver)

    def get_edit_page_url(self):
        return self.driver.current_url

    def edit_page_text(self):
        return self.wait_for_element(By.XPATH, self.EDIT_PAGE_TEXT).text

    def edit_product_text(self):
        return self.wait_for_element(By.XPATH, self.EDIT_PRODUCT_TEXT).text

    def new_product_input_name(self):
        return self.wait_for_element(By.XPATH, self.NEW_PRODUCT_INPUT_NAME)

    def new_product_input_description(self):
        return self.wait_for_element(By.XPATH, self.NEW_PRODUCT_INPUT_DESCRIPTION)

    def new_product_input_exp_category(self):
        return self.wait_for_element(By.XPATH, self.NEW_PRODUCT_INPUT_EXP_CATEGORY)

    def new_product_input_price(self):
        return self.wait_for_element(By.XPATH, self.NEW_PRODUCT_INPUT_PRICE)

    def new_product_input_pic_url(self):
        return self.wait_for_element(By.XPATH, self.NEW_PRODUCT_PIC_URL)

    def add_product_button(self):
        return self.wait_for_click(By.XPATH, self.ADD_PRODUCT_BUTTON)

    def add_product_button_click(self):
        self.add_product_button().click()

    def back_to_product_edit_button(self):
        return self.wait_for_click(By.XPATH, self.BACK_TO_PRODUCT_EDIT_BUTTON)

    def create_product_button(self):
        return self.wait_for_click(By.XPATH, self.CREATE_PRODUCT_BUTTON)

    def back_to_product_edit_button_click(self):
        self.back_to_product_edit_button().click()

    def create_product_button_click(self):
        self.create_product_button().click()

    def product_edit_button(self, name):
        xpath = f"//div[.//div[contains(@class, 'card-title') and text()='{name}']]//button[contains(@class, 'btn-outline-success')]"
        return self.wait_for_click(By.XPATH, xpath)

    def product_edit_button_click(self, name):
        self.product_edit_button(name).click()

    def product_delete_button(self, name):
        xpath = f"//div[.//div[contains(@class, 'card-title') and text()='{name}']]//button[contains(@class, 'btn-outline-danger')]"
        return self.wait_for_click(By.XPATH, xpath)

    def product_delete_button_click(self, name):
        self.product_delete_button(name).click()

    def confirm_refreshing_button(self):
        return self.wait_for_click(By.XPATH, self.CONFIRM_REFRESHING_BUTTON)

    def confirm_refreshing_button_click(self):
        self.confirm_refreshing_button().click()

    def is_product_displayed(self, name):
        return self.wait_for_text_on_page(name)

    def _fill_box_after_clearing(self, item_name, description, exp_category, price, pic_url):
        self.new_product_input_name().clear()
        self.new_product_input_name().send_keys(item_name)
        self.new_product_input_description().clear()
        self.new_product_input_description().send_keys(description)
        self.new_product_input_exp_category().clear()
        self.new_product_input_exp_category().send_keys(exp_category)
        self.new_product_input_price().clear()
        self.new_product_input_price().send_keys(price)
        self.new_product_input_pic_url().clear()
        self.new_product_input_pic_url().send_keys(pic_url)

    def fill_the_blanks(self, item_name, description, exp_category, price, pic_url):
        self._fill_box_after_clearing(item_name, description, exp_category, price, pic_url)
