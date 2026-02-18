from playwright.sync_api import Page, Locator, expect
from lib.pages.base_page import BasePage
from lib.pages.header_common import HeaderCommon
# Placeholders for your API/Model logic
# from lib.api_models.product import ProductAPI
# from lib.api_models.api_product import GetProductResponse

class ProductPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        # Using __ for private-like locators
        self.__add_to_cart_button = page.get_by_test_id("add-to-cart")
        self.__add_to_favorites_button = page.get_by_test_id("add-to-favorites")
        self.header = HeaderCommon(page)

    def click_add_to_cart(self, count: int = 1) -> "ProductPage":
        # Python uses click_count instead of clickCount
        self.__add_to_cart_button.click(click_count=count, delay=300)
        return self

    def get_added_to_cart_pop_up(self) -> Locator:
        # .last is a property in Python, not a method
        return self._page.get_by_role("alert", name="Product added to shopping cart.").last

    def click_add_to_cart_and_assert_pop_ups(self, count: int = 1) -> None:
        for _ in range(count):
            self.click_add_to_cart()
            # Assertions use snake_case
            expect(self.get_added_to_cart_pop_up()).to_be_visible()

    def get_cart_quantity(self) -> Locator:
        return self._page.get_by_test_id("cart-quantity")

    def click_add_to_favorites(self) -> "ProductPage":
        self.__add_to_favorites_button.click()
        return self

    def get_current_product_id(self) -> str:
        url = self._page.url
        # Splitting the URL to get the last segment
        product_id = url.split("/")[-1] if "/" in url else ""
        return product_id

    def get_current_product_info_by_id(self, product_api: "ProductAPI") -> "GetProductResponse":
        product_id = self.get_current_product_id()
        product_info = product_api.get_by_id(product_id)
        return product_info

    def get_added_to_favorites_pop_up(self) -> Locator:
        return self._page.get_by_role("alert", name="Product added to your favorites list.")
