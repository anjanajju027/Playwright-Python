import time

import pytest
from playwright.sync_api import Page, Playwright
from playwright.sync_api import sync_playwright,expect


def test_playwrightbasics(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/")
    page.close()


def test_playwright(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learning")
    page.get_by_role("combobox").select_option("teach")
    page.locator("//input[@type='checkbox']").check()
    page.get_by_role("link",name="terms and conditions").click()
    page.get_by_role("button",name="Sign In").click()
    time.sleep(5)
    page.close()


# wrong credentials give to check working assertions 
def test_wrongprediction(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learning356476")
    page.get_by_role("combobox").select_option("teach")
    page.locator("//input[@type='checkbox']").check()
    page.get_by_role("link",name="terms and conditions").click()
    page.get_by_role("button",name="Sign In").click()
    expect(page.get_by_text("Incorrect username/password")).to_be_visible()


# firefox or edge browser


def test_Firefox(playwright:Playwright):
    firefox = playwright.firefox.launch(headless=False)
    firefox_page = firefox.new_page()

@pytest.mark.skip
def test_Edge():
    with sync_playwright() as p:
        brows = p.chromium.launch(channel="msedge",headless=False)
        cont = brows.new_context()
        edge_page = cont.new_page()
        edge_page.goto("https://rahulshettyacademy.com/loginpagePractise/")
        print(edge_page.title())