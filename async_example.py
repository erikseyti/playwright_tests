import asyncio
from playwright.async_api import async_playwright
import os


async def main():
    browsers = ["chromium"]
    async with async_playwright() as p:
        for browser_type in browsers:
            browser = await p[browser_type].launch()
            page = await browser.new_page()
            await page.goto("https://amazon.com")
            base = os.getcwd()
            await page.screenshot(path=f"{base}/amazon_home_page/py_{browser_type}.png", full_page=True)
            await page.wait_for_timeout(1000)
            await browser.close()


asyncio.run(main())
