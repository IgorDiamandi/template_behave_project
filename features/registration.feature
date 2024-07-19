Feature: User Registration

  Scenario: Successful registration
    Given I am on the registration page
    When I register with a valid username and password
    Then I should see a success message

  Scenario: Failed registration
    Given I am on the registration page
    When I register with an invalid username
    Then I should see an error message
