import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support import expected_conditions as EC

class DemoqaRegisterTest(unittest.TestCase):
    """Testing the registration page and filling up forms"""

    def setUp(self):
        """Using Firefox Browser"""
        self.driver = webdriver.Firefox()

    def test_demoqa_register_form(self):
        """Navigate to register and fill the form"""
        driver = self.driver
        driver.get("http://demoqa.com/")  # navigate to homepage
        self.assertIn("DEMOQA", driver.title)  # check if the page is the home page

        # Creating a WebDriverWait object to wait for 10 seconds.
        wait = WebDriverWait(driver, 10)

        # Wait for the element with the text "Forms".
        forms_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//h5[text()='Forms']"))
        )

        # Click in button "Forms"
        forms_button.click()

        # Waiting for the page to load
        wait.until(EC.url_contains("forms"))

        # Wait for the "Practice Form" button to be clickable
        practice_form_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='Practice Form']"))
        )

        # Click on the "Practice Form" button
        practice_form_button.click()
        print("Clicked on 'Practice Form' button successfully.")

        # creating a WebdriverWait object to wait for 10 seconds
        wait = WebDriverWait(driver, 10)

        # Wait for the textfield to load then filling up the firstname text field
        elem_firstname = wait.until(expected_conditions.presence_of_element_located((By.ID, "firstName")))
        elem_firstname.clear()
        elem_firstname.send_keys("Válcler")

        # Wait for the textfield to load then filling up the lastname text field
        elem_lastname = wait.until(expected_conditions.presence_of_element_located((By.ID, "lastName")))
        elem_lastname.clear()
        elem_lastname.send_keys("Manoel")

        # email
        elem_useremail = wait.until(expected_conditions.presence_of_element_located((By.ID, "userEmail")))
        elem_useremail.clear()
        elem_useremail.send_keys("valcler.manoel@gmail.com")

        #clicking Male checkbox
        driver.find_element_by_css_selector("input[type='radio'][value='Male']").click()

        

if __name__ == "__main__":
    unittest.main()
