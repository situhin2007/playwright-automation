# 🎭 Playwright Automation

Automated end-to-end testing framework built with **Playwright** and **Python** for web applications.  
This repository contains reusable test scripts, modular test design, and practical examples to ensure web application quality.

---

## 📌 Features
- 🚀 Fast browser automation with **Playwright** (Chromium, Firefox, WebKit)
- ✅ Cross-browser testing
- 🔄 Reusable test functions and modular structure
- 📂 Organized folder structure for easy scaling
- 📜 Example test cases for login, form submissions, and validations
- 📊 Supports headless and headed browser modes
- 🔧 Easy integration with CI/CD pipelines

---

## 📂 Project Structure

playwright-automation/
│── tests/ # Test scripts
│── pages/ # Page Object Model (POM) files
│── utils/ # Helper functions
│── requirements.txt # Python dependencies
│── README.md # Documentation


---

## 🛠 Installation

1️⃣ **Clone the repository**
```bash
git clone https://github.com/your-username/playwright-automation.git
cd playwright-automation

2️⃣ Create & activate virtual environment

python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate

3️⃣ Install dependencies

pip install -r requirements.txt

4️⃣ Install Playwright browsers

playwright install

▶️ Usage

Run all tests

pytest

Run a specific test file

pytest tests/test_login.py

Run in headed mode

browser = p.chromium.launch(headless=False)

🔗 Supported Browsers

    Chromium

    Firefox

    WebKit (Safari)

🤝 Contributing

Contributions are welcome!

    Fork the repository

    Create a feature branch (git checkout -b feature-name)

    Commit your changes (git commit -m "Add new feature")

    Push to the branch (git push origin feature-name)

    Open a Pull Request

🧑‍💻 Author

Name: Siful Islam
💼 Software Quality Assurance Engineer
📧 Email: situhin2007@gmail.com


This project is licensed under the MIT License — you are free to use, modify, and distribute.
⭐ If you found this helpful, please star the repository!
