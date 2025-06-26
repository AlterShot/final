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

    def check_url_for_https(self):
        page_url = self.driver.current_url
        assert page_url.startswith("https://"), "Сайт работает через незащищенный протокол"
        print("Сайт работает через защищенный протокол")
