Feature: communication page


   Scenario Outline: Communication

   Given User launches SauceDemo application

    When User logs in with "<username>" and "<password>"
    And User clicks hamburgermenu
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
    And User verify the text











     Examples:
| username      | password     |
| standard_user | secret_sauce |
