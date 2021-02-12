from selenium.webdriver.common.by import By

from pages.base import BasePage


class HomePage(BasePage):

    class Locators:
        AB_TESTING_BUTTON = By.XPATH, "//a[text()='A/B Testing']"
        ADD_REMOVE_BUTTON = By.XPATH, "//a[text()='Add/Remove Elements']"
        FORM_AUTHENTICATION = By.XPATH, "//a[text()='Form Authentication']"
        DROPDOWN = By.XPATH, "//a[text()='Dropdown']"
        JS_ALERTS = By.XPATH, "//a[text()='JavaScript Alerts']"

    def click_ab_testing(self) -> None:
        self.click(self.Locators.AB_TESTING_BUTTON)

    def click_add_remove_element(self) -> None:
        self.click(self.Locators.ADD_REMOVE_BUTTON)

    def click_form_authentication(self) -> None:
        self.click(self.Locators.FORM_AUTHENTICATION)

    def click_dropdown(self) -> None:
        self.click(self.Locators.DROPDOWN)

    def click_js_alerts(self) -> None:
        self.force_click(self.get_element(self.Locators.JS_ALERTS))


