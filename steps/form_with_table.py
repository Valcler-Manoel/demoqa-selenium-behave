import time
from selenium import webdriver
from behave import when, given, step
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@given("the Demoqa registration page is open")
def demoqa_homepage(context):
    context.driver = webdriver.Firefox()
    context.driver.get("https://demoqa.com/automation-practice-form")
    context.driver.maximize_window()

    # Verify the actual URL
    actual_url = context.driver.current_url
    assert actual_url == "https://demoqa.com/automation-practice-form", f"Expected URL: {actual_url}"


@when('provide valid "{firstName}" "{lastName}" "{userEmail}" "{userNumber}"')
def step_impl(context, firstName, lastName, userEmail, userNumber):
    wait = WebDriverWait(context.driver, 10)

    elem_firstname = wait.until(EC.presence_of_element_located((By.ID, "firstName")))
    elem_firstname.clear()
    elem_firstname.send_keys(firstName)
    time.sleep(1)

    elem_lastname = wait.until(EC.presence_of_element_located((By.ID, "lastName")))
    elem_lastname.clear()
    elem_lastname.send_keys(lastName)
    time.sleep(1)

    elem_useremail = wait.until(EC.presence_of_element_located((By.ID, "userEmail")))
    elem_useremail.clear()
    elem_useremail.send_keys(userEmail)
    time.sleep(1)

    male_radio_button = WebDriverWait(context.driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//label[text()="Male"]'))
    )
    context.driver.execute_script("arguments[0].click();", male_radio_button)
    time.sleep(1)

    elem_usernumber = wait.until(EC.presence_of_element_located((By.ID, "userNumber")))
    elem_usernumber.clear()
    elem_usernumber.send_keys(userNumber)
    time.sleep(2)


@step('click "Submit" button')
def submit_button(context):
    click_button = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.ID, "submit"))
    )
    click_button.click()
    time.sleep(1)
