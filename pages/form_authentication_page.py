from selenium.webdriver.common.by import By

from pages.base import BasePage


class FormAuthentication(BasePage):

    class Locators:

        PAGE_TITLE = By.XPATH, "//h2[text()='Login Page']"
        USERNAME = By.XPATH, "//input[@id='username']"
        PASSWORD = By.XPATH, "//input[@id='password']"
        LOGIN_BUTTON = By.XPATH, "//i[contains(text(), 'Login')]"
        LOG_IN_MESSAGE = By.XPATH, "//div[@class='flash success']"
        LOG_OUT = By.XPATH, "//i[contains(text(), 'Logout')]"
        LOG_OUT_MESSAGE = By.XPATH, "//div[@class='flash success']"

    class Credentials:

        username = "tomsmith"
        password = "SuperSecretPassword!"

    def get_page_title(self) -> str:
        return self.get_element(self.Locators.PAGE_TITLE).text

    def input_username(self) -> None:
        self.input_value(self.Locators.USERNAME, self.Credentials.username)

    def input_password(self) -> None:
        self.input_value(self.Locators.PASSWORD, self.Credentials.password)

    def click_login(self) -> None:
        self.click(self.Locators.LOGIN_BUTTON)

    def get_log_in_message(self) -> str:
        return self.get_element(self.Locators.LOG_IN_MESSAGE).text[:30]

    def click_logout(self) -> None:
        self.click(self.Locators.LOG_OUT)

    def get_log_out_message(self) -> str:
        return self.get_element(self.Locators.LOG_OUT_MESSAGE).text[:34]