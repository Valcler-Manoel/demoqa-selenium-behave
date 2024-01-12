from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support.ui import Select
import unittest

@given("the user is on the Demoqa homepage")
def given_user_on_demoqa_homepage(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://demoqa.com/")
    context.driver.maximize_window()
    time.sleep(3)

@when("the user navigates to the \"Practice Form\" section")
def when_user_navigates_to_practice_form(context):
    forms_button = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//h5[text()='Forms']"))
    )
    forms_button.click()
    time.sleep(3)

    practice_form_button = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()='Practice Form']"))
    )
    practice_form_button.click()
    time.sleep(3)


@when("the user fills in the following details:")
def when_user_fills_in_details(context):
    demoqa_page = DemoqaPage(context.driver)
    demoqa_page.open_practice_form()

    data = {}
    for row in context.table:
        data[row["Field"]] = row["Value"]

    demoqa_page.fill_form(data)
    time.sleep(3)

@then("the user should see successful form submission")
def then_user_should_see_successful_submission(context):
    demoqa_page = DemoqaPage(context.driver)
    demoqa_page.submit_form()
    time.sleep(3)


class DemoqaPage:
    def __init__(self, driver):
        self.driver = driver

    def open_practice_form(self):
        self.driver.get("https://demoqa.com/practice-form")
        time.sleep(3)

    def fill_form(self, data):
        for field, value in data.items():
            time.sleep(3)
            self.driver.find_element(By.ID, field.lower()).send_keys(value)
        time.sleep(3)

    def submit_form(self):
        self.driver.find_element(By.ID, "submit").click()
        time.sleep(3)



