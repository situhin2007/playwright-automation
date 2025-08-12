from playwright.sync_api import Page

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def take_screenshot(self, path: str):
        self.page.screenshot(path=path)