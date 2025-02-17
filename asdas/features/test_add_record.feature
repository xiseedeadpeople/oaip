Feature: Adding a record to the database

  Scenario: Adding a valid record
    Given I have opened the application
    When I enter valid data into the form
    And I click the "Add" button
    Then the new record should be added to the database
