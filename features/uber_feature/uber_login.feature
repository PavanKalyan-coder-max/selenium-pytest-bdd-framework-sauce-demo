#Feature: Complete Checkout

#   Scenario Outline: Login feature
#
#    Given User launches uber web application
#        When User enters valid email
#        And User clicks on continue
#        #     And User clicks on more options
#        #     And User clicks on password option
#        And User enters valid uber password
#        And User clicks on next button
#        And User clicks on vehicles beta
#        #     And User clicks on filters
##        And User clicks on filters and verifies all filter options
#        And User clicks on add vehicles
#        And User writes vehicles name
#        And User writes optional name
#        And User uploads vehicle registration document
#        And User click on add vehicle submit button
##        And User verifies the added vehicle is visible in the vehicles list
#        And User clicks on tickets tab
#        And User clicks on create new ticket
#        And User selects test1 vehicle
#        And User selects issue type lost items
#        And User enters description
#        And User click on submit and claim button
#

  Feature: Uber supplier login

  Scenario Outline: Login with different credentials
    Given User launches uber web application
    When User enters email "<username>"
    And User clicks on continue
#    And User clicks on more options
#    And User clicks on password option
    And User enters password "<password>"
    And User clicks on next button


Examples:
| username      | password     |
| nlogan+test+avfleet@ext.uber.com | Uber12345 |
| sontapavan@gmail.com | Uber12345 |