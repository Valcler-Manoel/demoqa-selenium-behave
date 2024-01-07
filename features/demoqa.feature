Feature: Demoqa Registration Form

  Scenario: Fill Practice Form with User Details
    Given the user is on the Demoqa homepage
    When the user navigates to the "Practice Form" section
    And the user fills in the following details:
      | Field         | Value         |
      | firstName     | Dante         |
      | lastName      | Abidin        |
      | userEmail     | blah@gmail.com|
    Then the user should see successful form submission
