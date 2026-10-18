class LoginPage:
    def __init__(self, page):
        self.page = page

    def open(self):
        self.page.goto("https://www.saucedemo.com/")

    def enter_username(self, username):
        self.page.get_by_role("textbox", name="Username").fill(username)

    def enter_password(self, password):
        self.page.get_by_label("Password").fill(password)

    def click_login(self):
        self.page.locator("#login-button").click()