from selenium.webdriver.common.by import By

class SecurePage:
    #locators
    WELCOME_TEXT = (By.CSS_SELECTOR, 'h4')

    # URL
    URL = "https://the-internet.herokuapp.com/secure"

    def __init__(self, browser):
       self.browser = browser

    def load_page(self):
        self.browser.get(self.URL)

    def getWelcomeMessage(self):
        return self.browser.find_element(*self.WELCOME_TEXT).text