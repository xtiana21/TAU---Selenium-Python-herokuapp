import time
from pages.javascript_alerts_page import AlertsPage


def test_alert(browser):
    alert_page = AlertsPage(browser)
    alert_page.load_page()
    alert_page.open_alert()
    time.sleep(5)
    alert_page.accept_alert()
    assert 'You successfully clicked an alert' == alert_page.get_result_message()
    time.sleep(5)

def test_confirm_dismiss(browser):
    alert_page = AlertsPage(browser)
    alert_page.load_page()
    alert_page.open_confirm()
    time.sleep(5)
    alert_page.cancel_confirm()
    assert 'You clicked: Cancel' == alert_page.get_result_message()
    time.sleep(5)

def test_confirm_accept(browser):
    alert_page = AlertsPage(browser)
    alert_page.load_page()
    alert_page.open_confirm()
    time.sleep(5)
    alert_page.accept_confirm()
    assert 'You clicked: Ok' == alert_page.get_result_message()
    time.sleep(5)

def test_input_alert(browser):
    alert_page = AlertsPage(browser)
    alert_page.load_page()
    alert_page.open_prompt()
    alert_page.insert_alert('alabalaportocala')
    alert_page.accept_alert()
    time.sleep(5)
    assert 'You entered: alabalaportocala' == alert_page.get_result_message()
