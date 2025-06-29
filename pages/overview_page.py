from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class OverviewPage(BasePage):

    OVERVIEW_PAGE_TEXT = '//div[@class="navbar-brand" and contains(text(), "Подтверждение")]'
    BACK_TO_SHOP_BUTTON = '//button[@class="btn btn-dark text-light text-end px-5"]'
    CLOSE_ORDER_BUTTON = '//button[@class="btn btn-success text-light text-end px-5"]'

    def __init__(self, driver):
        super().__init__(driver)

    def get_overview_url(self):
        return self.driver.current_url

    def overview_page_text(self):
        return self.wait_for_element(By.XPATH, self.OVERVIEW_PAGE_TEXT)

    def back_to_shop_button(self):
        return self.wait_for_element(By.XPATH, self.BACK_TO_SHOP_BUTTON)

    def back_to_shop_button_click(self):
        self.back_to_shop_button().click()

    def close_order_button(self):
        return self.wait_for_element(By.XPATH, self.CLOSE_ORDER_BUTTON)

    def close_order_button_click(self):
        self.close_order_button().click()

