import time
from selenium import webdriver
from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DemoqaPage:
    def __init__(self, driver):
        self.driver = driver

    def find_element_by_id(self, element_id):
        return self.driver.find_element(By.ID, element_id)


@given("the user is on the Demoqa homepage")
def demoqa_homepage(context):
    """
        Opens the Demoqa site in Firefox and maximizes the window.

        Args:
            context: A context object that contains information about the current state of the test.
        """
    context.driver = webdriver.Firefox()
    context.driver.get("https://demoqa.com")
    context.driver.maximize_window()
    time.sleep(1)


@when("the user clicks on the \"Forms\" button")
def practice_form(context):
    """
        Click in "Forms" button.

        Raises:
            TimeoutException: If the element is not located within the specified wait time.
         """
    forms_button = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//h5[text()='Forms']"))
    )
    forms_button.click()
    time.sleep(1)


@when("navigates to the \"Practice Form\" section")
def user_fills_in_details(context):
    """
        Click in "Practice Form" button.

        Raises:
            TimeoutException: If the element is not located within the specified wait time.
        """
    practice_form_button = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()='Practice Form']"))
    )
    practice_form_button.click()
    time.sleep(1)


@then("the user should be in registration page")
def registration_page(context):
    """
        Opens the DemoQA site in a Firefox browser and verifies the actual URL.

        Args:
            context: A context object that contains information about the current state of the test.

        Raises:
            AssertionError: If the actual URL does not match the expected URL.
        """
    expected_url = "https://demoqa.com/automation-practice-form"
    actual_url = context.driver.current_url
    assert actual_url == expected_url, f"Expected URL: {expected_url}, Actual URL: {actual_url}"
    context.driver.quit()
