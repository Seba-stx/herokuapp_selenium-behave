from selenium.webdriver.common.by import By
from random import randint

from pages.base import BasePage


class AddRemoveTesting(BasePage):

    class Locators:

        PAGE_TITLE = By.XPATH, "//h3"
        ADD_ELEMENT_BUTTON = By.XPATH, "//button[text()='Add Element']"
        DELETE_BUTTON = By.XPATH, "//button[text()='Delete']"

    def get_page_title(self) -> str:
        return self.get_element(self.Locators.PAGE_TITLE).text

    def click_add_element_button(self) -> None:
        self.number_of_clicks = randint(1, 10)
        for i in range(self.number_of_clicks):
            self.click(self.Locators.ADD_ELEMENT_BUTTON)

    def get_delete_button(self):
        return self.get_element(self.Locators.DELETE_BUTTON).is_displayed()

    def click_delete_button(self):
        for i in range(self.number_of_clicks):
            self.click(self.Locators.DELETE_BUTTON)

    def check_if_delete_button_available(self):
        return self.check_invisibility_of_element(self.Locators.DELETE_BUTTON)