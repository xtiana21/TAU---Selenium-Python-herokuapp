import time
from pages.cotext_menu_page import ContextMenuPage


def test_context_menu(browser):
    context_menu_page = ContextMenuPage(browser)
    context_menu_page.load_page()
    context_menu_page.open_menu()
    time.sleep(5)
    context_menu_page.accept_alert()

