from playwright.sync_api import expect
from pages.products_page import ProductsPage


def test_product_count(login):
    products_page = ProductsPage(login)

    expect(products_page.get_products()).to_have_count(6)


def test_sort_products_a_to_z(login):
    products_page = ProductsPage(login)

    products_page.sort_products("az")
    names = products_page.get_product_names()

    assert names == sorted(names)


def test_sort_products_price_low_to_high(login):
    products_page = ProductsPage(login)

    products_page.sort_products("lohi")
    prices = products_page.get_product_prices()

    assert prices == sorted(prices)
