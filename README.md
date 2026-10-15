# Playwright Python SDET Framework

A beginner-friendly Software Development Engineer in Test (SDET) project built using Python, Playwright, Pytest, and Requests. This project demonstrates UI automation, API testing, reusable fixtures, test reporting, and Continuous Integration using GitHub Actions.

## Tech Stack

- **Python** — Programming language
- **Playwright** — Web UI automation
- **Pytest** — Test execution and fixtures
- **Requests** — REST API testing
- **Git & GitHub** — Version control
- **GitHub Actions** — Continuous Integration (CI)
- **Pytest HTML** — HTML test reports
- **python-dotenv** — Environment variable management

## Project Features

### 1. UI Automation
Automated end-to-end tests for [SauceDemo](https://www.saucedemo.com/).

- Login with valid credentials
- Invalid password validation
- Locked-out user validation
- Product listing verification
- Product sorting by name and price
- Add and remove products from cart
- Cart validation
- Checkout flow and required-field validation

### 2. API Testing
Automated REST API tests using [JSONPlaceholder](https://jsonplaceholder.typicode.com/).

- GET requests and response validation
- Validation of existing and nonexistent resource IDs
- POST requests for resource creation
- PUT requests for full updates
- PATCH requests for partial updates
- DELETE requests
- Response status codes, headers, content type, and response time checks

### 3. Test Framework Features

- Reusable Pytest fixtures
- Centralized test configuration
- Reusable API test data
- Automatic screenshots on test failures
- HTML test report generation
- Environment-based configuration using `.env`
- Automated test execution through GitHub Actions

## Project Structure

```text
playwright-python-sdet-framework/
├── .github/
│   └── workflows/
│       └── tests.yml
├── pages/
├── tests/
│   ├── test_login.py
│   ├── test_products.py
│   ├── test_cart.py
│   ├── test_checkout.py
│   ├── test_api.py
│   └── test_data.py
├── reports/
├── screenshots/
├── .env
├── .gitignore
├── conftest.py
└── requirements.txt
```

*Note: Generated reports, screenshots, and environment files are excluded from version control where configured. The `pages` directory is reserved for Page Object Model implementation.*

## Getting Started

### Prerequisites

- Python 3.12 or a compatible Python version
- Git
- pip

### 1. Clone the repository

```bash
git clone https://github.com/kushagrajaiswal07/playwright-python-sdet-framework.git
cd playwright-python-sdet-framework
```

### 2. Create and activate a virtual environment

**Windows:**

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
playwright install chromium
```

### 4. Configure environment variables

Create a `.env` file in the project root:

```env
API_BASE_URL=https://jsonplaceholder.typicode.com
```

### 5. Run the test suite

```bash
pytest -v
```

### 6. Generate an HTML test report

```bash
pytest -v --html=reports/report.html --self-contained-html
```

Ensure the `reports` directory exists before generating the report.

## Continuous Integration

This project uses **GitHub Actions** to execute the test suite automatically on pushes and pull requests.

The workflow installs dependencies, sets up Playwright with Chromium, and runs the tests in an Ubuntu environment.

**CI Status:** The GitHub Actions workflow has successfully completed with a passing status.

## Learning Objectives

This project demonstrates practical experience with:

- Functional UI testing
- REST API testing
- Test case design and assertions
- Reusable fixtures and test data
- Test automation and debugging
- Test reporting
- Git-based collaboration workflows
- CI pipeline configuration

## Future Improvements

- Implement the Page Object Model (POM)
- Add API schema validation
- Improve test data management
- Add parameterized and negative test scenarios
- Publish test reports as CI artifacts
- Add Docker-based test execution
- Expand automated regression coverage

## Author

**Kushagra Jaiswal**

- GitHub: [@kushagrajaiswal07](https://github.com/kushagrajaiswal07)
- LinkedIn: [kushagra-jaiswal-ai](https://linkedin.com/in/kushagra-jaiswal-ai)

