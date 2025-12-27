# MINI-PROJECT-1 ✅

**Automated end-to-end test suite** implemented with Python, pytest and Selenium using the Page Object Model (POM).

---

## 📌 Project Overview

This repository contains automated UI tests for a sample web application. The tests are organized using the Page Object Model to keep locators and page interactions separate from test logic, and are driven by configuration values placed in `config.ini`.

The test suite includes features such as logging, HTML test reports, and screenshot capture on failures.

---

## 🔧 Tech Stack

- Python 3.10+
- pytest
- Selenium
- pytest-html (for HTML test reports)

See `requirements.txt` for the full list of dependencies.

---

## 📁 Project Structure

- `pages/` - Page objects for the application (e.g., `login_page.py`, `inventory_page.py`)
- `tests/` - pytest test modules (e.g., `test_login.py`)
- `utils/` - helper modules (`config_reader.py`, `logger.py`)
- `config.ini` - test configuration (base URL, credentials, browser, etc.)
- `reports/` - generated HTML test reports (`report.html`)
- `screenshots/` - screenshots taken during failures
- `logs/` - test run logs

---

## ⚙️ Configuration

Edit `config.ini` to provide test configuration values (base URL, username, password, browser). `utils/config_reader.py` reads these values for use in tests.

Example `config.ini` snippet:

```
[DEFAULT]
base_url = https://www.saucedemo.com
username = standard_user
password = secret_sauce
browser = chrome
implicit_wait = 10
```

---

## ▶️ How to run the tests

1. Create a Python virtual environment and activate it:

   - Windows (PowerShell):
     ```powershell
     python -m venv .venv
     .\.venv\Scripts\Activate.ps1
     ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run all tests:

   ```bash
   pytest -v
   ```

4. Run a specific test file:

   ```bash
   pytest tests/test_login.py -q
   ```

5. Generate an HTML report:

   ```bash
   pytest --html=reports/report.html
   ```

6. View screenshots and logs in `screenshots/` and `logs/` respectively if tests fail.

---

## 🧩 Writing tests (Guidelines)

- Use the Page Object Model: add pages under `pages/` and expose methods for interactions.
- Keep test logic in `tests/` and use fixtures from `conftest.py` for setup/teardown.
- Use `utils/logger.py` to add structured logs to the `logs/` directory.
- On failures, screenshots are taken to `screenshots/` (check the test hooks that capture screenshots).

---

## ✅ Adding Features / Contributing

- Fork the repo and create a branch for features/fixes
- Keep tests atomic and focused
- Run `pytest` locally and make sure the tests pass
- Open a pull request describing the change

---

## 📞 Contact & License

- Author: Satish
- License: MIT — see the `LICENSE` file (if applicable).

---

If you'd like, I can also add badges (build, coverage), a quick start script, or a CONTRIBUTING.md file. 🔧
