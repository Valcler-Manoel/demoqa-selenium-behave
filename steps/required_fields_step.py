import time
from selenium import webdriver
from behave import when, then, given
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DemoqaPage:
    def __init__(self, driver):
        self.driver = driver

    def find_element_by_id(self, element_id):
        return self.driver.find_element(By.ID, element_id)


@given("the user is on the Demoqa registration page")
def demoqa_homepage(context):
    context.driver = webdriver.Firefox()
    context.driver.get("https://demoqa.com/automation-practice-form")
    context.driver.maximize_window()

    context.demoqa_page = DemoqaPage(context.driver)

    time.sleep(1)


@when("the user leaves the First Name field blank")
def first_name_blank(context):
    elem_firstname = context.demoqa_page.find_element_by_id("firstName")
    elem_firstname.clear()
    time.sleep(1)


@when("leaves the Last Name field blank")
def last_name_blank(context):
    elem_lastname = context.demoqa_page.find_element_by_id("lastName")
    elem_lastname.clear()
    time.sleep(1)


@when("leaves the User Number field blank")
def user_number_blank(context):
    elem_usernumber = context.demoqa_page.find_element_by_id("userNumber")
    elem_usernumber.clear()
    time.sleep(1)


@when("clicks on the \"Submit\" button")
def submit_button(context):
    submit_button = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.ID, "submit"))
    )
    submit_button.click()
    time.sleep(1)


@then("the user should see error messages indicating the mandatory fields")
def error_messages(context):
    pass
    context.driver.quit()
