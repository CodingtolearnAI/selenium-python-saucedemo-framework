from pages.login_page import LoginPage
from pages.cart_page import CartPage
from pages.inventory_page import InventoryPage
from pages.checkout_page import CheckoutPage


def test_checkout(driver):
    login = LoginPage(driver)
    login.open()
    inventory = InventoryPage(driver)
    cart = CartPage(driver)
    checkout = CheckoutPage(driver)

    login.login("standard_user", "secret_sauce")
    inventory.addbackpack()
    inventory.opencart()

    cart.checkout()

    checkout.adddetails()

    checkout.letscontinue()
    assert "two" in driver.current_url

    checkout.finish()
    assert "complete" in driver.current_url

    checkout.backhome()
    assert "inventory" in driver.current_url
