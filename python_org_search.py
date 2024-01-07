import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support import expected_conditions as EC

class DemoqaRegisterTest(unittest.TestCase):
    """Testing the registration page from homepage link and filling up forms"""

    def setUp(self):
        """Using Firefox Browser"""
        self.driver = webdriver.Firefox()

    def test_demoqa_register_form(self):
        """Navigate to register and fill the form"""
        driver = self.driver
        driver.get("http://demoqa.com/")  # navigate to homepage
        self.assertIn("DEMOQA", driver.title)  # check if the page is the home page

        # Creating a WebDriverWait object to wait for 10 seconds
        wait = WebDriverWait(driver, 10)

        # Wait for the element with the text "Forms" to be clickable
        forms_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//h5[text()='Forms']"))
        )

        # Clicar no botão "Forms"
        forms_button.click()

        # Wait for the page to load (you can increase the timeout if needed)
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
        elem_firstname.send_keys("Dante")

        # Wait for the textfield to load then filling up the lastname text field
        elem_lastname = wait.until(expected_conditions.presence_of_element_located((By.ID, "lastName")))
        elem_lastname.clear()
        elem_lastname.send_keys("Abidin")

        # email
        elem_useremail = wait.until(expected_conditions.presence_of_element_located((By.ID, "userEmail")))
        elem_useremail.clear()
        elem_useremail.send_keys("blah@gmail.com")




        #clicking the married radio button as my wife will not be happy if I will click the other option
        #even if this was just a test

        #clicking both reading and dance checkbox
        driver.find_element_by_css_selector("input[type='radio'][value='Male']").click()

        #Filling up date of birth
        #by xpath
        wait.until(expected_conditions.presence_of_element_located((By.XPATH, '//*[@id="mm_date_8"]')))
        Select(driver.find_element_by_xpath('//*[@id="mm_date_8"]')).select_by_value("12")

        #by id
        Select(driver.find_element_by_id("dd_date_8")).select_by_value("12")
        #by id
        Select(driver.find_element_by_id("yy_date_8")).select_by_value("1990")

        #Fill up the phone number
        elem_phone_number = driver.find_element_by_id("phone_9")
        elem_phone_number.clear()
        elem_phone_number.send_keys("09091234567")

        #username
        elem_username = driver.find_element_by_id("username")
        elem_username.clear()
        elem_username.send_keys("blah")

        #email
        elem_email = driver.find_element_by_id("email_1")
        elem_email.clear()
        elem_email.send_keys("blah@gmail.com")

        #Profile Picture Upload#
        #elem_profile_pic = driver.find_element_by_id("profile_pic_10")
        #elem_profile_pic.send_keys(os.getcwd(). + "\\tooth.png")

        #textarea
        elem_textarea = driver.find_element_by_id("description")
        elem_textarea.clear()
        elem_textarea.send_keys("Lorem ipsum")

        #password
        elem_password = driver.find_element_by_id("password_2")
        elem_password.clear()
        elem_password.send_keys("blah")

        #confrim password
        elem_confirm_password = driver.find_element_by_id("confirm_password_password_2")
        elem_confirm_password.clear()
        elem_confirm_password.send_keys("blah")

        #Clicking the submit button
        elem_submit = driver.find_element_by_name('pie_submit').click()


        #assertions
        self.assertIn("Registration", driver.title)  # check if the page is the registration page
        self.assertEquals ("Dante", elem_firstname.get_attribute('value'))
        self.assertEquals("Abidin", elem_lastname.get_attribute('value'))
        self.assertTrue(driver.find_element_by_css_selector("input[type='checkbox'][value='reading']").is_selected())



if __name__ == "__main__":
    unittest.main()