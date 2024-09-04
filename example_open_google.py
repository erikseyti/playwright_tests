from playwright.sync_api import sync_playwright
import time

url = "https://www.google.com"


def run(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(
        user_agent="", viewport={"width": 800, "height": 600}, bypass_csp=True
    )
    page = context.new_page()
    page.goto(url)
    time.sleep(5)
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
