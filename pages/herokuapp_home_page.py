from selenium.webdriver.common.by import By

from pages.base import BasePage


class HomePage(BasePage):

    class Locators:
        AB_TESTING_BUTTON = By.XPATH, "//a[text()='A/B Testing']"
        ADD_REMOVE_BUTTON = By.XPATH, "//a[text()='Add/Remove Elements']"
        FORM_AUTHENTICATION = By.XPATH, "//a[text()='Form Authentication']"
        DROPDOWN = By.XPATH, "//a[text()='Dropdown']"

    def click_ab_testing(self) -> None:
        self.get_element(self.Locators.AB_TESTING_BUTTON).click()

    def click_add_remove_element(self) -> None:
        self.get_element(self.Locators.ADD_REMOVE_BUTTON).click()

    def click_form_authentication(self) -> None:
        self.get_element(self.Locators.FORM_AUTHENTICATION).click()

    def click_dropdown(self) -> None:
        self.get_element(self.Locators.DROPDOWN).click()

