from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CartPage(BasePage):

    checkoutbutton = (By.ID, "checkout")
    shopping = (By.ID, "continue-shopping")

    CART_ITEM = (By.CLASS_NAME, "inventory_item_name")

    def checkout(self):
        self.click(self.checkoutbutton)

    def continueshopping(self):
        self.click(self.shopping)

    def get_cart_item_name(self):
        return self.get_text(self.CART_ITEM)
