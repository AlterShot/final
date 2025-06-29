from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class HeaderContainer(BasePage):

    HIDDEN_MENU_BUTTON = "//span[@class='material-symbols-outlined text-light-emphasis']"
    HIDDEN_MENU_EDIT_BUTTON = "//a[@class='nav-link' and contains(text(), 'Редактировать товары')]"
    HIDDEN_SHOP_BUTTON = "//a[@class='router-link-active router-link-exact-active nav-link' and contains(text(), 'Магазин')]"
    HIDDEN_CART_BUTTON = "//a[@class='nav-link' and contains(text(), 'Корзинка')]"
    CLOSE_HIDDEN_MENU_BUTTON = "//button[@id='closeSidebarButton']"
    HEADER_SHOP_BUTTON = "//a[@class='router-link-active router-link-exact-active navbar-brand' and contains(text(), 'Магазин')]"
    HEADER_CART_BUTTON = "//button[@class='btn btn-light btn-sm d-flex position-relative']"
    EXIT_BUTTON = "//div[@class='btn btn-danger text-light d-flex justify-content-center' and contains(text(), 'Выход')]"

    def __init__(self, driver):
        super().__init__(driver)

    def hidden_menu_button(self):
        return self.wait_for_click(By.XPATH, self.HIDDEN_MENU_BUTTON)

    def open_hidden_menu(self):
        self.hidden_menu_button().click()

    def close_hidden_menu(self):
        self.driver.find_element(By.XPATH, self.CLOSE_HIDDEN_MENU_BUTTON).click()

    def hidden_menu_edit_button(self):
        return self.wait_for_click(By.XPATH, self.HIDDEN_MENU_EDIT_BUTTON)

    def open_edit_menu(self):
        self.hidden_menu_edit_button().click()

    def hidden_shop_button(self):
        return self.wait_for_click(By.XPATH, self.HIDDEN_SHOP_BUTTON)

    def hidden_shop_button_click(self):
        self.hidden_shop_button().click()

    def hidden_cart_button(self):
        return self.wait_for_click(By.XPATH, self.HIDDEN_CART_BUTTON)

    def hidden_cart_button_click(self):
        self.hidden_cart_button().click()

    def header_shop_button(self):
        return self.wait_for_click(By.XPATH, self.HEADER_SHOP_BUTTON)

    def header_shop_button_click(self):
        self.header_shop_button().click()

    def header_cart_button(self):
        return self.wait_for_click(By.XPATH, self.HEADER_CART_BUTTON)

    def header_cart_button_click(self):
        self.header_cart_button().click()

    def exit_button(self):
        return self.wait_for_click(By.XPATH, self.EXIT_BUTTON)

    def click_exit_button(self):
        self.exit_button().click()

    def logout(self):
        self.open_hidden_menu()
        self.click_exit_button()

    def get_to_edit_menu(self):
        self.open_hidden_menu()
        self.open_edit_menu()

    def hidden_menu_edit_button_is_visible(self):
        menu_button = self.wait_for_element(By.XPATH, self.HIDDEN_MENU_EDIT_BUTTON)
        if menu_button:
            return menu_button.is_displayed()
        else:
            return False