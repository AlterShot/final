import pytest

from pages.shop_page import ShopPage
from pages.cart_page import CartPage
from pages.header_container import HeaderContainer

def test_shop_page(driver, user_login):
    shop_page = ShopPage(user_login)
    assert "Продукты" in shop_page.text_above_shop(), "Страница каталога не открыта"
    print("Страница каталога верна")

def test_cart_url(driver, user_login):
    header = HeaderContainer(user_login)
    cart_page = CartPage(user_login)
    header.headline_cart_button_click()
    assert cart_page.get_cart_url() == "http://91.197.96.80/cart", "Ошибка с url корзины"
    print("URL корзины верный")

def test_empty_cart(driver, user_login):
    shop_page = ShopPage(user_login)
    header = HeaderContainer(user_login)
    cart_page = CartPage(user_login)
    product = "Бургер"
    shop_page.clear_icon_shop(product)
    header.headline_cart_button_click()
    assert cart_page.is_cart_empty(), "Корзина не пуста, ошибка"
    print("Корзина пуста, сообщение показано")

@pytest.mark.parametrize("quantity", [1, 10, 50, 99, 100, 101, 120])
def test_maximum_product_quantity(driver, user_login, quantity):
    shop_page = ShopPage(user_login)
    header = HeaderContainer(user_login)
    cart_page = CartPage(user_login)
    maximum_product_quantity = 100
    product = "Бургер"
    shop_page.clear_icon_shop(product)
    for i in range(quantity):
        shop_page.add_product(product)
    header.headline_cart_button_click()
    assert cart_page.item_cart_quantity() == quantity, (
        f"Количество в корзине не совпадает: {cart_page.item_cart_quantity()},"
        f"Должно быть: {quantity}")
    print("Количество товаров в заказе и корзине совпадает")
    assert cart_page.item_cart_quantity() <= maximum_product_quantity, "Прошел заказ больше, чем на 100 единиц товара"
    print("Максимальное количество товара в 100 единиц сохранено")

@pytest.mark.parametrize("quantity", [10, 100, 510])
def test_maximum_price(driver, user_login, quantity):
    maximum_overall_price = 100000
    shop_page = ShopPage(user_login)
    header = HeaderContainer(user_login)
    cart_page = CartPage(user_login)
    product = "Бургер"
    shop_page.clear_the_shop(product)
    for i in range(quantity):
        shop_page.add_product(product)
    header.headline_cart_button_click()
    assert cart_page.get_exact_cart_price() == shop_page.get_price_value(
        product) * quantity, "Общая цена не совпадает"
    print("Общая цена в корзине верна")
    assert cart_page.get_exact_cart_price() <= maximum_overall_price, "общая цена вышла за допустимые пределы"
    print("Общая цена в пределах нормы")

def test_order_and_delete(driver, user_login):
    shop_page = ShopPage(user_login)
    header = HeaderContainer(user_login)
    cart_page = CartPage(user_login)
    product = "Бургер"
    shop_page.clear_icon_shop(product)
    shop_page.add_product(product)
    header.headline_cart_button_click()
    assert cart_page.wait_for_quantity(1), "Товар не добавлен в корзину"
    print("Товар добавлен в корзину")
    cart_page.add_product_cart_button_click()
    assert cart_page.wait_for_quantity(2), "Кнопка добавления в корзине не работает"
    print("Количество увеличено")
    cart_page.remove_product_cart_button_click()
    assert cart_page.wait_for_quantity(1), "Кнопка удаления товара в корзине не работает"
    print("Кнопка удаления товара в корзине работает")



