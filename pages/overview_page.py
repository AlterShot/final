from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class OverviewPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def get_overview_url(self):
        return self.driver.current_url

    def overview_page_text(self):
        xpath = '//div[@class="navbar-brand" and contains(text(), "Подтверждение")]'
        return self.wait_for_element(By.XPATH, xpath)

    def back_to_shop_button(self):
        xpath = '//button[@class="btn btn-dark text-light text-end px-5"]'
        return self.wait_for_element(By.XPATH, xpath)

    def close_order_button(self):
        xpath = '//button[@class="btn btn-success text-light text-end px-5"]'
        return self.wait_for_element(By.XPATH, xpath)

    def back_to_shop_button_click(self):
        self.back_to_shop_button().click()

    def close_order_button_click(self):
        self.close_order_button().click()

