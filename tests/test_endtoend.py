
from selenium.webdriver.common.by import By
import time

from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from pages.logout_page import BurgerMenu
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from utils.logger import get_logger

logger = get_logger()


def test_endtoend(driver):
    login = LoginPage(driver)
    login.open()
    inventory = InventoryPage(driver)
    cart = CartPage(driver)
    checkout = CheckoutPage(driver)
    logout = BurgerMenu(driver)

    logger.info("Starting End To End Test")

    login.login("standard_user", "secret_sauce")
    assert "inventory" in driver.current_url
    # time.sleep(1)

    inventory.addbackpack()
    inventory.opencart()
    assert "cart" in driver.current_url
    # time.sleep(1)

    cart.checkout()
    assert "checkout" in driver.current_url
    # time.sleep(1)

    checkout.adddetails()
    # time.sleep(1)
    checkout.letscontinue()
    assert "two" in driver.current_url
    # time.sleep(1)

    checkout.finish()
    assert "complete" in driver.current_url
    # time.sleep(1)

    checkout.backhome()
    assert "inventory" in driver.current_url
    # time.sleep(1)

    logout.logout()
    assert "saucedemo" in driver.current_url

    logger.info("End To End Test Completed")
