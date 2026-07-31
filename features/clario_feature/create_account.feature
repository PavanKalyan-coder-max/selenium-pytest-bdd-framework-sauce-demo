
  Feature: Create Account

   Scenario Outline: create a new account

    Given User launches ERT Clario URL
        When User clicks on create acocunt
        And User enters Email "<email>"

#        And User enters Confirm Email "<confirm_email>"
#
#        And User enters First Name "<first_name>"
#
#        And User enters Last Name "<last_name>"
#
#        And User enters Password "<password>"
#
#        And User enters Confirm Password "<confirm_password>"
#
#        Then User details should be entered successfully

      Examples:

          | email             | confirm_email     | first_name | last_name | password | confirm_password |
          | pavan@gmail.com   | pavan@gmail.com   | Pavan      | Sonta     | Test@123 | Test@123         |
          #| rahul@gmail.com   | rahul@gmail.com   | Rahul      | Kumar     | Test@123 | Test@123         |
          #| john@gmail.com    | john@gmail.com    | John       | David     | Test@123 | Test@123         |