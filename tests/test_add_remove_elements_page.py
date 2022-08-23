from selenium.webdriver.common.by import By

from pages.add_remove_elements_page import AddRemoveElementsPage


def test_check_add_element_functionality(browser):
    add_remove_page = AddRemoveElementsPage(browser)
    add_remove_page.load_page()        # deschidem o pagina
    add_remove_page.clickAddButton()   # dam click pe Add Button
    assert add_remove_page.isAddButtonDisplayed()     # verificare afisare buton


def test_check_url(browser):
    browser.get('https://the-internet.herokuapp.com/add_remove_elements/')
    url = 'https://the-internet.herokuapp.com/add_remove_elements/'
    get_url = browser.current_url
    assert url == get_url


def test_title(browser):
    browser.get('https://the-internet.herokuapp.com/add_remove_elements/')
    title = browser.find_element(By.CSS_SELECTOR, 'h3').text
    assert title == 'Add/Remove Elements'

def test_link(browser):
    browser.get('https://the-internet.herokuapp.com/add_remove_elements/')
    link = browser.find_element(By.LINK_TEXT, 'Elemental Selenium')
    assert link.is_displayed()
    link.click()
    browser.switch_to.window(browser.window_handles[1])
    assert 'http://elementalselenium.com/' == browser.current_url

def test_add_and_delete_functionality(browser):
    browser.get('https://the-internet.herokuapp.com/add_remove_elements/') # deschidem pagina
    add_element_button = browser.find_element(By.CSS_SELECTOR, "[onclick='addElement()']") # cream varabila pentru buton

    for i in range(10):
      add_element_button.click()   # click pe Button List de 10 ori
    delete_button_list = browser.find_elements(By.CLASS_NAME, "added-manually")

    assert len(delete_button_list) == 10, "Not all delete button is displayed"

    for i in range(10):
        delete_button_list[0].click()
        delete_button_list = browser.find_elements(By.CLASS_NAME, "added-manually")
        assert len(delete_button_list) == 10-i-1, "Not all delete button is displayed"


