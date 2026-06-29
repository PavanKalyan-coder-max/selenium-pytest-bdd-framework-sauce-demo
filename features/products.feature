Feature: products page


   Scenario Outline: Complete purchase

   Given User launches SauceDemo application

    When User logs in with "<username>" and "<password>"
    And User clicks hamburgermenu
    And User clicks on about
    And User clicks on products





     Examples:
     | username      | password     |
     | standard_user | secret_sauce |