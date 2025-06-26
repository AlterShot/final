from pages.data_input_page import DataInputPage
from pages.overview_page import OverviewPage
from pages.checkout_complete_page import CheckoutCompletePage
from pages.shop_page import ShopPage


def test_full_checkout(driver, simple_order):
    overview_page = OverviewPage(simple_order)
    checkout_complete_page = CheckoutCompletePage(simple_order)
    shop_page = ShopPage(simple_order)

    data_input_page = DataInputPage(simple_order)
    assert "Оформление" in data_input_page.input_page_text_check().text, "Ошибка, страница неправильная"
    print("Переход на страницу оформления заказа успешен")

    data_input_page.fill_the_blanks()
    data_input_page.proceed_purchase_button_click()
    assert "Подтверждение" in overview_page.overview_page_text().text, "Ошибка, это не страница подтверждения заказа"
    print("Страница подтверждения заказа верна")

    overview_page.close_order_button_click()
    assert "Спасибо" in checkout_complete_page.thanks_text(), "Заказ не подтвержден"
    print("Заказ подтвержден")

    checkout_complete_page.back_to_shop_final_button_click()
    assert "Продукты" in shop_page.text_above_shop().text, "Возврат на страницу каталога не сработал"
    print("Вы вернулись на страницу каталога после подтверждения заказа")
