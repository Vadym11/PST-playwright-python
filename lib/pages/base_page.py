from abc import ABC
from playwright.sync_api import Page

class BasePage(ABC):
    def __init__(self, page: Page):
        self._page = page

    def get_page(self) -> Page:
        return self._page
