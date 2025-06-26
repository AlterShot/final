import pytest

from pages.shop_page import ShopPage
from pages.cart_page import CartPage
from pages.header_container import HeaderContainer


@pytest.mark.parametrize("quantity", [0, 1, 10, 50, 99, 100, 101, 200, 500, 1000, 2000])
def test_order_and_check(driver, user_login, quantity):
    shop_page = ShopPage(user_login)
    header = HeaderContainer(user_login)
    cart_page = CartPage(user_login)
    maximum_product_quantity = 100
    maximum_overall_price = 100000
    assert "Продукты" in shop_page.text_above_shop(), "Страница каталога не открыта"
    print("Страница каталога верна")
    product = "Бургер"
    if quantity == 0:
        header.headline_cart_button_click()
        assert cart_page.empty_cart_text() is not None, "Корзина не пуста, ошибка"
        print("Корзина пуста, сообщение показано")
    else:
        for i in range(quantity):
            shop_page.add_product(product)
        header.headline_cart_button_click()
        assert int(cart_page.item_cart_quantity()) == quantity, (
            f"Количество в корзине не совпадает: {cart_page.item_cart_quantity()},"
            f"Должно быть: {quantity}")
        print("Количество товаров в заказе и корзине совпадает")
        assert int(cart_page.item_cart_quantity()) <= maximum_product_quantity, "Прошел заказ больше, чем на 100 единиц товара"
        print("Максимальное количество товара в 100 единиц сохранено")
        assert int(cart_page.get_exact_cart_price()) == shop_page.get_price_value(product) * quantity, "Общая цена не совпадает"
        print("Общая цена в корзине верна")
        assert int(cart_page.get_exact_cart_price()) <= maximum_overall_price, "общая цена вышла за допустимые пределы"
        print("Общая цена в пределах нормы")
    cart_page.continue_cart_button_click()

def test_order_and_delete(driver, user_login):
    shop_page = ShopPage(user_login)
    header = HeaderContainer(user_login)
    cart_page = CartPage(user_login)
    assert "Продукты" in shop_page.text_above_shop(), "Страница каталога не открыта"
    print("Страница каталога верна")
    product = "Бургер"
    shop_page.add_product(product)
    header.headline_cart_button_click()
    assert cart_page.get_cart_url() == "http://91.197.96.80/cart", "Ошибка с url"
    print("URL корзины верный")
    assert cart_page.item_cart_quantity() == 1, "Товар не добавлен в корзину"
    print("Товар добавлен в корзину")
    cart_page.add_product_cart_button_click()
    assert cart_page.item_cart_quantity() == 2, "Кнопка добавления в корзине не работает"
    print("Количество увеличено")
    for i in range(2):
        cart_page.remove_product_cart_button_click()
    assert cart_page.empty_cart_text() is not None, "Товар не удалился"
    print("Корзина пуста, кнопка удаления товара сработала")



