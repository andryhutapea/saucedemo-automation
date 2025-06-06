
Feature: Automate SauceDemo

  Scenario: User can Add "Sauce Labs Backpack" to cart
    Given user open Login page
    When user login with Valid Account
    And user add "Sauce Labs Backpack" to Chart
    Then Chart must contain item "Sauce Labs Backpack"

  Scenario: User can Add "Sauce Labs Fleece Jacket" to cart
    Given user open Login page
    When user login with Valid Account
    And user add "Sauce Labs Fleece Jacket" to Chart
    Then Chart must contain item "Sauce Labs Fleece Jacket"

  Scenario: User can open About page from Hamburger menu
    Given user open Login page
    When user login with Valid Account
    And user opens the Hamburger menu and click "About"
    Then user should be redirected to About page

  Scenario: User adds all T-shirt products to the cart
    Given user open Login page
    When user login with Valid Account
    And user adds all products containing "T-shirt" to the cart
    Then cart should contain all "T-shirt" products
