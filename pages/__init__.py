from pages.ab_testing_page import AbTesting
from pages.add_remove_element_page import AddRemoveTesting
from selenium import webdriver
from pages.herokuapp_home_page import HomePage
from pages.form_authentication_page import FormAuthentication
from pages.dropdown_page import Dropdown
from pages.javascript_alerts_page import JavaScriptAlerts

'''
'driver: webdriver.Remote' --> giving type of 'driver', it's called 'typowanie'
'''


def get_starting_page(driver: webdriver.Remote, base_url: str) -> webdriver:
    driver.get(base_url)
    return HomePage(driver)
