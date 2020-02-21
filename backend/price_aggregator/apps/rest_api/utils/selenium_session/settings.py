from enum import Enum
from selenium.webdriver.firefox.options import Options as ParentOptions


class SessionSettings(Enum):
    driver_path = 'price_aggregator/apps/rest_api/utils/webdriver/geckodriver'


class BrowserOptions(ParentOptions):
    def __init__(self):
        super().__init__()
        self.headless = True
