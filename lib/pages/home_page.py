from playwright.sync_api import Page
from faker import Faker
from lib.pages.base_page import BasePage
# Note: These imports assume your package structure is set up
from lib.pages.header_common import HeaderCommon
from lib.pages.product_page import ProductPage

fake = Faker()


class HomePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.header = HeaderCommon(page)

    def go_to(self, url) -> "HomePage":
        # Use _page to match your BasePage
        self._page.goto(url, wait_until="networkidle", timeout=60000)
        return self

    def filter_eco_products(self) -> "HomePage":
        self._page.get_by_test_id("eco-friendly-filter").click()
        return self

    def click_first_product(self) -> ProductPage:
        # In Python, .first is a property, not a method ()
        self._page.get_by_test_id("product-name").first.click()
        return ProductPage(self._page)

    def click_random_page(self) -> "HomePage":
        random_page = str(fake.random_int(min=1, max=5))
        if random_page == "1":
            self._page.reload()
            return self

        self._page.get_by_role("button", name=random_page).click()
        return self

    def click_random_product(self) -> ProductPage:
        self._page.wait_for_load_state("networkidle")

        all_cards = self._page.locator(".card")
        available_products = all_cards.filter(
            has_not=self._page.get_by_test_id("out-of-stock")
        ).filter(
            has_not_text="Thor Hammer"
        )

        product_list = available_products.all()
        if not product_list:
            raise Exception("No available products found matching criteria.")

        random_product = fake.random_element(product_list)
        random_product.click()

        return ProductPage(self._page)
