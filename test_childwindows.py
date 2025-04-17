from playwright.sync_api import Page, Playwright
from playwright.sync_api import sync_playwright,expect

def test_mainwindow(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")

    with page.expect_popup() as newpage_info:
        page.locator(".blinkingText").click()
        child = newpage_info.value
        text = child.locator(".red").text_content()
        print(text)
        word = text.split(".com")
        print(word[0])
        assert word[0]== "Please email us at mentor@rahulshettyacademy"
        new_word = text.split("at")
        email = new_word[1].strip().split(" ")[0]

        assert email == "mentor@rahulshettyacademy.com"
        print(email)
        child.close()

    page.close()







