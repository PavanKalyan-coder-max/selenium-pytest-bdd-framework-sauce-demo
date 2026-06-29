Feature: logout scenario


   Scenario Outline: logout

   Given User launches SauceDemo application

    When User logs in with "<username>" and "<password>"
    And User clicks hamburgermenu
    Then User logouts the application












     Examples:
| username      | password     |
| standard_user | secret_sauce |
