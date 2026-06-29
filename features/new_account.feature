Feature: new account app page


   Scenario Outline: Complete purchase

   Given User launches SauceDemo application

    When User logs in with "<username>" and "<password>"
    And User clicks hamburgermenu
    And User clicks on about

    And User clicks on go to app
    And User clicks on try for free
    And User verify index disclaimer text
    And User verify visa logo




     Examples:
| username      | password     |
| standard_user | secret_sauce |
