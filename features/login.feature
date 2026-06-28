
#@regression
Feature: Complete Checkout

#  Scenario: Complete purchase
   Scenario Outline: Complete purchase

    Given User launches SauceDemo application
#    When User enters valid username and password
    When User logs in with "<username>" and "<password>"

    And User adds backpack to cart

    And User clicks cart icon

    And User clicks checkout button

    And User enters checkout information

    And User clicks finish button

    Then User should see order completion page

    And User clicks back home page

    When User adds fleece jacket to cart

    And User clicks cart icon
    And User clicks checkout button
    And User enters checkout information
    And User clicks finish button
    Then User clicks back home page

    When User clicks hamburgermenu
    And User clicks on about
    And User clicks on book a demo
    And User enters business email
    And User enters company name
    And User comments in the free text box
    And User enters first name
    And User enters last name
    And User enters phone number
    And User selects country
    And User selects interest
    And User clicks checkbox
    And User clicks on submit




Examples:
| username      | password     |
| standard_user | secret_sauce |



