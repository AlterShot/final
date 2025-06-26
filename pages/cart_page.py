from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def get_cart_url(self):
        return self.driver.current_url

    def cart_page_text(self):
        xpath = '//div[@class="navbar-brand" and contains(text(), "Корзинка")]'
        return self.wait_for_element(By.XPATH, xpath)

    def empty_cart_text(self):
        xpath = '//div[@class="mx-auto my-2 fs-5 text-center" and contains(text(), "в корзине")]'
        return self.wait_for_element(By.XPATH, xpath).text

    def continue_cart_button(self):
        xpath = '//button[@class="btn btn-success text-light text-end px-5" and contains(text(), "Оформить")]'
        return self.wait_for_element(By.XPATH, xpath)

    def continue_cart_button_click(self):
        self.continue_cart_button().click()

    def overall_cart_price(self):
        xpath = '//div[@class="mx-2 my-4 fs-5 text-end" and contains(text(), "Итого:")]'
        return self.wait_for_element(By.XPATH, xpath)

    def get_exact_cart_price(self):
        price_text = self.overall_cart_price().text
        exact_price = int(price_text.replace("Итого: ", "").replace("₽", "").strip())
        return exact_price

    def item_cart_quantity(self):
        xpath = "//input[@class='form-control shadow-none w-25 align-self-center text-center bg-light-subtle mx-2']"
        cart_item_quantity = self.wait_for_element(By.XPATH, xpath)
        return cart_item_quantity.get_attribute("value")

    def add_product_cart_button(self):
        xpath = "//span[@class='material-symbols-outlined m-auto' and contains(text(), 'add')]"
        return self.wait_for_element(By.XPATH, xpath)

    def remove_product_cart_button(self):
        xpath = "//span[@class='material-symbols-outlined m-auto' and contains(text(), 'remove')]"
        return self.wait_for_element(By.XPATH, xpath)

    def add_product_cart_button_click(self):
        self.add_product_cart_button().click()

    def remove_product_cart_button_click(self):
        self.remove_product_cart_button().click()


