
from playwright.sync_api import Page, Playwright
from playwright.sync_api import Page, expect

import pytest

@pytest.mark.smoke
def test_CartAdd(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learning")
    page.get_by_role("combobox").select_option("teach")
    page.get_by_role("link", name="terms and conditions").click()
    page.get_by_role("button", name="Sign In").click()
    iphone =page.locator("app-card").filter(has_text="iphone X")
    iphone.get_by_role("button").click()
    Blackberry = page.locator("app-card").filter(has_text="Blackberry")
    Blackberry.get_by_role("button").click()
    page.get_by_text("Checkout").click()
    expect(page.locator("//div[@class='media-body']")).to_have_count(2)
    page.get_by_text("Checkout").click()
    input = page.locator("//input[@id='country']")
    input.click()
    input.fill("India")
    input.click()
    # Wait for the suggestions to be attached to the DOM
    page.locator("//div[@class='suggestions']").wait_for(state="attached",
                                                         timeout=100000)
    # Wait for the country dropdown to become visible
    suggestions = page.locator("//div[@class='suggestions']")
    suggestions.wait_for(state="visible", timeout=100000)  # Wait for the suggestions to be visible
    # Debugging: Print all suggestion texts to see what is available
    suggestion_texts = [suggestion.inner_text() for suggestion in suggestions.locator("span").all()]
    print("Available Suggestions:", suggestion_texts)  # This helps identify if "India" is actually in the list
    # Try to click the "India" suggestion
    india_suggestion = suggestions.locator("text=India")
    # Ensure the element exists and is visible before clicking
    if india_suggestion.is_visible():
        india_suggestion.click()
    else:
        print("India suggestion not found in the list.")

    page.close()
#page.locator("//div[@class='suggestions']").wait_for(state="attached")
    # Find and click on the "India" suggestion
    #suggestions = page.locator("//div[@class='suggestions']//span")
    # Wait for the suggestion containing "India" to appear
    #india_suggestion = suggestions.locator("text=India")
    # Click on the India suggestion
    #india_suggestion.click()
   # for index in range(page.locator("//div[@class='suggestions']")).count():
        #if page.locator("//div[@class='suggestions']").nth(index).filter(has_text="India").click():
            #break
    #page.wait_for_selector("//a[contains(text(),'India')]").click()
    #India_op = page.locator("//a[contains(text(),'India')]")
    #India_op.wait_for(state="visible",timeout=10000)
    #page.locator("//input[@id ='checkbox2']").check()
    #page.get_by_role("button",name="Purchase").click()
