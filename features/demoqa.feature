Feature: Demoqa Registration Form

  Scenario: The user enters in registration page
    Given the user is on the Demoqa homepage
    When the user clicks on the "Forms" button
    And navigates to the "Practice Form" section
    Then the user should be in registration page

  Scenario: Failure to fill in required fields
    Given the user is on the Demoqa registration page
    When the user leaves the First Name field blank
    And leaves the Last Name field blank
    And leaves the User Number field blank
    And clicks on the "Submit" button
    Then the user should see error messages indicating the mandatory fields

  Scenario: User fills in required information
    Given the user should be in registration page
    When the user fills in the registration form with valid data
    And press the "Submit" button
    Then the user should see a success message

  Scenario: The user fills in the form completely
    Given the user is on the registration page
    When the user fills in all the form fields
    And he concludes
    Then a modal appears with the mirror of the answer

  Scenario Outline: User fills in form using a data table
    Given the Demoqa registration page is open
    When provide valid "<firstName>" "<lastName>" "<userEmail>" "<userNumber>"
    And click "Submit" button
    Then the user should see a success message

    Examples:
  | firstName | lastName | userNumber |      userEmail     |
  | Joao      | Oliveira | 8723414680 | joao.oliveira@email.com |




