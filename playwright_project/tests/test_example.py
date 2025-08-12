from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.firefox.launch(headless=False)  # ব্রাউজার দেখানোর জন্য headless=False
    page = browser.new_page()
    page.goto("https://www.google.com")

    page.locator("textarea[name='q']").fill("siful islam")
    page.keyboard.press("Enter")

    page.wait_for_timeout(5000)  # ৫ সেকেন্ড অপেক্ষা করে
    browser.close()
