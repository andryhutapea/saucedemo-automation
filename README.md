# Project Name: SauceDemo Automation Testing

## Description
This project is an automated test suite for the SauceDemo website using Selenium, pytest, and BDD. It includes test scenarios for adding items to the cart, logging in, and navigating through the website. It also integrates Allure Report and pytest-html for test result reporting.

### Technology
It's using BDD approach and Gherkin syntax for implementation. This project is using following basic technology:
1. Pipenv for dependency management using virtual environment. 
2. Selenium 4 to automate web browser
3. PyTest BDD for test framework.
4. Allure UI for test reporting.

---

## Prerequisites

Make sure the following are installed on your system:

- **Python 3.8+**: You need Python to run the tests.
- **Selenium**: WebDriver for automating web browsers.
- **pytest**: Testing framework.
- **pytest-bdd**: Behavior-Driven Testing for pytest.
- **pytest-html**: HTML reporting plugin for pytest.
- **allure-pytest**: Allure reporting plugin for pytest.
- **Google Chrome** (or another browser of choice) and the corresponding **WebDriver**.

To install all dependencies, use the provided `requirements.txt`.

---

## Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/andryhutapea/saucedemo-automation.git
cd <your-project-directory>
```
### Step 2: Install Dependencies
Ensure you have Python 3.8+ installed on your system. Then, install the required Python libraries using pip.

```bash
pip install -r requirements.txt
```

### Step 3: Install Allure Command Line
If you're using Allure Report, you need to install Allure Command Line. If you're on macOS, use Homebrew:
```bash
brew install allure
```
For other operating systems, download Allure from the official Allure GitHub page and follow the installation instructions.

### Folder Structure
1. features/: Contains Gherkin feature files (BDD scenarios).
2. pages: contains page object for all pages.
3. tests/: Contains Python test scripts for Selenium-based automation.
4. reports/: Contains generated test reports (Allure and HTML).
5. screenshots/: Stores screenshots for failed tests.
6. conftest.py: Configurations for pytest fixtures and hooks.
7. pytest.ini: config file
8. .env: environment variable (this project is not using envar yet)


### Example Test Scenario (BDD)
Here is an example of a feature file for adding items to the cart:
```
Feature: Automate SauceDemo
  Scenario: User can Add "Sauce Labs Backpack" to cart
    Given user open Login page
    When user login with Valid Account
    And user add "Sauce Labs Backpack" to Chart
    Then Chart must contain item "Sauce Labs Backpack"
```

### Running Tests
To run the SauceDemo Automation Testing:
```bash
./run_saucedemo_tests.sh
```

To run the specific tests, you can try this:
1. Run the tests with pytest and generate Allure results:
```bash
pytest --alluredir=reports/allure-results --html=reports/report.html --self-contained-html
```
2. To generate the Allure report:
```bash
allure generate reports/allure-results --clean -o reports/allure-report
```


### Result Tests
For this project you can view result using Allure Report & html result 
1. To view Result Test using Allure Report:
```bash
allure open reports/allure-report
```
2. To view Result Test using html result
```bash
open reports/report.html
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
### Branching strategy
This project is using `main` branch as main branch. We merge all of our work into `main` branch. All CI/CD projects are using `main` branch as well. So if you want to contribute to this project, please create your branch from `main` and pull request it.
### Who do I talk to?
1.  Author (Andry)
