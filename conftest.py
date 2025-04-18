import pytest

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="browser__options"
    )

pytest.fixture(scope='session')
def user_credentials(request):
    return request.param

def browser_instance(playwright,request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chorme":
        browser = playwright.chromium.launch(headless=False)
    elif browser_name == "firefox":
        browser = playwright.firefox.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()


        yield page
        context.close()

        browser.close()
