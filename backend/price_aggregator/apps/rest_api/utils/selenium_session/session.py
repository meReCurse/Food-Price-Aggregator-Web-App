from selenium import webdriver

from .url_constructor import UrlConstructor
from .settings import BrowserOptions, SessionSettings
from .deco import wait_until_page_downloaded


class Session(webdriver.Firefox):
    def __init__(self):
        self.browser_options = BrowserOptions()
        self.url_constructor = UrlConstructor()

        super().__init__(
            executable_path=SessionSettings.driver_path.value,
            options=self.browser_options
            )

    @wait_until_page_downloaded
    def get(self, page, text):
        url = self.url_constructor.construct(page, text)
        return super().get(url)
