from selenium.webdriver.common.by import By

class AddRemoveElementsPage:
    #locators
    TITLE_TEXT = (By.CSS_SELECTOR, "h3")
    ADD_ELEMENT_BUTTON = (By.CSS_SELECTOR, '[onclick="addElement()"]')
    DELETE_BUTTON = (By.CLASS_NAME, "added-manually")

    # URL
    URL = "https://the-internet.herokuapp.com/add_remove_elements/"

    def __init__(self, browser):
       self.browser = browser

    def load_page(self):
        self.browser.get(self.URL)

    def clickAddButton(self):
        self.browser.find_element(*self.ADD_ELEMENT_BUTTON).click()

    def clickDeleteButton(self):
        self.browser.find_element(*self.DELETE_BUTTON).click()

    def getNumberOfDeleteButton(self):
        return len(self.browser.find_elements(*self.DELETE_BUTTON))

    def clickFirstDeleteButton(self):
        self.browser.find_element(*self.DELETE_BUTTON).click()

    def isAddButtonDisplayed(self):
        return self.browser.find_element(*self.ADD_ELEMENT_BUTTON).is_displayed()

    def isDeleteButtonDisplayed(self):
        return self.browser.find_element(*self.DELETE_BUTTON).is_displayed()

    def getTitlePage(self):
        return self.browser.find_element(*self.TITLE_TEXT).text




