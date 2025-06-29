def test_admin_product_creation(admin_login, admin_page, header):
    admin_page_url = "http://91.197.96.80/manageProductsPage"

    old_name = "Хот-дог"
    old_item_name = f"{old_name} с курицей"
    old_description = f"{old_item_name} 200 г"
    old_price = "200"
    old_exp_category = old_name
    old_pic_url = "https://volshebnaya-eda.ru/wp-content/uploads/2019/09/datskij-xot-dog-10.jpg"

    new_name = "Манты"
    new_item_name = f"{new_name} с курицей"
    new_description = f"{new_item_name} 300 г"
    new_price = "500"
    new_exp_category = new_name
    new_pic_url = old_pic_url

    header.open_hidden_menu()
    header.open_edit_menu()
    assert admin_page.get_edit_page_url() == admin_page_url, "URL профиля администратора неправильный"

    admin_page.add_product_button_click()
    admin_page.fill_the_blanks(old_item_name, old_description, old_exp_category, old_price, old_pic_url)

    admin_page.create_product_button_click()
    assert admin_page.is_product_displayed(old_name), f"Товар {old_name} не создался"

    admin_page.product_edit_button_click(old_name)
    admin_page.fill_the_blanks(new_item_name, new_description, new_exp_category, new_price, new_pic_url)
    admin_page.confirm_refreshing_button_click()
    assert admin_page.is_product_displayed(new_name), f"Товар {old_name} не обновился на {new_name}"

    admin_page.product_delete_button_click(new_name)
    assert not admin_page.is_product_displayed(new_name), f"Товар {new_name} не удалился"
