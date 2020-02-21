from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


def wait_until_page_downloaded(function):
    def wrapper(self, *args):
        result = function(self, *args)
        wait = WebDriverWait(self, 3)
        try:
            element = wait.until(
                EC.presence_of_element_located((By.ID, "catalogItems")))
            return self.page_source
        except TimeoutException as e:
            print("Exception occured: Time is out.")

    return wrapper
