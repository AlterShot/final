from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage


class CartPage(BasePage):

    EMPTY_CART_TEXT = "//div[contains(@class, 'mx-auto') and contains(@class, 'fs-5') and contains(text(), 'в корзине')]"
    CART_PAGE_TEXT = '//div[@class="navbar-brand" and contains(text(), "Корзинка")]'
    CONTINUE_CART_BUTTON = '//button[@class="btn btn-success text-light text-end px-5" and contains(text(), "Оформить")]'
    REMOVE_PRODUCT_CART_BUTTON = "//button[contains(@class, 'btn') and .//span[contains(text(),'remove')]]"
    ADD_PRODUCT_CART_BUTTON = "//button[contains(@class, 'btn') and .//span[contains(text(),'add')]]"
    OVERALL_CART_PRICE = '//div[@class="mx-2 my-4 fs-5 text-end" and contains(text(), "Итого:")]'
    ITEM_CART_QUANTITY = "//input[@class='form-control shadow-none w-25 align-self-center text-center bg-light-subtle mx-2']"
    WAIT_FOR_QUANTITY = "//span[contains(@class, 'cart-counter') and contains(@class, 'badge')]"

    def __init__(self, driver):
        super().__init__(driver)

    def get_cart_url(self):
        return self.driver.current_url

    def cart_page_text(self):
        return self.wait_for_element(By.XPATH, self.CART_PAGE_TEXT).text

    def empty_cart_text(self):
        element = self.wait_for_element(By.XPATH, self.EMPTY_CART_TEXT)
        text = element.text.lower()
        if "пока пусто" in text:
            return text
        return None

    def continue_cart_button(self):
        return self.wait_for_click(By.XPATH, self.CONTINUE_CART_BUTTON)

    def continue_cart_button_click(self):
        self.continue_cart_button().click()

    def add_product_cart_button(self):
        return self.wait_for_click(By.XPATH, self.ADD_PRODUCT_CART_BUTTON)

    def add_product_cart_button_click(self):
        self.add_product_cart_button().click()

    def remove_product_cart_button(self):
        return self.wait_for_click(By.XPATH, self.REMOVE_PRODUCT_CART_BUTTON)

    def remove_product_cart_button_click(self):
        self.remove_product_cart_button().click()

    def overall_cart_price(self):
        return self.wait_for_element(By.XPATH, self.OVERALL_CART_PRICE)

    def get_exact_cart_price(self):
        price_text = self.overall_cart_price().text
        exact_price = float(price_text.replace("Итого: ", "").replace("₽", "").strip())
        return exact_price

    def item_cart_quantity(self):
        cart_item_quantity = self.wait_for_element(By.XPATH, self.ITEM_CART_QUANTITY)
        return int(cart_item_quantity.get_attribute("value"))

    def wait_for_quantity(self, expected_quantity, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(
                lambda d: int(d.find_element(By.XPATH, self.WAIT_FOR_QUANTITY).text.strip()) == expected_quantity
            )
            return True
        except TimeoutException:
            return False

    def is_cart_empty(self):
        try:
            return self.empty_cart_text() is not None
        except NoSuchElementException:
            return False
