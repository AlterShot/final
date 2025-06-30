from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CheckoutCompletePage(BasePage):

    COMPLETION_PAGE_TEXT = '//div[@class="navbar-brand" and contains(text(), "успешно")]'
    THANKS_TEXT = '//div[@class="mx-auto my-2 fs-1 fw-bold text-center"]'
    BACK_TO_SHOP_FINAL_BUTTON = '//button[@class="btn btn-success text-light text-end px-5 mx-auto mt-5"]'

    def __init__(self, driver):
        super().__init__(driver)

    @property
    def completion_page_text(self):
        return self.wait_for_element(By.XPATH, self.COMPLETION_PAGE_TEXT).text

    def is_thanks_text_displayed(self):
        return self.wait_for_text_element(By.XPATH, self.THANKS_TEXT, "Спасибо")

    def back_to_shop_final_button_click(self):
        self.click_button(By.XPATH, self.BACK_TO_SHOP_FINAL_BUTTON)


