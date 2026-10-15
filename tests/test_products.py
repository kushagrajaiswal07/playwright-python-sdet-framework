
from playwright.sync_api import expect

def test_product_count(login):
    products = login.locator(".inventory_item")

    expect(products).to_have_count(6)


def test_sort_products_a_to_z(login):
    login.locator(".product_sort_container").select_option("az")

    names = login.locator(".inventory_item_name").all_text_contents()

    assert names == sorted(names)


def test_sort_products_price_low_to_high(login):
    login.locator(".product_sort_container").select_option("lohi")

    prices = login.locator(".inventory_item_price").all_text_contents()
    prices = [float(price.replace("$", "")) for price in prices]

    assert prices == sorted(prices)
