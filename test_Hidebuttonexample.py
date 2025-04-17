from playwright.sync_api import Page, Playwright
from playwright.sync_api import sync_playwright,expect

def test_HideButton(page:Page):

    #To check button visible ,click,diabled
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_visible()
    page.get_by_role("button",name="Hide").click()
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_hidden()

    # Alerts handling
    page.on("dailog",lambda dialog:dialog.accept())
    page.get_by_role("button",name="Confirm")

    #hover
    page.locator("#mousehover").hover()
    page.get_by_role("link",name="Top").click()

    # Frames
    page_frame = page.frame_locator("#courses-iframe")
    page_frame.get_by_role("link",name="All Access plan").click()
    expect(page_frame.locator("body")).to_contain_text("Join 13,522")

    #check the price of rice is equal  to 37
    #identify the price column
    #identify the rice row
    #extraxt the rice of the price
def test_Ui(page:Page):
    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/offers")
    for index in range(page.locator("//th").count()):
        if page.locator("//th").nth(index).filter(has_text="Price").count()>0:
            prcie_val = index
            print(f"price column values is {prcie_val}")
            break
    riceRow = page.locator("//tr").filter(has_text="Rice")
    expect(riceRow.locator("td").nth(prcie_val)).to_have_text("37")

    print(riceRow)

    page.close()



