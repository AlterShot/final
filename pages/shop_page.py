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
        price_value = float(self.get_product_price(name).text.replace('₽', '').strip())
        return price_value

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
        xpath = f"//div[@class='navbar-brand' and contains(text(), 'Продукты')]"
        text = self.wait_for_element(By.XPATH, xpath).text
        return text

    def get_product_shop_quantity_icon(self):
        xpath = "//span[contains(@class, 'cart-counter') and contains(@class, 'badge')]"
        return int(self.wait_for_element(By.XPATH, xpath).text.strip())

    def get_product_shop_quantity(self, name):
        xpath = f"//div[contains(., '{name}')]/ancestor::div[contains(@class, 'card')]//input[contains(@class, 'shadow-form')]"
        box_value = self.wait_for_element(By.XPATH, xpath)
        if box_value is None:
            return 0
        item_value = box_value.get_attribute("value")
        return int(item_value) if item_value and item_value.isdigit() else 0

    def clear_the_shop(self, name):
        while self.get_product_shop_quantity(name) > 0:
            self.remove_product(name)

    def clear_icon_shop(self, name):
        while self.get_product_shop_quantity_icon() > 0:
            self.remove_product(name)



