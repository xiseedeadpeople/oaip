Feature: Editing and deleting a record

  Scenario: Editing a record
    Given I have an existing record in the database
    When I edit the record data
    And I click the "Save" button
    Then the record should be updated in the database

  Scenario: Deleting a record
    Given I have an existing record in the database
    When I click the "Delete" button for that record
    Then the record should be removed from the database
