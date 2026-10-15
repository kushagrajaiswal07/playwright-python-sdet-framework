import pytest
from pathlib import Path
from playwright.sync_api import Page
import os
from dotenv import load_dotenv

load_dotenv()

@pytest.fixture
def api_base_url():
    return os.getenv("API_BASE_URL")

@pytest.fixture
def login(page: Page):
    page.goto("https://www.saucedemo.com/")

    page.get_by_role("textbox", name="Username").fill("standard_user")
    page.get_by_label("Password").fill("secret_sauce")
    page.locator("#login-button").click()

    return page


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")

        if page:
            Path("screenshots").mkdir(exist_ok=True)
            page.screenshot(
                path=f"screenshots/{item.name}.png",
                full_page=True
            )



@pytest.fixture
def api_base_url():
    return "https://jsonplaceholder.typicode.com"
