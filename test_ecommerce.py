from playwright.sync_api import Playwright, expect


def test_ecommerce(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False,slow_mo=1000)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://www.saucedemo.com/")
    page.get_by_placeholder("Username").fill("visual_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button",name="Login").click()
    page.locator("#add-to-cart-sauce-labs-bike-light").click()
    page.locator("#add-to-cart-sauce-labs-fleece-jacket").click()
    # .shopping_cart_badge fo cart class cart button clicking
    page.locator(".shopping_cart_link").click()
    page.get_by_role("button",name="Checkout").click()
    page.get_by_placeholder("First Name").fill("Om namaha")
    page.get_by_placeholder("Last Name").fill("Shiva")
    page.get_by_placeholder("Zip/Postal Code").fill("77777")
    page.get_by_role("button",name="Continue").click()
    page.get_by_role("button",name="Finish").click()
    message = page.locator(".complete-header").text_content()
    print(message)
    expect(page.locator("//h2[contains(text(),'Thank you for your order!')]")).to_have_text("Thank you for your order!")
    page.locator("#react-burger-menu-btn").click()
    page.locator("#logout_sidebar_link").click(timeout=100)