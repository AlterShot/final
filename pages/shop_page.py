from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ShopPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def get_product_image(self, name):
        xpath = f"//div[contains(., '{name}')]/ancestor::div[contains(@class, 'card')]//img"
        return self.wait_for_element(By.XPATH, xpath)

    def get_product_price(self, name):
        xpath = f"//div[contains(., '{name}')]/ancestor::div[contains(@class, 'card')]//div[contains(text(), '₽')]"
        return self.wait_for_element(By.XPATH, xpath)

    def get_price_value(self, name):
        price_value = int(self.get_product_price(name).text.replace('₽', '').strip())
        return price_value

    def get_product_description(self, name):
        xpath = f"//div[contains(., '{name}')]/ancestor::div[contains(@class, 'card')]//div[contains(text(), ' г')]"
        return self.wait_for_element(By.XPATH, xpath)

    def get_product_add_button(self, name):
        xpath = f"//div[contains(., '{name}')]/ancestor::div[contains(@class, 'card')]//button[contains(text(), 'add')]"
        return self.wait_for_element(By.XPATH, xpath)

    def get_product_remove_button(self, name):
        xpath = f"//div[contains(., '{name}')]/ancestor::div[contains(@class, 'card')]//button[contains(text(), 'remove')]"
        return self.wait_for_element(By.XPATH, xpath)

    def add_product(self, name):
        self.get_product_add_button(name).click()

    def remove_product(self, name):
        self.get_product_remove_button(name).click()

    def text_above_shop(self):
        xpath = f"//div[@class='navbar-brand' and contains(text(), 'Продукты')]"
        text = self.wait_for_element(By.XPATH, xpath).text
        return text

    def get_product_shop_quantity(self, name):
        xpath = f"//div[contains(., '{name}')]/ancestor::div[contains(@class, 'card')]//input[contains(@class, 'shadow-form')]"
        return self.wait_for_element(By.XPATH, xpath)
