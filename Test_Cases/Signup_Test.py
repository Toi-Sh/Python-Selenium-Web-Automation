import pytest
from selenium import webdriver
from configparser import ConfigParser
from Pages.base_page import BasePage
from Pages.registration_page import RegistrationPage


config_object = ConfigParser()
config_object.read("C:/Users/User/Documents/AgeOfLearning/config.ini")
base_URL = "https://www.abcmouse.com"
driver= webdriver.Chrome()
expectedURL = config_object["testData"]["url1"]
registrationURL = config_object["testData"]["url2"]


def set_up():
    driver.get(base_URL)
    driver.maximize_window()

def test_signup_button():
    bp= BasePage(driver)
    bp.drv.implicitly_wait(5)
    bp.click_signup_button()
    bp.validateURL(expectedURL)

def test_registering_email():
    rp=RegistrationPage(driver)
    rp.enter_email_info()
    rp.click_submit_button()
    rp.validateURL(registrationURL)
    rp.assert_page_tag()

set_up()
test_signup_button()
test_registering_email()
print("Test Complete")
driver.close()

