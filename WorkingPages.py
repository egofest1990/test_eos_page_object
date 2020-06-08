from .Locators import RegisterPageLocators, AccountLoginTransition
from .BasePages import BasePage
import time


class WorkingOnElements(BasePage):
    def entered_first_name(self, word):
        please = self.find_element(RegisterPageLocators.FIRST_NAME_FIELD)
        please.click()
        please.send_keys(word)
        return please

    def entered_last_name(self, word):
        give = self.find_element(RegisterPageLocators.LAST_NAME_FIELD)
        give.click()
        give.send_keys(word)
        # time.sleep(2)
        return give

    def entered_email(self, word):
        me = self.find_element(RegisterPageLocators.EMAIL_FIELD)
        me.click()
        me.send_keys(word)
        return me

    def entered_password(self, word):
        this = self.find_element(RegisterPageLocators.PASSWORD_FIELD)
        this.click()
        this.send_keys(word)
        return this

    def entered_phone_number(self, word):
        job = self.find_element(RegisterPageLocators.PHONE_NUMBER_FIELD)
        job.click()
        job.send_keys(word)
        return job

    def click_checkbox(self):
        please = self.find_element(RegisterPageLocators.CHECKBOX)
        please.click()
        time.sleep(2)
        return please

    def click_registration_button(self):
        return self.find_element(RegisterPageLocators.BUTTON_SUBMIT, time=3).click()

    def check_registration_passed(self):
        assert self.find_element(RegisterPageLocators.CHECK_BUTTON, time=2), "Registration Failed!!!"

    def account_login_transition_button(self):
        pass
        # return self.find_element(AccountLoginTransition.AUTH_LOGIN).click()

    def entered_auth_login(self, word):
        set_in = self.find_element(AccountLoginTransition.AUTH_EMAIL)
        set_in.click()
        set_in.send_keys(word)
        return set_in

    def entered_auth_login_password(self, word):
        set_inn = self.find_element(AccountLoginTransition.AUTH_PASSWORD)
        set_inn.click()
        set_inn.send_keys(word)
        time.sleep(3)
        return set_inn

    def submit_button_login(self):
        set_n = self.find_element(AccountLoginTransition.SIGN_IN_BUTTON)
        set_n.click()
        return set_n

    def login_assert(self):
        assert self.find_element(AccountLoginTransition.BUTTON_USER_MENU, time=10), "Button user menu not Found!!!"
