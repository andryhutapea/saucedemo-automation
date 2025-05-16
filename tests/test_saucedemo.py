import os
import sys
from pytest_bdd import scenarios, given, when, then, parsers
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.menu_page import MenuPage
from dotenv import load_dotenv

# Tambahkan path agar bisa impor modul dari folder 'pages'
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

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


@then(parsers.parse('Chart must contain item "{item}"'))
def verify_cart(driver, item):
    cart = CartPage(driver)
    cart.open_cart()
    assert cart.is_item_in_cart(item), f"Item '{item}' not found in cart!"


@when(parsers.parse('user opens the Hamburger menu and click "{menu_item}"'))
def open_menu_item(driver, menu_item):
    menu = MenuPage(driver)
    menu.open_menu()
    menu.click_menu_item(menu_item)


@then("user should be redirected to About page")
def verify_about(driver):
    assert "saucelabs.com" in driver.current_url
