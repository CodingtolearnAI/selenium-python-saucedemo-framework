from pages.login_page import LoginPage
from pages.cart_page import CartPage
from pages.inventory_page import InventoryPage


def test_cart(driver):
    login = LoginPage(driver)
    login.open()
    inventory = InventoryPage(driver)
    cart = CartPage(driver)

    login.login("standard_user", "secret_sauce")
    assert inventory.is_backpack_visible()
    inventory.addbackpack()
    inventory.opencart()
    assert "cart" in driver.current_url
    assert "Sauce Labs Backpack" in cart.get_cart_item_name()
    cart.checkout()
    assert "checkout" in driver.current_url
