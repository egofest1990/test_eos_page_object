from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, browser):
        self.browser = browser
        # self.base_url = "https://auth.eos.com/?v=1591385739205#!/sign-up?embed=crop-" \
                        # "monitoring&return_url=https://eos.com/crop-monitoring/"
        # self.base_url_login = "https://auth.eos.com/#!/sign-in?return_url=https:%2F%2Feos.com%2Fcrop-" \
                              # "monitoring%2Fmain-map%2Ffields%2Fall"
        self.base_url = "https://eos.com/crop-monitoring/login"
        self.base_url_login = "https://auth.eos.com/#!/sign-in?return_url=https:%2F%2Feos.com%2Fcrop-" \
                              "monitoring%2Fmain-map%2Ffields%2Fall"

    def find_element(self, locator, time=10):
        return WebDriverWait(self.browser, time).until(EC.presence_of_element_located(locator),
                                                       message=f"Can't find element by locator {locator}")

    def open(self):
        return self.browser.get(self.base_url)

    def open_login(self):
        return self.browser.get(self.base_url_login)
