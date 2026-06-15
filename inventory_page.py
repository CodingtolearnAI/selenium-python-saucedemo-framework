from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from utils.logger import get_logger

logger = get_logger()


class InventoryPage(BasePage):

    backpack = (By.ID, "add-to-cart-sauce-labs-backpack")
    bikelight = (By.ID, "add-to-cart-sauce-labs-bike-light")
    tshirt = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    jacket = (By.ID, "add-to-cart-sauce-labs-fleece-jacket")
    onesie = (By.ID, "add-to-cart-sauce-labs-onesie")
    tshirtred = (By.ID, "add-to-cart-test.allthethings()-t-shirt-(red)")
    open_cart = (By.CLASS_NAME, "shopping_cart_link")

    BACKPACK_NAME = (By.XPATH, "//div[text()='Sauce Labs Backpack']")

    def addbackpack(self):
        logger.info("Adding backpack to cart")
        self.click(self.backpack)

    def addbikelight(self):
        self.click(self.bikelight)

    def addtshirt(self):
        self.click(self.tshirt)

    def addtshirtred(self):
        self.click(self.tshirtred)

    def addjacket(self):
        self.click(self.jacket)

    def addonsie(self):
        self.click(self.onesie)

    def opencart(self):
        self.click(self.open_cart)

    def is_backpack_visible(self):
        return self.driver.find_element(*self.BACKPACK_NAME).is_displayed()
