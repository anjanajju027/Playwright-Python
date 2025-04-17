import json

import pytest
from playwright.sync_api import Playwright

from PageObjects.dasboard import Dashboard
from PageObjects.login import Login
from PageObjects.orderhistory import OrderHistoy
from PageObjects.viewdetailspage import ViewDetails
from Utils.apiBaseFramework import Api
from playwright.sync_api import sync_playwright,expect

# jsno-->utils--->access into test.
with open("data/credentials.json") as f:
        test_dat = json.load(f)
        print(test_dat)
        data_list = test_dat['user_credentials']


@pytest.mark.parametrize("user_credentials",data_list)
def test_Web_API(playwright:Playwright,user_credentials):
    email = user_credentials["email"]
    password = user_credentials["Password"]
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
#create order id using token
    util = Api()
    order = util.Createorder(playwright,user_credentials)
#login page
    login_page = Login(page)  #object for login page
    login_page.navigation(user_credentials)
    login_page.login(email, password)
    #dashboard =login_page.login(email, password) we can more optimze like this
#click on orders page
    dashboard = Dashboard(page)
    dashboard.navigateorder()
 #checking the order id using assertion
    order_history_page = OrderHistoy(page)
    order_history_page.orderhist()
# row = page.locator("//tr").filter(has_text=order)
#row.get_by_role("button",name="View").click()

#view details page and assertion using expect to see the text
    view_details_page = ViewDetails(page)
    view_details_page.Vieworderdetails()
    print(order)


