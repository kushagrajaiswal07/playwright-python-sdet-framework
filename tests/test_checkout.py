from playwright.sync_api import expect
from pages.checkout_page import CheckoutPage


def test_complete_checkout(login):
    checkout_page = CheckoutPage(login)

    checkout_page.add_first_product()
    checkout_page.open_cart()
    checkout_page.start_checkout()

    checkout_page.enter_first_name("Kushagra")
    checkout_page.enter_last_name("Jaiswal")
    checkout_page.enter_postal_code("560001")
    checkout_page.continue_checkout()

    expect(login.get_by_text("Checkout: Overview")).to_be_visible()

    checkout_page.finish_checkout()

    expect(login.get_by_text("Thank you for your order!")).to_be_visible()


def test_checkout_without_first_name(login):
    checkout_page = CheckoutPage(login)

    checkout_page.add_first_product()
    checkout_page.open_cart()
    checkout_page.start_checkout()

    checkout_page.enter_last_name("Jaiswal")
    checkout_page.enter_postal_code("560001")
    checkout_page.continue_checkout()

    expect(login.get_by_text("Error: First Name is required")).to_be_visible()


def test_checkout_without_postal_code(login):
    checkout_page = CheckoutPage(login)

    checkout_page.add_first_product()
    checkout_page.open_cart()
    checkout_page.start_checkout()

    checkout_page.enter_first_name("Kushagra")
    checkout_page.enter_last_name("Jaiswal")
    checkout_page.continue_checkout()

    expect(login.get_by_text("Error: Postal Code is required")).to_be_visible()


def test_checkout_without_last_name(login):
    checkout_page = CheckoutPage(login)

    checkout_page.add_first_product()
    checkout_page.open_cart()
    checkout_page.start_checkout()

    checkout_page.enter_first_name("Kushagra")
    checkout_page.enter_postal_code("560001")
    checkout_page.continue_checkout()

    expect(login.get_by_text("Error: Last Name is required")).to_be_visible()
