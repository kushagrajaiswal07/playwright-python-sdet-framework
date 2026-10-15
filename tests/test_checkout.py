
from playwright.sync_api import expect

def test_complete_checkout(login):
    login.get_by_role("button", name="Add to cart").first.click()

    login.locator(".shopping_cart_link").click()
    login.get_by_role("button", name="Checkout").click()

    login.get_by_role("textbox", name="First Name").fill("Kushagra")
    login.get_by_role("textbox", name="Last Name").fill("Jaiswal")
    login.get_by_role("textbox", name="Zip/Postal Code").fill("560001")

    login.get_by_role("button", name="Continue").click()

    expect(login.get_by_text("Checkout: Overview")).to_be_visible()

    login.get_by_role("button", name="Finish").click()

    expect(login.get_by_text("Thank you for your order!")).to_be_visible()


def test_checkout_without_first_name(login):
    login.get_by_role("button", name="Add to cart").first.click()
    login.locator(".shopping_cart_link").click()
    login.get_by_role("button", name="Checkout").click()

    login.get_by_role("textbox", name="Last Name").fill("Jaiswal")
    login.get_by_role("textbox", name="Zip/Postal Code").fill("560001")

    login.get_by_role("button", name="Continue").click()

    expect(login.get_by_text("Error: First Name is required")).to_be_visible()


def test_checkout_without_postal_code(login):
    login.get_by_role("button", name="Add to cart").first.click()
    login.locator(".shopping_cart_link").click()
    login.get_by_role("button", name="Checkout").click()

    login.get_by_role("textbox", name="First Name").fill("Kushagra")
    login.get_by_role("textbox", name="Last Name").fill("Jaiswal")

    login.get_by_role("button", name="Continue").click()

    expect(login.get_by_text("Error: Postal Code is required")).to_be_visible()


def test_checkout_without_last_name(login):
    login.get_by_role("button", name="Add to cart").first.click()
    login.locator(".shopping_cart_link").click()
    login.get_by_role("button", name="Checkout").click()

    login.get_by_role("textbox", name="First Name").fill("Kushagra")
    login.get_by_role("textbox", name="Zip/Postal Code").fill("560001")

    login.get_by_role("button", name="Continue").click()

    expect(login.get_by_text("Error: Last Name is required")).to_be_visible()
