from .WorkingPages import WorkingOnElements
import random


def test_register_form(browser):
    nmbr = random.randint(25, 10000000)
    go_to = WorkingOnElements(browser)
    go_to.open()
    go_to.entered_first_name("Test")
    go_to.entered_last_name("Test")
    go_to.entered_email(f"igorfesenko25+{nmbr}@gmail.com")
    go_to.entered_password("qwerty")
    go_to.entered_phone_number("508585852")
    go_to.click_checkbox()
    go_to.click_registration_button()
    go_to.check_registration_passed()


def test_login_page(browser):
    transition_to = WorkingOnElements(browser)
    transition_to.open_login()
    # transition_to.account_login_transition_button()
    transition_to.entered_auth_login("igorfesenko25+5496768@gmail.com")
    transition_to.entered_auth_login_password("qwerty")
    transition_to.submit_button_login()
    transition_to.login_assert()
