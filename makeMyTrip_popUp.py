
from playwright.sync_api import sync_playwright, expect
import pytest

def test_mmt():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)


        page = browser.new_page()
        #page.goto("https://www.makemytrip.com")
        page.goto("https://www.makemytrip.com/flights/")

        # Handle popup if it appears
        page.locator(".commonModal__close").click()

        # Locate the element using XPath
        locator = page.locator(
                    "xpath=//*[@id='top-banner']/div[2]/div/div/div/div/div"
                    "/div[2]/div[3]/div[2]/div/div[1]/span"
        )

        value = locator.inner_text() #capturing the text
        print(value)


        browser.close()
