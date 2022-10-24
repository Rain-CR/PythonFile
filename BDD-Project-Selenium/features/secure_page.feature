Feature: Secure Page

  Scenario: Verify correct login and logout
    Given I connect with correct user and password
    When Check if the  message: ' You logged into a secure area!' is displayed
    Then I click the logout button
