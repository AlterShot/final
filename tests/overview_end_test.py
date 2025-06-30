from pages.data_input_page import DataInputPage
from pages.overview_page import OverviewPage
from pages.checkout_complete_page import CheckoutCompletePage
from pages.shop_page import ShopPage


def test_full_checkout(simple_order):
    overview_page = OverviewPage(simple_order)
    checkout_complete_page = CheckoutCompletePage(simple_order)
    shop_page = ShopPage(simple_order)
    data_input_page = DataInputPage(simple_order)

    assert "Оформление" in data_input_page.input_page_text_check.text, "Ошибка, страница неправильная"

    data_input_page.fill_the_blanks_name()
    data_input_page.proceed_purchase_button_click()
    assert "Подтверждение" in overview_page.overview_page_text.text, "Ошибка, это не страница подтверждения заказа"

    overview_page.close_order_button_click()
    assert checkout_complete_page.is_thanks_text_displayed(), "Заказ не подтвержден"

    checkout_complete_page.back_to_shop_final_button_click()
    assert "Продукты" in shop_page.text_above_shop, "Возврат на страницу каталога не сработал"
