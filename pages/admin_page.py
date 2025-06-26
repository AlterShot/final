import time

from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class AdminPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def get_edit_page_url(self):
        return self.driver.current_url

    def edit_page_text(self):
        xpath = "//div[@class='navbar-brand' and contains(., 'Редактирование: Товары')]"
        return self.wait_for_element(By.XPATH, xpath).text

    def edit_product_text(self):
        xpath = "//div[@class='navbar-brand' and contains(., 'Редактирование: Товар')]"
        return self.wait_for_element(By.XPATH, xpath).text

    def add_product_button(self):
        xpath = "//button[contains(., 'Добавить товар')]"
        return self.wait_for_element(By.XPATH, xpath)

    def add_product_button_click(self):
        self.add_product_button().click()

    def new_product_input_name(self):
        xpath = "//input[@placeholder='Наименование']"
        return self.wait_for_element(By.XPATH, xpath)

    def new_product_input_description(self):
        xpath = "//input[@placeholder='Описание']"
        return self.wait_for_element(By.XPATH, xpath)

    def new_product_input_exp_category(self):
        xpath = "//input[@placeholder='Ожидаемая категория']"
        return self.wait_for_element(By.XPATH, xpath)

    def new_product_input_price(self):
        xpath = "//input[@placeholder='Цена']"
        return self.wait_for_element(By.XPATH, xpath)

    def new_product_input_pic_url(self):
        xpath = "//input[@placeholder='Image Source']"
        return self.wait_for_element(By.XPATH, xpath)

    def add_product_full_info_input(self):
        name = "Хот-дог"
        item_name = f"{name} с курицей"
        description = f"{name} 200 г"
        exp_category = name
        price = "200"
        pic_url = "https://volshebnaya-eda.ru/wp-content/uploads/2019/09/datskij-xot-dog-10.jpg"
        self.new_product_input_name().send_keys(item_name)
        self.new_product_input_description().send_keys(description)
        self.new_product_input_exp_category().send_keys(exp_category)
        self.new_product_input_price().send_keys(price)
        self.new_product_input_pic_url().send_keys(pic_url)

    def back_to_product_edit_button(self):
        xpath = "//button[contains(., 'Обратно к товарам')]"
        return self.wait_for_element(By.XPATH, xpath)

    def create_product_button(self):
        xpath = "//button[contains(., 'Создать товар')]"
        return self.wait_for_element(By.XPATH, xpath)

    def back_to_product_edit_button_click(self):
        self.back_to_product_edit_button().click()

    def create_product_button_click(self):
        if self.create_product_button().is_enabled():
            self.create_product_button().click()
        else:
            time.sleep(2)
            self.create_product_button().click()