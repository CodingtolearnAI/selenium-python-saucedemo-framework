import os
from datetime import datetime


def take_screenshot(driver):

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    file_name = f"screenshots/{timestamp}.png"

    os.makedirs("screenshots", exist_ok=True)

    driver.save_screenshot(file_name)

    return file_name
