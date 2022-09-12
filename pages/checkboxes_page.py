from selenium.webdriver.common.by import By

class CheckboxesPage:
    #locators
    CHECHBOX_SUBTITLE = (By.CSS_SELECTOR, 'h3').text
    CHECKBOX_1_CHECK = (By.CSS_SELECTOR, 'checkboxes > input[type=checkbox]:nth-child(1)' )
    CHECKBOX_2_CHECK = (By.CSS_SELECTOR, 'checkboxes > input[type=checkbox]:nth-child(3)')


    #URL
    URL = 'https://the-internet.herokuapp.com/checkboxes'

    def __init__(self, browser):
       self.browser = browser

    def load_page(self):
        self.browser.get(self.URL)

