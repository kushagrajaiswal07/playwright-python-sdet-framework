from playwright.sync_api import Page, expect
from pages.login_page import LoginPage


def test_login(page: Page):
    login_page = LoginPage(page)

    login_page.open()
    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()

    expect(page.get_by_text("Products", exact=True)).to_be_visible()


def test_invalid_login(page: Page):
    login_page = LoginPage(page)

    login_page.open()
    login_page.enter_username("standard_user")
    login_page.enter_password("wrong_password")
    login_page.click_login()

    expect(
        page.get_by_text("Username and password do not match")
    ).to_be_visible()


def test_locked_out_user(page: Page):
    login_page = LoginPage(page)

    login_page.open()
    login_page.enter_username("locked_out_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()

    expect(page.get_by_text("locked out")).to_be_visible()