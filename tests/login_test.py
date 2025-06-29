import pytest


valid_users = [
    ('покупатель1', 'покупатель1'),
    ('покупатель2', 'покупатель2'),
    ('покупатель3', 'покупатель3'),
    ('покупатель4', 'покупатель4')
]

invalid_users = [
    ('покупатель', 'покупатель', 'несуществующие логин и пароль'),
    ('покупатель1', '', 'пустое поле пароля'),
    ('', 'покупатель1', 'пустое поле имени пользователя'),
    ('', '', 'пустые поля логина и пароля'),
    ('admin', '', 'имя администратора с пустым паролем'),
    ('', 'admin', 'пароль администратора с пустым именем'),
    ('покупатель1', 'admin', 'пользователь с паролем администратора'),
    ('admin', 'покупатель1', 'администратор с паролем пользователя'),
    ('покупатель1', 'покупатель2', 'пользователь с паролем другого пользователя')
]

def test_for_security(login_page):
    assert login_page.check_url_for_https(), "Сайт работает через незащищенный протокол"

@pytest.mark.parametrize('username, password', valid_users)
def test_user_login(username, password, login_page, header):
    login_page.full_login_process(username, password)
    assert login_page.at_shop_page(), f"{username}: Логин неуспешен, страница не обновилась"
    header.open_hidden_menu()
    assert not header.hidden_menu_edit_button_is_visible(), f"Права администратора появились у {username}, произошел вход администратора"

@pytest.mark.parametrize('username, password, reason', invalid_users)
def test_wrong_login(username, password, reason, login_page):
    login_page.full_login_process(username, password)
    assert not login_page.at_shop_page(), f"Некорректные данные сработали: {reason}"

def test_user_logout(login_page, header):
    login_page.full_login_process('покупатель1', 'покупатель1')
    header.logout()
    assert login_page.login_field(), "Выход пользователя неуспешен"
    login_page.login_button_click()
    assert not login_page.at_shop_page(), "Предыдущая сессия пользователя сохранилась, тест провален"

def test_admin_login(login_page, header):
    login_page.full_login_process('admin', 'admin')
    header.open_hidden_menu()
    assert header.hidden_menu_edit_button_is_visible(), "Вход админа неуспешен, меню возможностей администратора не появилось"

def test_admin_logout(login_page, header):
    login_page.full_login_process('admin', 'admin')
    header.logout()
    assert login_page.login_field(), "Выход администратора неуспешен"
    login_page.login_button_click()
    assert not login_page.at_shop_page(), "Предыдущая сессия администратора сохранилась, тест провален"