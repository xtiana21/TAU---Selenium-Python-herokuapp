
def test_check_add_element_functionality(browser):
    browser.get('https://the-internet.herokuapp.com/add_remove_elements/')
    add_element_button = browser.find_element(By.CSS_SELECTOR, '[onclick="addElement()"]')
    add_element_button.click()

    delete_button = browser.find_element(By.CLASS_NAME, 'added-manually')

    assert delete_button.is_displayed()

    time.sleep(5)
    chrome.quit()

def test_check_url():
    pass

def test_title():
    pass

def test_link():
    pass

def test_add_and_delete_functionality(browser):
    browser.get('https://the-internet.herokuapp.com/add_remove_elements/')

    add_element_button = browser.find_element(By.CSS_SELECTOR, '[onclick="addElement()"]')
    for i in range(10): # executam de mai multe ori o functie
        add_element_button.click()

    delete_button_list = browser.find_elements(By.CLASS_NAME, 'added-manually')
    assert len(delete_button_list) == 10, 'Check all delete button is displayed'

    for i in range (10):
        delete_button_list.click()
        assert len(delete_button_list) == 10-i-1


    time.sleep(5)
    chrome.quit()


