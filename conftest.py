import shutil
import tempfile
import pytest
import logging
import os

from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import LoginPage
from pages.header_container import HeaderContainer
from pages.cart_page import CartPage
from pages.shop_page import ShopPage


logger = logging.getLogger("logger_shop_test")
logger.setLevel(logging.INFO)
if not os.path.exists('logs'):
    os.makedirs('logs')

logger_file = f'logs/test_log_{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.log'

file_handler = logging.FileHandler(logger_file, encoding="utf-8")
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    result = outcome.get_result()
    if result.when == 'call':
        test_name = item.name
        test_name = test_name.encode().decode("unicode_escape")

        if result.failed:
            message = ""
            if call.excinfo:
                message = str(call.excinfo.value).split('\n')[0]
            driver = item.funcargs.get('driver', None)
            if driver:
                screenshots_dir = 'screenshots'
                os.makedirs(screenshots_dir, exist_ok=True)
                screenshots_path = os.path.join(screenshots_dir, f"{test_name}.png")
                driver.save_screenshot(screenshots_path)
                logger.error(f"Провал: {test_name},ошибка: {message}, скрин сохранен: {screenshots_path}")
            else:
                logger.error(f"Провал: {test_name},ошибка: {message}, но скрин не получился")
        elif result.passed:
            logger.info(f"Успех: {test_name}")

@pytest.fixture(params=['chrome', 'firefox', 'edge'])
def driver(request):
    browser = request.param
    logger.info(f"Запускается {browser}")
    new_profile = None
    if browser == 'chrome':
        options = webdriver.ChromeOptions()
        new_profile = tempfile.mkdtemp()
        options.add_argument(f"--user-data-dir={new_profile}")
        options.add_argument("--ignore-certificate-errors")
        options.add_argument("--allow-insecure-localhost")
        options.add_argument("--ignore-ssl-errors")
        options.add_argument("--disable-web-security")
        options.add_argument("--allow-running-insecure-content")
        driver = webdriver.Chrome(options=options,
                                  service=ChromeService(ChromeDriverManager().install()))
    elif browser == 'firefox':
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    elif browser == 'edge':
        options = webdriver.EdgeOptions()
        options.add_experimental_option("detach", True)
        driver = webdriver.Edge(options=options,
                                service=EdgeService(EdgeChromiumDriverManager().install()))
    else:
        raise ValueError("нет такого браузера")

    driver.get("http://91.197.96.80/")
    driver.set_window_size(1920, 1080)
    yield driver
    driver.quit()
    shutil.rmtree(new_profile, ignore_errors=True)

@pytest.fixture
def user_login(driver):
    page = LoginPage(driver)
    page.full_login_process('покупатель1', 'покупатель1')
    yield driver
    header = HeaderContainer(driver)
    header.logout()

@pytest.fixture
def admin_login(driver):
    page = LoginPage(driver)
    page.full_login_process('admin', 'admin')
    yield driver
    header = HeaderContainer(driver)
    header.logout()

@pytest.fixture
def simple_order(driver):
    page = LoginPage(driver)
    shop = ShopPage(driver)
    cart = CartPage(driver)
    header = HeaderContainer(driver)
    page.full_login_process('покупатель1', 'покупатель1')
    shop.add_product("Бургер")
    header.headline_cart_button_click()
    cart.continue_cart_button_click()
    yield driver
    header.logout()

