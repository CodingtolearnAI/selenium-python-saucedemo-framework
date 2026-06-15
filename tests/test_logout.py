from pages.login_page import LoginPage
from pages.logout_page import BurgerMenu


def test_logout(driver):
    login = LoginPage(driver)
    login.open()
    logout = BurgerMenu(driver)

    login.login("standard_user", "secret_sauce")

    logout.logout()
    assert "saucedemo" in driver.current_url
