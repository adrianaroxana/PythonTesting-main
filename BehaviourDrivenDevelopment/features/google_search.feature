Feature: Search something on Google
  As an Internet user
  I want to be able to access Google
  In order to search for information

  Scenario: Open Google and insert value "Coronavirus"
    Given I access google.ro
    When I type 'Coronavirus' in textfield
    Then I want to see the news regarding the subject
