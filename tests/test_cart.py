from playwright.sync_api import expect
from pages.cart_page import CartPage


def test_add_product_to_cart(login):
    cart_page = CartPage(login)

    cart_page.add_first_product()
    expect(cart_page.get_cart_badge()).to_have_text("1")

    cart_page.open_cart()

    expect(cart_page.get_cart_items()).to_have_count(1)
    expect(login.get_by_text("Sauce Labs Backpack")).to_be_visible()


def test_remove_product_from_cart(login):
    cart_page = CartPage(login)

    cart_page.add_first_product()
    cart_page.remove_product()

    expect(cart_page.get_cart_badge()).to_have_count(0)

    cart_page.open_cart()

    expect(cart_page.get_cart_items()).to_have_count(0)


def test_initial_cart_is_empty(login):
    cart_page = CartPage(login)

    cart_page.open_cart()

    expect(cart_page.get_cart_items()).to_have_count(0)
