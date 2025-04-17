from playwright.sync_api import Playwright

mail = "anjanajju027@gmail.com"
password = "Govindha10"
fakepayload = {"data":[],"message":"No Orders"}
def intrcept_response(route):
    route.fulfill(
        json=fakepayload)


# api call from browser-->api call contact server return back response to browser-->browser use response to generate html
# that reponse we use as fake response and in actual browser we have orders due to route call we are intercepting.
#mocking the original response with fake response.

def test_Network(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False,slow_mo=1000)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/client")
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-for-customer/*",intrcept_response)
    page.get_by_placeholder("email@example.com").fill(mail)
    page.get_by_placeholder("enter your passsword").fill(password)
    page.get_by_role("button", name="Login").click()
    page.get_by_role("button", name="ORDERS").click()
    order_text = page.locator(".mt-4").text_content()
    print(order_text)

    context.close()


