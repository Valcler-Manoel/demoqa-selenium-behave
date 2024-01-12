import time
from selenium import webdriver
from behave import given, when, then, step
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support import expected_conditions as EC


class DemoqaPage:
    def __init__(self, driver):
        self.driver = driver

    def find_element_by_id(self, element_id):
        return self.driver.find_element(By.ID, element_id)


@given("the user is on the registration page")
def demoqa_homepage(context):
    context.driver = webdriver.Firefox()
    context.driver.get("https://demoqa.com/automation-practice-form")
    context.driver.maximize_window()

    # Verify the actual URL
    actual_url = context.driver.current_url
    assert actual_url == "https://demoqa.com/automation-practice-form", f"Expected URL: {actual_url}"


@when("the user fills in the registration form with valid data")
def valid_data_registration(context):
    wait = WebDriverWait(context.driver, 10)
    elem_firstname = wait.until(expected_conditions.presence_of_element_located((By.ID, "firstName")))
    elem_firstname.clear()
    elem_firstname.send_keys("Válcler")
    time.sleep(1)

    elem_lastname = wait.until(expected_conditions.presence_of_element_located((By.ID, "lastName")))
    elem_lastname.clear()
    elem_lastname.send_keys("Manoel")
    time.sleep(1)

    # Click on "Male" Button.
    male_radio_button = WebDriverWait(context.driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//label[text()="Male"]'))
    )
    context.driver.execute_script("arguments[0].click();", male_radio_button)
    time.sleep(1)

    # Fill up the phone number
    elem_usernumber = wait.until(expected_conditions.presence_of_element_located((By.ID, "userNumber")))
    elem_usernumber.clear()
    elem_usernumber.send_keys("5585986321")
    time.sleep(1)


@step('press the "Submit" button')
def submit_button(context):
    submit_button = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.ID, "submit"))
    )
    submit_button.click()
    time.sleep(1)


@then("the user should see a success message")
def success_message(context):
    modal_title = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.ID, "example-modal-sizes-title-lg"))
    )

    # Verify the actual modal title
    assert modal_title.text == "Thanks for submitting the form", f"Expected title: {modal_title.text}"
    context.driver.quit()
