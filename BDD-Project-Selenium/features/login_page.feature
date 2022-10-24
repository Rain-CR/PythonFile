Feature: Login page

  Scenario: Try login test
    Given I am on the login page
    When I enter a correct username
    And I enter a correct password
    Then I click on the login button
