# Created by kroum at 2/11/2026
Feature: run the test

  Scenario: User can go to settings and see the right number of UI elements **
    Given Open the main page https://soft.reelly.io
    When Log in to the page
    And Click on the settings option
    Then Verify the right page opens
    And Verify there are 18 options for the settings
    And Verify the “connect the company” button is available

