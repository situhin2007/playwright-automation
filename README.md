# Playwright Automation Project

This repository contains automated end-to-end (E2E) tests built with **Playwright** and **Python**.  
The goal of this project is to provide fast, reliable, and maintainable browser tests for web applications.

---

## 📂 Project Structure

playwright_project/
├── tests/
│ └── test_example.py
├── requirements.txt
├── README.md
└── playwright.config.py


---

## 🚀 Features
- Cross-browser testing (Chromium, Firefox, WebKit)
- Headless and headed test execution
- Page object model (POM) support
- CI/CD ready for GitHub Actions
- Screenshots and videos on failure

---

## 🔧 Installation

1. **Clone the repository**
```bash
git clone https://github.com/YourUsername/playwright-automation.git
cd playwright-automation

    Create & activate virtual environment

python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

    Install dependencies

pip install -r requirements.txt

    Install Playwright browsers

playwright install

▶️ Running Tests

Run all tests:

pytest

Run tests in headed mode:

pytest --headed

Run a specific test file:

pytest tests/test_example.py

📷 Reports, Screenshots & Videos

    Screenshots: Stored automatically on test failure

    Videos: Can be enabled in pytest.ini or playwright.config.py

📜 License

This project is licensed under the MIT License.
🤝 Contributing

Pull requests are welcome!
Please follow proper commit messages and create descriptive PR titles.
📧 Contact

Author: Siful Islam
Email: situhin2007@gmail.com
GitHub: https://github.com/situhin2007
