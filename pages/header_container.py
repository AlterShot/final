from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class HeaderContainer(BasePage):
    def hidden_menu_button(self):
        xpath = "//span[@class='material-symbols-outlined text-light-emphasis']"
        return self.wait_for_click(By.XPATH, xpath)

    def open_hidden_menu(self):
        self.hidden_menu_button().click()

    def close_hidden_menu(self):
        self.driver.find_element(By.XPATH, "//button[@id='closeSidebarButton']").click()

    def hidden_menu_edit_button(self):
        xpath = "//a[@class='nav-link' and contains(text(), 'Редактировать товары')]"
        return self.wait_for_click(By.XPATH, xpath)

    def hidden_menu_edit_button_is_visible(self):
        xpath = "//a[@class='nav-link' and contains(text(), 'Редактировать товары')]"
        menu_button = self.wait_for_element(By.XPATH, xpath)
        if menu_button:
            return menu_button.is_displayed()
        else:
            return False

    def header_shop_button(self):
        xpath = "//a[@class='router-link-active router-link-exact-active navbar-brand' and contains(text(), 'Магазин')]"
        return self.wait_for_click(By.XPATH, xpath)

    def header_shop_button_click(self):
        self.header_shop_button().click()

    def open_edit_menu(self):
        button = self.hidden_menu_edit_button()
        if button:
            button.click()
        else:
            raise Exception(f"Кнопка 'Редактировать товары' не найдена")

    def hidden_shop_button(self):
        xpath = "//a[@class='router-link-active router-link-exact-active nav-link' and contains(text(), 'Магазин')]"
        return self.wait_for_click(By.XPATH, xpath)

    def hidden_shop_button_click(self):
        self.hidden_shop_button().click()

    def hidden_cart_button(self):
        xpath = "//a[@class='nav-link' and contains(text(), 'Корзинка')]"
        return self.wait_for_click(By.XPATH, xpath)

    def hidden_cart_button_click(self):
        self.hidden_cart_button().click()

    def headline_cart_button(self):
        xpath = "//button[@class='btn btn-light btn-sm d-flex position-relative']"
        return self.wait_for_click(By.XPATH, xpath)


    def headline_cart_button_click(self):
        self.headline_cart_button().click()

    def exit_button(self):
        xpath = "//div[@class='btn btn-danger text-light d-flex justify-content-center' and contains(text(), 'Выход')]"
        return self.wait_for_click(By.XPATH, xpath)


    def click_exit_button(self):
        self.exit_button().click()

    def logout(self):
        self.open_hidden_menu()
        self.click_exit_button()

    def get_to_edit_menu(self):
        self.open_hidden_menu()
        self.open_edit_menu()
