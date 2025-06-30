from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class OverviewPage(BasePage):

    OVERVIEW_PAGE_TEXT = '//div[@class="navbar-brand" and contains(text(), "Подтверждение")]'
    BACK_TO_SHOP_BUTTON = '//button[@class="btn btn-dark text-light text-end px-5"]'
    CLOSE_ORDER_BUTTON = '//button[@class="btn btn-success text-light text-end px-5"]'

    def __init__(self, driver):
        super().__init__(driver)

    @property
    def overview_page_text(self):
        return self.wait_for_element(By.XPATH, self.OVERVIEW_PAGE_TEXT)

    def back_to_shop_button_click(self):
        self.click_button(By.XPATH, self.BACK_TO_SHOP_BUTTON)

    def close_order_button_click(self):
        self.click_button(By.XPATH, self.CLOSE_ORDER_BUTTON)

