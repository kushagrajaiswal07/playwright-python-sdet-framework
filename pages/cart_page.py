class CartPage:
    def __init__(self, page):
        self.page = page

    def add_first_product(self):
        self.page.get_by_role("button", name="Add to cart").first.click()

    def remove_product(self):
        self.page.get_by_role("button", name="Remove").click()

    def open_cart(self):
        self.page.locator(".shopping_cart_link").click()

    def get_cart_badge(self):
        return self.page.locator(".shopping_cart_badge")

    def get_cart_items(self):
        return self.page.locator(".cart_item")
