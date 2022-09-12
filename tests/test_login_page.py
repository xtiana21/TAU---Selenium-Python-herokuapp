import pytest as pytest

from pages.login_page import LoginPage
from pages.secure_page import SecurePage

@pytest.mark.pozitive
def test_check_login_functionality(browser):
    login_page = LoginPage(browser)
    login_page.load_page()
    login_page.login('tomsmith', 'SuperSecretPassword!')
    secure_page = SecurePage(browser)
    assert 'Welcome to the Secure Area. When you are done click logout below.' == secure_page.getWelcomeMessage()
    assert browser.current_url == secure_page.URL