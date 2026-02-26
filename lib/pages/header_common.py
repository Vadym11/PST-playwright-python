from __future__ import annotations # let using the class name as a return type hint within the class itself
from playwright.sync_api import Page
from lib.pages.auth_page import AuthPage

# Assuming your package structure: lib/pages/...
# from lib.pages.shopping_cart.shopping_cart_main_page import ShoppingCartMainPage
# from lib.pages.account.profile_page import ProfilePage
# from lib.pages.account.favorites_page import FavoritesPage
# from lib.pages.account.invoices_page import InvoicesPage
# from lib.pages.home_page import HomePage  # Importing HomePage for navigation


class HeaderCommon:
    def __init__(self, page: Page):
        self._page = page

        # Locators (Using __ for private-like encapsulation)
        self.__main_banner = self._page.get_by_title("Practice Software Testing - Toolshop")
        self.__sign_in_link = self._page.get_by_test_id("nav-sign-in")
        self.__cart_icon = self._page.get_by_test_id("nav-cart")
        self.__home_page_link = self._page.get_by_test_id("nav-home")
        self.__user_nav_menu = self._page.get_by_test_id("nav-menu")
        self.__sign_out_link = self._page.get_by_test_id("nav-sign-out")
        self.__profile_link = self._page.get_by_test_id("nav-my-profile")
        self.__favorites_link = self._page.get_by_test_id("nav-my-favorites")

    def click_main_banner(self) -> None:
        self.__main_banner.click()

    def click_sign_in_link(self) -> AuthPage:
        self.__sign_in_link.click()

        return AuthPage(self._page)

    # def click_favorites_link(self) -> FavoritesPage:
    #     self.__favorites_link.click()
    #     return FavoritesPage(self._page)
    #
    # def click_invoice_link(self) -> InvoicesPage:
    #     self._page.get_by_test_id("nav-my-invoices").click()
    #     return InvoicesPage(self._page)
    #
    # def go_to_invoices_page(self) -> InvoicesPage:
    #     self.click_user_nav_menu()
    #     return self.click_invoice_link()

    def click_user_nav_menu(self) -> HeaderCommon:
        self.__user_nav_menu.click()
        return self

    # def click_profile_link(self) -> ProfilePage:
    #     self.__profile_link.click()
    #     return ProfilePage(self._page)
    #
    # def go_to_profile_page(self) -> ProfilePage:
    #     self.click_user_nav_menu()
    #     return self.click_profile_link()
    #
    # def go_to_favorites_page(self) -> FavoritesPage:
    #     self.click_user_nav_menu()
    #     return self.click_favorites_link()

    def click_sign_out(self) -> None:
        self.__sign_out_link.click()

    def sign_out(self) -> HeaderCommon:
        self.click_user_nav_menu()
        self.click_sign_out()
        return self

    # def click_cart_icon(self) -> ShoppingCartMainPage:
    #     self.__cart_icon.click()
    #     return ShoppingCartMainPage(self._page)

    def click_home_page_link(self) -> None:
        # Import inside the method to avoid circular import issues with HomePage
        from lib.pages.home_page import HomePage

        self._page.wait_for_load_state("networkidle")
        self.__home_page_link.click()
        # return HomePage(self._page)
