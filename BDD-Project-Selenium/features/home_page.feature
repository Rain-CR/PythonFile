Feature: Home page
  Scenario: Redirect to Add/Remove Elements
    Given I am on the home page
    When I click the link for Add/Remove Elements
    Then I am redirected to the 'add_remove_elements' page

  Scenario: Redirect to Checkboxes link
    Given I am on the home page
    When I click the link for checkbox
    Then I am redirected to the 'checkbox' page

  Scenario: Redirect to Form authentication link
    Given I am on the home page
    When I click the link for Form authentication
    Then I am redirected to the 'Form authentication' page