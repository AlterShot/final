from pages.admin_page import AdminPage
from pages.header_container import HeaderContainer

def test_admin_product_creation(driver, admin_login):
    admin_page = AdminPage(admin_login)
    header = HeaderContainer(admin_login)
    old_name = "Хот-дог"
    new_name = "Манты"
    admin_page_url = "http://91.197.96.80/manageProductsPage"

    header.open_hidden_menu()
    header.open_edit_menu()
    assert admin_page.get_edit_page_url() == admin_page_url, "URL профиля администратора неправильный"
    print("URL профиля администратора правильный")

    admin_page.add_product_button_click()
    admin_page.add_product_full_info_input(old_name)
    admin_page.create_product_button_click()
    assert admin_page.is_product_displayed(old_name), "Товар не создался"
    print(f"Новый товар {old_name} успешно создан")

    admin_page.product_edit_button_click(old_name)
    admin_page.refreshed_product_info_input(new_name)
    admin_page.confirm_refreshing_button_click()
    assert admin_page.is_product_displayed(new_name), "Товар не обновился"
    print(f"Товар {old_name} обновлен, теперь это {new_name}")

    admin_page.product_delete_button_click(new_name)
    assert not admin_page.is_product_displayed(new_name), "Товар не удалился"
    print(f"Товар {new_name} успешно удален")


