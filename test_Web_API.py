from playwright.sync_api import Playwright
from Utils.apiBase import Api
from playwright.sync_api import sync_playwright,expect

mail = "anjanajju027@gmail.com"
password = "Govindha10"
def test_Web_API(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False,slow_mo=1000)
    context = browser.new_context()
    page = context.new_page()

    util = Api()
    order = util.Createorder(playwright)

    page.goto("https://rahulshettyacademy.com/client")
    page.get_by_placeholder("email@example.com").fill(mail)
    page.get_by_placeholder("enter your passsword").fill(password)
    page.get_by_role("button",name="Login").click()
    page.get_by_role("button",name="ORDERS").click()

    #checking the order id using assertion

    row = page.locator("tr").filter(has_text=order)
    row.get_by_role("button",name="View").click()
    expect(page.locator(".tagline")).to_contain_text("Thank you for Shopping With Us")
    print(order)

