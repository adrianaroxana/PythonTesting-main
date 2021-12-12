Feature: Login on herokuapp.com
  As a registered user
  I want to be able to click login button
  So I could access the site info

  Scenario: Login with valid credentials
    Given I enter https://www.herokuapp.com
    When I enter correct credentials
    Then I access the site info

