from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CheckoutCompletePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def get_final_url(self):
        return self.driver.current_url

    def completion_page_text(self):
        xpath = '//div[@class="navbar-brand" and contains(text(), "успешно")]'
        return self.wait_for_element(By.XPATH, xpath)

    def back_to_shop_final_button(self):
        xpath = '//button[@class="btn btn-success text-light text-end px-5 mx-auto mt-5"]'
        return self.wait_for_element(By.XPATH, xpath)

    def back_to_shop_final_button_click(self):
        self.back_to_shop_final_button().click()

    def thanks_text(self):
        xpath = '//div[@class="mx-auto my-2 fs-1 fw-bold text-center"]'
        return self.wait_for_text_element(By.XPATH, xpath, "Спасибо")

