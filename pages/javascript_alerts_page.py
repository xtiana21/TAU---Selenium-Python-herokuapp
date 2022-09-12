from selenium.webdriver.common.by import By

class AlertsPage:
    ALERT_BUTTON = (By.CSS_SELECTOR, '[onclick="jsAlert()"]')
    CONFIRM_BUTTON = (By.CSS_SELECTOR, '[onclick="jsConfirm()"]')
    PROMPT_BUTTON = (By.CSS_SELECTOR, '[onclick="jsPrompt()"]')
    RESULT_MESSAGE = (By.CSS_SELECTOR, '#result')

    URL = "https://the-internet.herokuapp.com/javascript_alerts"

    def __init__(self, browser):
       self.browser = browser

    def load_page(self):
        self.browser.get(self.URL)

    def open_alert(self):
        self.browser.find_element(*self.ALERT_BUTTON).click()

    def open_confirm (self):
        self.browser.find_element(*self.CONFIRM_BUTTON).click()

    def open_prompt (self):
        self.browser.find_element(*self.PROMPT_BUTTON).click()

    def accept_alert(self):
        alert = self.browser.switch_to.alert
        alert.accept()

    def cancel_confirm(self):
        confirm = self.browser.switch_to.alert
        confirm.dismiss()

    def accept_confirm(self):
        confirm = self.browser.switch_to.alert
        confirm.accept()

    def get_result_message(self):
        return self.browser.find_element(*self.RESULT_MESSAGE).text

    def insert_alert(self, text):
        alert = self.browser.switch_to.alert
        alert.send_keys(text)

