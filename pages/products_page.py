class ProductsPage:
    def __init__(self, page):
        self.page = page

    def get_products(self):
        return self.page.locator(".inventory_item")

    def sort_products(self, option):
        self.page.locator(".product_sort_container").select_option(option)

    def get_product_names(self):
        return self.page.locator(".inventory_item_name").all_text_contents()

    def get_product_prices(self):
        prices = self.page.locator(".inventory_item_price").all_text_contents()
        return [float(price.replace("$", "")) for price in prices]
