import re
import time
from playwright.sync_api import Page, expect, sync_playwright

def test_mmt():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)

        page = browser.new_page()
        page.goto("https://www.bing.com/account/general?ru")

        #Assertion
        expect(page.get_by_role("checkbox", name="See search suggestions as you type")).to_be_checked()
        #handling checkbox
        page.get_by_role("checkbox", name="See search suggestions as you type").uncheck()
        time.sleep(2)


        #Assertion
        expect(page.get_by_role("checkbox", name="See search suggestions as you type")).not_to_be_checked()
        #handling checkbox
        page.get_by_role("checkbox", name="See search suggestions as you type").check()
        time.sleep(2)


