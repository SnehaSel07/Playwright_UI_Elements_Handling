import re
import time
from playwright.sync_api import Page, expect, sync_playwright

def test_bing_radio():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)

        page = browser.new_page()
        page.goto("https://www.bing.com/account/general?ru")

        #Assertion
        #expect(page.get_by_role("radio", name="Strict")).not_to_be_checked()
        #handling radio button
        page.get_by_role("radio", name="Strict").check()
        time.sleep(3)
        page.get_by_role("radio", name="Moderate").check()
        time.sleep(3)
        page.get_by_role("radio", name="off").check()
        time.sleep(3)

        #Saving the decision
        #page.get_by_role("button", name="Save").click()
        #time.sleep(3)




        #Assertion
        #expect(page.get_by_role("checkbox", name="See search suggestions as you type")).not_to_be_checked()
        #handling checkbox
        #page.get_by_role("checkbox", name="See search suggestions as you type").check()
        #time.sleep(2)


