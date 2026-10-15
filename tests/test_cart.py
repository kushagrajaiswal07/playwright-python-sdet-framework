
from playwright.sync_api import expect

def test_add_product_to_cart(login):
    login.get_by_role("button", name="Add to cart").first.click()

    expect(login.locator(".shopping_cart_badge")).to_have_text("1")

    login.locator(".shopping_cart_link").click()

    expect(login.locator(".cart_item")).to_have_count(1)
    expect(login.get_by_text("Sauce Labs Backpack")).to_be_visible()


def test_remove_product_from_cart(login):
    login.get_by_role("button", name="Add to cart").first.click()

    login.get_by_role("button", name="Remove").click()

    expect(login.locator(".shopping_cart_badge")).to_have_count(0)

    login.locator(".shopping_cart_link").click()

    expect(login.locator(".cart_item")).to_have_count(0)


def test_initial_cart_is_empty(login):
    login.locator(".shopping_cart_link").click()

    expect(login.locator(".cart_item")).to_have_count(0)
