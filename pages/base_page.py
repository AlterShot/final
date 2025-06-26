from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, by, locator, timeout=10):
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((by, locator)))
        except TimeoutException:
            return None

    def wait_for_text_element(self, by, locator, expected_text, timeout=10) -> bool:
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.text_to_be_present_in_element((by, locator), expected_text))
        except TimeoutException:
            return False

    def wait_for_click(self, by, locator, timeout=10):
        try:
            return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((by, locator)))
        except TimeoutException:
            return False

    def wait_for_text_on_page(self, text, timeout=10):
        xpath = f"//*[contains(text(), '{text}')]"
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            return True
        except TimeoutException:
            return False

    def check_url_for_https(self) -> bool:
        page_url = self.driver.current_url
        return page_url.startswith("https://")
