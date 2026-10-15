
from playwright.sync_api import Page, expect

def test_login(page: Page):
    page.goto("https://www.saucedemo.com/")

    page.get_by_role("textbox", name="Username").fill("standard_user")
    page.get_by_label("Password").fill("secret_sauce")
    page.locator("#login-button").click()

    expect(page.get_by_text("Products", exact=True)).to_be_visible()


def test_invalid_login(page: Page):
    page.goto("https://www.saucedemo.com/")

    page.get_by_role("textbox", name="Username").fill("standard_user")
    page.get_by_label("Password").fill("wrong_password")
    page.locator("#login-button").click()

    expect(
        page.get_by_text("Username and password do not match")
    ).to_be_visible()


def test_locked_out_user(page: Page):
    page.goto("https://www.saucedemo.com/")

    page.get_by_role("textbox", name="Username").fill("locked_out_user")
    page.get_by_label("Password").fill("secret_sauce")
    page.locator("#login-button").click()

    expect(page.get_by_text("locked out")).to_be_visible()
