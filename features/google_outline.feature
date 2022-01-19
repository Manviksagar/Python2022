@smoke
Feature: working google home page
  Scenario Outline: google home page working
    Given User entered the url
    When user enter user "<name>"
    Then user enter the passwords
    And user clicks on submit button
    Examples:
      | name |
      | Sagar |
      | Allu  |

