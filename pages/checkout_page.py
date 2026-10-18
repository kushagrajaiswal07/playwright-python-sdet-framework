class CheckoutPage:
    def __init__(self, page):
        self.page = page

    def add_first_product(self):
        self.page.get_by_role("button", name="Add to cart").first.click()

    def open_cart(self):
        self.page.locator(".shopping_cart_link").click()

    def start_checkout(self):
        self.page.get_by_role("button", name="Checkout").click()

    def enter_first_name(self, first_name):
        self.page.get_by_role("textbox", name="First Name").fill(first_name)

    def enter_last_name(self, last_name):
        self.page.get_by_role("textbox", name="Last Name").fill(last_name)

    def enter_postal_code(self, postal_code):
        self.page.get_by_role("textbox", name="Zip/Postal Code").fill(postal_code)

    def continue_checkout(self):
        self.page.get_by_role("button", name="Continue").click()

    def finish_checkout(self):
        self.page.get_by_role("button", name="Finish").click()
