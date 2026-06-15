from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.logger import get_logger

logger = get_logger()


class CheckoutPage(BasePage):

    first_name = (By.ID, "first-name")
    last_name = (By.ID, "last-name")
    zip_code = (By.ID, "postal-code")
    tocontinue = (By.ID, "continue")
    tofinish = (By.ID, "finish")
    cancel = (By.ID, "cancel")
    home = (By.ID, "back-to-products")

    def adddetails(self):
        logger.info("Entering first name")
        self.enter_text(self.first_name, "Johny")

        logger.info("Entering last name")
        self.enter_text(self.last_name, "Rose")

        logger.info("Entering zip code")
        self.enter_text(self.zip_code, "560001")

    def letscontinue(self):
        logger.info("Clicking continue")
        self.click(self.tocontinue)

    def finish(self):
        logger.info("Clicking finish")
        self.click(self.tofinish)
        logger.info("Order completed successfully")

    def cancelcheckout(self):
        self.click(self.cancel)

    def backhome(self):

        self.click(self.home)
