import os
from pytest_bdd import scenarios, given, when, then, parsers
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.menu_page import MenuPage
from dotenv import load_dotenv
import pdb;


load_dotenv()
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")

scenarios('../features/saucedemo.feature')


@given("user open Login page")
def open_login(driver):
    driver.get("https://www.saucedemo.com/")


@when("user login with Valid Account")
def login(driver):
    LoginPage(driver).login(USERNAME, PASSWORD)


@when(parsers.parse('user add "{item}" to Chart'))
def add_to_cart(driver, item):
    InventoryPage(driver).add_to_cart(item)


@when(parsers.parse('user add "{item}" to Chart'))
def add_to_cart(driver, item):
    InventoryPage(driver).add_to_cart(item)


@when(parsers.parse('user adds all products containing "{text}" to the cart'))
def add_all_matching_products(driver, text):
    CartPage(driver).add_all_products_with_text(text)


@then(parsers.parse('cart should contain all "{text}" products'))
def verify_all_matching_products_in_cart(driver, text):
    assert CartPage(driver).verify_all_products_in_cart(text)


@when(parsers.parse('user opens the Hamburger menu and click "{menu_item}"'))
def open_menu_item(driver, menu_item):
    menu = MenuPage(driver)
    menu.open_menu()
    menu.click_menu_item(menu_item)


@then("user should be redirected to About page")
def verify_about(driver):
    assert "saucelabs.com" in driver.current_url
