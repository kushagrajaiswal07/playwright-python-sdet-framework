# Playwright Python SDET Framework

A hands-on test automation project built with **Python, Playwright, Pytest, and Requests**. It demonstrates browser-based UI testing, REST API testing, the Page Object Model (POM), reusable fixtures, test data, failure screenshots, and continuous integration with GitHub Actions.

> **Project goal:** Practice skills used in QA Automation Engineer and SDET roles through a maintainable, beginner-friendly test suite.

## What This Project Tests

### UI automation — SauceDemo

The browser tests cover key shopping workflows on [SauceDemo](https://www.saucedemo.com/):

- Successful login
- Invalid credentials and locked-out user validation
- Product listing count
- Product sorting by name and price
- Adding and removing products from the cart
- Empty-cart behavior
- Completing checkout
- Required checkout-field validation

### REST API testing — JSONPlaceholder

API tests use [JSONPlaceholder](https://jsonplaceholder.typicode.com/) as a practice API and cover:

- GET requests for individual and multiple posts
- Existing and nonexistent resource IDs
- Response status codes and JSON structure
- Response field types and values
- POST resource creation
- PUT full updates and PATCH partial updates
- DELETE requests
- Content type and response-header checks
- Basic response-time assertion
- Parameterized tests for multiple resource IDs

**Note:** JSONPlaceholder is a demo API. Write operations are simulated; they do not persistently modify the public dataset.

## Framework Features

- **Page Object Model (POM):** UI actions are organized into page classes under `pages/`.
- **Pytest fixtures:** Shared browser setup and login setup reduce repeated test code.
- **API configuration:** The API base URL is supplied through the `api_base_url` fixture.
- **Reusable test data:** Example API payloads are kept in `tests/test_data.py`.
- **Failure screenshots:** A screenshot is saved when a UI test fails and a Playwright page is available.
- **HTML reporting:** `pytest-html` is included so a report can be generated locally.
- **Continuous integration:** GitHub Actions installs the dependencies and Chromium, then runs the test suite on pushes and pull requests.

## Tech Stack

| Tool | Purpose |
|---|---|
| Python | Test code |
| Playwright | Browser automation |
| Pytest | Test runner, assertions, fixtures, and parametrization |
| Requests | REST API requests |
| pytest-html | Optional HTML test reports |
| python-dotenv | Loading environment variables |
| Git and GitHub | Version control and repository hosting |
| GitHub Actions | Automated CI test runs |

## Project Structure

```text
playwright-python-sdet-framework/
├── .github/
│   └── workflows/
│       └── tests.yml
├── pages/
│   ├── login_page.py
│   ├── products_page.py
│   ├── cart_page.py
│   └── checkout_page.py
├── tests/
│   ├── test_login.py
│   ├── test_products.py
│   ├── test_cart.py
│   ├── test_checkout.py
│   ├── test_api.py
│   └── test_data.py
├── .gitignore
├── conftest.py
└── requirements.txt
```

Generated screenshots, reports, virtual environments, cache files, and the local `.env` file are excluded from version control by `.gitignore`.

## Run It Locally

### 1. Clone the repository

```bash
git clone https://github.com/kushagrajaiswal07/playwright-python-sdet-framework.git
cd playwright-python-sdet-framework
```

### 2. Create and activate a virtual environment

**Windows (Command Prompt):**

```bat
python -m venv .venv
.venv\\Scripts\\activate
```

**macOS / Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies and Chromium

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
playwright install chromium
```

### 4. Run the test suite

Run all UI and API tests:

```bash
pytest -v
```

Run only UI tests:

```bash
pytest -v tests/test_login.py tests/test_products.py tests/test_cart.py tests/test_checkout.py
```

Run only API tests:

```bash
pytest -v tests/test_api.py
```

### 5. Generate an HTML report (optional)

Create the reports directory first, then run:

**Windows (Command Prompt):**

```bat
if not exist reports mkdir reports
pytest -v --html=reports/report.html --self-contained-html
```

**macOS / Linux:**

```bash
mkdir -p reports
pytest -v --html=reports/report.html --self-contained-html
```

Open `reports/report.html` in a browser to view the report. Generated reports are local artifacts and are ignored by Git.

## Continuous Integration

The workflow at [`.github/workflows/tests.yml`](.github/workflows/tests.yml) runs on pushes and pull requests. It sets up Python 3.12, installs the project dependencies, installs Playwright with Chromium system dependencies, and executes `pytest -v`.

See the [Actions tab](https://github.com/kushagrajaiswal07/playwright-python-sdet-framework/actions) for workflow runs and their results.

## Skills Demonstrated

- Functional UI test automation
- REST API testing and response validation
- Pytest fixtures, assertions, and parameterized tests
- Page Object Model fundamentals
- Reusable test data and configuration
- Failure evidence through screenshots
- Local test reporting
- GitHub Actions CI workflow

## Potential Next Improvements

- Add more negative and boundary-value test cases
- Improve configuration so local and CI environments use the same settings
- Publish test reports as GitHub Actions artifacts
- Add API schema validation
- Expand browser and test-data coverage
- Add database validation with SQL
- Explore Docker-based test execution

## Author

**Kushagra Jaiswal**

- GitHub: [@kushagrajaiswal07](https://github.com/kushagrajaiswal07)
- LinkedIn: [kushagra-jaiswal-ai](https://linkedin.com/in/kushagra-jaiswal-ai)
