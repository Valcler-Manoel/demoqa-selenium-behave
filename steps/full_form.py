import os
import time
from selenium import webdriver
from selenium.webdriver import Keys
from behave import given, when, then, step
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions, expected_conditions as EC


class DemoqaPage:
    def __init__(self, driver):
        self.driver = driver

    def find_element_by_id(self, element_id):
        return self.driver.find_element(By.ID, element_id)


@given("the user should be in registration page")
def demoqa_homepage(context):
    context.driver = webdriver.Firefox()
    context.driver.get("https://demoqa.com/automation-practice-form")
    context.driver.maximize_window()

    # Verify the actual URL
    actual_url = context.driver.current_url
    assert actual_url == "https://demoqa.com/automation-practice-form", f"Expected URL: {actual_url}"


@when("the user fills in all the form fields")
def step_impl(context):
    wait = WebDriverWait(context.driver, 10)
    elem_firstname = wait.until(expected_conditions.presence_of_element_located((By.ID, "firstName")))
    elem_firstname.clear()
    elem_firstname.send_keys("Anderson")
    time.sleep(1)

    elem_lastname = wait.until(expected_conditions.presence_of_element_located((By.ID, "lastName")))
    elem_lastname.clear()
    elem_lastname.send_keys("Silva")
    time.sleep(1)

    elem_useremail = wait.until(expected_conditions.presence_of_element_located((By.ID, "userEmail")))
    elem_useremail.clear()
    elem_useremail.send_keys("anderson.silva@gmail.com")
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

    # Date of Birth
    date_of_birth_input = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'dateOfBirthInput'))
    )

    date_of_birth_input.click()
    time.sleep(1)

    year_selector = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, 'react-datepicker__year-select'))
    )

    year_selector.send_keys("2005")
    time.sleep(1)

    month_selector = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, 'react-datepicker__month-select'))
    )

    month_selector.send_keys("April")
    time.sleep(1)

    day_selector = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//div[@aria-label="Choose Thursday, April 7th, 2005"]'))
    )
    day_selector.click()
    time.sleep(1)

    # Subject
    campo_input = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.ID, "subjectsInput"))
    )
    campo_input.click()
    time.sleep(1)

    campo_input.send_keys("Computer Science")
    campo_input.click()
    time.sleep(1)

    campo_input.send_keys(Keys.TAB)
    time.sleep(1)

    # Choosing a hobby
    checkbox_label = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//label[@for='hobbies-checkbox-3']"))
    )
    checkbox_label.click()

    # Uploading a profile picture
    elem_profile_pic = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.ID, "uploadPicture"))
    )
    time.sleep(1)
    file_path = os.path.abspath("Astronaut.png")
    elem_profile_pic.send_keys(file_path)
    time.sleep(1)

    # Fill up the current address
    elem_useraddress = wait.until(expected_conditions.presence_of_element_located((By.ID, "currentAddress")))
    elem_useraddress.clear()
    elem_useraddress.send_keys("National Capital Region, New Okhla Industrial Development Authority")
    time.sleep(1)


@step("he concludes")
def submit_button(context):
    submit_button = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.ID, "submit"))
    )
    submit_button.click()
    time.sleep(1)


@then("a modal appears with the mirror of the answer")
def step_impl(context):
    modal_title = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.ID, "example-modal-sizes-title-lg"))
    )

    # Verify the actual modal title
    assert modal_title.text == "Thanks for submitting the form", f"Expected title: {modal_title.text}"
    context.driver.quit()
