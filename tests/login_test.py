from pages.login_page import LoginPage
from pages.header_container import HeaderContainer
import pytest


@pytest.mark.parametrize('username, password', [
    ('покупатель1', 'покупатель1'),
    ('покупатель2', 'покупатель2'),
    ('покупатель3', 'покупатель3'),
    ('покупатель4', 'покупатель4')
])
def test_user_login(driver, username, password):
    page = LoginPage(driver)
    page.full_login_process(username, password)
    page.check_url_for_https()
    assert page.at_shop_page(), f"{username}: Логин неуспешен, страница не обновилась"
    print(f"{username}: Логин успешен, открыта страница магазина")
    header = HeaderContainer(driver)
    header.open_hidden_menu()
    assert not header.hidden_menu_edit_button(), f"Права администратора появились у {username}, произошел вход администратора"
    print(f"Прав администратора нет, пользователь {username} верный")

def test_admin_login(driver):
    page = LoginPage(driver)
    page.full_login_process('admin', 'admin')
    page.check_url_for_https()
    header = HeaderContainer(driver)
    header.open_hidden_menu()
    assert header.hidden_menu_edit_button(), "Вход админа неуспешен, меню возможностей администратора не появилось"
    print("Вход успешен, меню возможностей администратора есть")


@pytest.mark.parametrize('username, password, reason', [
    ('покупатель', 'покупатель', 'несуществующие логин и пароль'),
    ('покупатель1', '', 'пустое поле пароля'),
    ('', 'покупатель1', 'пустое поле имени пользователя'),
    ('', '', 'пустые поля логина и пароля'),
    ('admin', '', 'имя администратора с пустым паролем'),
    ('', 'admin', 'пароль администратора с пустым именем'),
    ('покупатель1', 'admin', 'пользователь с паролем администратора'),
    ('admin', 'покупатель1', 'администратор с паролем пользователя'),
    ('покупатель1', 'покупатель2', 'пользователь с паролем другого пользователя')
])
def test_wrong_login(driver, username, password, reason):
    page = LoginPage(driver)
    page.full_login_process(username, password)
    assert not page.at_shop_page(), f"Некорректные данные сработали: {reason}"
    print("Некорректные данные не сработали, тест успешен")

def test_user_logout(driver):
    page = LoginPage(driver)
    page.full_login_process('покупатель1', 'покупатель1')
    header = HeaderContainer(driver)
    header.logout()
    assert page.login_field(), "Выход пользователя неуспешен"
    print("Пользователь вышел из аккаунта")
    page.login_button_click()
    assert not page.at_shop_page(), "Предыдущая сессия пользователя сохранилась, тест провален"
    print("Предыдущая сессия пользователя не сохранилась, тест успешен")

def test_admin_logout(driver):
    page = LoginPage(driver)
    page.full_login_process('admin', 'admin')
    header = HeaderContainer(driver)
    header.logout()
    assert page.login_field(), "Выход администратора неуспешен"
    print("Администратор вышел из аккаунта")
    page.login_button_click()
    assert not page.at_shop_page(), "Предыдущая сессия администратора сохранилась, тест провален"
    print("Предыдущая сессия администратора не сохранилась, тест успешен")
