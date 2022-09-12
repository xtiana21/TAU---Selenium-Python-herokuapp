from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

class LoginPage:
    #locators
    USERNAME_INPUT = (By.ID, 'username')
    PASSWORD_INPUT = (By.ID, 'password')

    # URL
    URL = "https://the-internet.herokuapp.com/login"

    def __init__(self, browser):
       self.browser = browser

    def load_page(self):
        self.browser.get(self.URL)

    def insert_password(self, password):
        self.browser.find_element(*self.PASSWORD_INPUT).send_keys(password)

    def insert_username(self, username):
        self.browser.find_element(*self.USERNAME_INPUT).send_keys(username)

    def click_login(self):
        self.browser.find_element(*self.USERNAME_INPUT).send_keys(Keys.ENTER)

    def login(self, username, password):
        self.insert_username(username)
        self.insert_password(password)
        self.click_login()