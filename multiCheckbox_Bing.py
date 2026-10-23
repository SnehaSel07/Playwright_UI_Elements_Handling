import re
import time
from playwright.sync_api import Page, expect, sync_playwright

def test_bing_multicheck():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)

        page = browser.new_page()
        page.goto("https://www.bing.com/account/general?ru")

        checkboxes = page.get_by_role("checkbox")

        #counting total checkboxes in a webpage
        count = checkboxes.count()
        print("total checkboxes = " , count)

        for i in range(3):
            checkboxes.nth(i).uncheck() #uncheking 3 checkboxes out of 7
            time.sleep(1)
