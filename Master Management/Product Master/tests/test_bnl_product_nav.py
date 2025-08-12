import pytest
from playwright.sync_api import sync_playwright
from pages.sidebar_product_page import ProductSidebarPage
import timepytest

def test_bnl_product_navigation():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # ✅ Step 1: Open ERP Login Page
        page.goto("https://uat.bracnet.net")

        # ✅ Step 2: Login (Change username & password)
        page.fill("input[name='username']", "your_username")
        page.fill("input[name='password']", "your_password")
        page.click("button[type='submit']")
        page.wait_for_timeout(3000)

        # ✅ Step 3: Navigate to BNL Products
        product_nav = ProductSidebarPage(page)
        product_nav.go_to_bnl_products()
        page.wait_for_timeout(3000)

        # ✅ Step 4: Screenshot & Assertion
        page.screenshot(path="screenshots/bnl_products_page.png")
        assert "BNL Products" in page.content()

        browser.close()
