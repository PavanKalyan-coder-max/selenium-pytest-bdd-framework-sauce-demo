Feature: Create Account

Scenario: Create a new account

    Given User launches ERT Clario URL
        When User clicks on create acocunt
        And User enters Email from JSON
        And User enters Confirm Email from JSON
        And User enters First Name from JSON
        And User enters Last Name from JSON
        And User enters Password from JSON
        And User enters Confirm Password from JSON
        Then User details should be entered successfully