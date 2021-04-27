from selenium.webdriver.common.by import By


class RegisterPageLocators:
    FIRST_NAME_FIELD = (By.ID, "first_name")
    LAST_NAME_FIELD = (By.ID, "last_name")
    EMAIL_FIELD = (By.ID, "email")
    PASSWORD_FIELD = (By.ID, "password")
    # PHONE_NUMBER_FIELD = (By.NAME, "phone")
    CHECKBOX = (By.ID, "policy_confirm")
    BUTTON_SUBMIT = (By.CSS_SELECTOR, 'button.primary.ui-button')
    CHECK_BUTTON = (By.CSS_SELECTOR, "button.secondary-special.primary.ui-button")


class AccountLoginTransition:
    AUTH_LOGIN = (By.CSS_SELECTOR, "a.ng-scope")
    AUTH_EMAIL = (By.CSS_SELECTOR, "#email")
    AUTH_PASSWORD = (By.CSS_SELECTOR, "#password")
    SIGN_IN_BUTTON = (By.CSS_SELECTOR, "button.submit-btn.primary.ui-button")
    BOTTOM_MENU = (By.CLASS_NAME, "div.sidebar-menu")
    BUTTON_USER_MENU = (By.NAME, "user-menu")
