from playwright.sync_api import Playwright
from playwright.sync_api import sync_playwright,expect
from Utils.apiBase import Api

mail = "anjanajju027@gmail.com"
password = "Govindha10"

# any accounts having order id apart from our account we need to acess the other person order then will you are not authorized.
#for tha above scenario will use route continue to use other person order id
# for this we ar mocking the order link with another account for checking msg to show not authorized.

def interceptRequest(route):
    route.continue_(url="https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=67c83c8dc019fb1ad617a36f")


def test_Network(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False,slow_mo=500)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/client")
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=*",interceptRequest) #?id=* it is regular expression catches any order id
    page.get_by_placeholder("email@example.com").fill(mail)
    page.get_by_placeholder("enter your passsword").fill(password)
    page.get_by_role("button", name="Login").click()
    page.get_by_role("button", name="ORDERS").click()
    page.get_by_role("button",name="View").first.click()
    #use Debug button for slow mo and page loactors
    message = page.locator(".blink_me").text_content()
    print(message)



#Scenario3
#using token and key directly login without filling credentials to the website.

def test_withoutcredentials(playwright:Playwright):
    token = Api()
    get_token = token.get_Token(playwright)
    browser = playwright.chromium.launch(headless=False,slow_mo=200)
    context = browser.new_context()
    page = context.new_page()
    page.add_init_script(f"""localStorage.setItem('token','{get_token}')""")
    page.goto("https://rahulshettyacademy.com/client")
    page.get_by_role("button", name="ORDERS").click()
    expect(page.get_by_text("Your Orders")).to_be_visible()

    context.close()
