Feature: Complete Checkout

   Scenario Outline: Alerts clicking

    Given User launches heroku web application
     When User clicks on java alerts
     And User click on JS alert
#     And User accept the JS alert
#     And User dismiss the JS alert
     And User navigates back to home page
     And User clicks on dropdown link
#     And User clicks on dropdown box
     And User selects "Option 1" from dropdown
     And User navigates back to home page
     And User prints page title
     And User prints current url
     And User verifies current url
#     And User clicks file upload
#     And User uploads "C:\Users\DELL\CVPavanKalyan.pdf"
#     And User navigates back to home page
# Git Learning



Examples:
| username      | password     |
| standard_user | secret_sauce |
