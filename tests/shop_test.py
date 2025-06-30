import pytest

PRODUCT_NAME = 'Бургер'
MAXIMUM_PRODUCT_QUANTITY = 100
MAXIMUM_OVERALL_PRICE = 100000

def test_shop_page(user_shop_page):
    assert "Продукты" in user_shop_page.text_above_shop, "Страница каталога не открыта"

def test_cart_url(user_header, user_cart_page):
    user_header.header_cart_button_click()
    assert user_cart_page.get_page_url() == "http://91.197.96.80/cart", "Ошибка с url корзины"

def test_empty_cart(user_shop_page, user_cart_page, user_header):
    user_shop_page.clear_icon_shop(PRODUCT_NAME)
    user_header.header_cart_button_click()
    assert user_cart_page.is_cart_empty(), "Корзина не пуста, ошибка"

@pytest.mark.parametrize("quantity", [1, 10, 50, 99, 100, 101, 120])
def test_maximum_product_quantity(quantity, user_shop_page, user_cart_page, user_header):
    user_shop_page.clear_and_buy(PRODUCT_NAME, quantity)
    user_header.header_cart_button_click()
    assert user_cart_page.item_cart_quantity() == quantity, (
        f"Количество в корзине не совпадает: {user_cart_page.item_cart_quantity()},"
        f"Должно быть: {quantity}")
    assert user_cart_page.item_cart_quantity() <= MAXIMUM_PRODUCT_QUANTITY, f"Прошел заказ больше, чем на {MAXIMUM_PRODUCT_QUANTITY} единиц товара"

@pytest.mark.parametrize("quantity", [10, 100, 510])
def test_maximum_price(quantity, user_shop_page, user_cart_page, user_header):
    user_shop_page.clear_and_buy(PRODUCT_NAME, quantity)
    user_header.header_cart_button_click()
    assert user_cart_page.get_exact_cart_price() == user_shop_page.get_price_value(
        PRODUCT_NAME) * quantity, "Общая цена не совпадает"
    assert user_cart_page.get_exact_cart_price() <= MAXIMUM_OVERALL_PRICE, f"Общая цена вышла за допустимые пределы в {MAXIMUM_OVERALL_PRICE}"

def test_order_and_delete(user_shop_page, user_cart_page, user_header):
    user_shop_page.clear_icon_shop(PRODUCT_NAME)
    user_shop_page.add_product(PRODUCT_NAME)
    user_header.header_cart_button_click()
    assert user_cart_page.wait_for_quantity(1), "Товар не добавлен в корзину"
    user_cart_page.add_product_cart_button_click()
    assert user_cart_page.wait_for_quantity(2), "Кнопка добавления в корзине не работает"
    user_cart_page.remove_product_cart_button_click()
    assert user_cart_page.wait_for_quantity(1), "Кнопка удаления товара в корзине не работает"
