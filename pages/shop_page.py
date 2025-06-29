from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ShopPage(BasePage):

    TEXT_ABOVE_SHOP = "//div[@class='navbar-brand' and contains(text(), 'Продукты')]"
    PRODUCT_SHOP_QUANTITY_ICON = "//span[contains(@class, 'cart-counter') and contains(@class, 'badge')]"

    def __init__(self, driver):
        super().__init__(driver)

    def get_product_image(self, name):
        xpath = f"//div[contains(., '{name}')]/ancestor::div[contains(@class, 'card')]//img"
        return self.wait_for_element(By.XPATH, xpath)

    def get_product_price(self, name):
        xpath = f"//div[contains(., '{name}')]/ancestor::div[contains(@class, 'card')]//div[contains(text(), '₽')]"
        return self.wait_for_element(By.XPATH, xpath)

    def get_price_value(self, name):
        return float(self.get_product_price(name).text.replace('₽', '').strip())

    def get_product_description(self, name):
        xpath = f"//div[contains(., '{name}')]/ancestor::div[contains(@class, 'card')]//div[contains(text(), ' г')]"
        return self.wait_for_element(By.XPATH, xpath)

    def get_product_add_button(self, name):
        xpath = f"//div[contains(., '{name}')]/ancestor::div[contains(@class, 'card')]//button[.//span[text()='add']]"
        return self.wait_for_click(By.XPATH, xpath)

    def get_product_remove_button(self, name):
        xpath = f"//div[contains(., '{name}')]/ancestor::div[contains(@class, 'card')]//button[.//span[text()='remove']]"
        return self.wait_for_click(By.XPATH, xpath)

    def add_product(self, name):
        self.get_product_add_button(name).click()

    def remove_product(self, name):
        self.get_product_remove_button(name).click()

    def text_above_shop(self):
        return self.wait_for_element(By.XPATH, self.TEXT_ABOVE_SHOP).text

    def get_product_shop_quantity_icon(self):
        return int(self.wait_for_element(By.XPATH, self.PRODUCT_SHOP_QUANTITY_ICON).text.strip())

    def clear_icon_shop(self, name):
        while self.get_product_shop_quantity_icon() > 0:
            self.remove_product(name)

    def buy_many_products(self, name, quantity):
        for i in range(quantity):
            self.add_product(name)

    def clear_and_buy(self, name, quantity):
        self.clear_icon_shop(name)
        self.buy_many_products(name, quantity)


