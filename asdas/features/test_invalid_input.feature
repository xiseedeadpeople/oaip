Feature: Handling invalid input

  Scenario: Adding a record with invalid data
    Given I have opened the application
    When I enter invalid data into the form
    And I click the "Add" button
    Then I should see an error message
