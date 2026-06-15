from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.logger import get_logger

logger = get_logger()


class LoginPage(BasePage):

    def open(self):
        self.driver.get("https://www.saucedemo.com/")

    username_input = (By.ID, "user-name")
    password_input = (By.ID, "password")
    login_button = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")

    def login(self, username, password):
        logger.info("Entering username")

        self.enter_text(self.username_input, username)

        logger.info("Entering password")

        self.enter_text(self.password_input, password)

        logger.info("Clicking login button")

        self.click(self.login_button)

        logger.info("Login completed")

    def get_error_message(self):
        return self.get_text(self.ERROR_MESSAGE)
