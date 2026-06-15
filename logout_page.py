from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from utils.logger import get_logger

logger = get_logger()


class BurgerMenu(BasePage):

    burger_button = (By.ID, "react-burger-menu-btn")
    logout_button = (By.ID, "logout_sidebar_link")

    def logout(self):
        logger.info("Opening menu")

        self.click(self.burger_button)
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.ID, "logout_sidebar_link"))
        )

        self.click(self.logout_button)

        logger.info("Logout successful")
