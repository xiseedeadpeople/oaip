Feature: Displaying records in the application

  Scenario: Displaying all records
    Given I have records in the database
    When I open the "View" window
    Then I should see all the records listed
