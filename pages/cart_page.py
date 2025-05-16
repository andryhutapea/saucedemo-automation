from selenium.webdriver.common.by import By


class CartPage:
    def __init__(self, driver):
        self.driver = driver

    def open_cart(self):
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    def is_item_in_cart(self, item_name):
        items = self.driver.find_elements(By.CLASS_NAME, "inventory_item_name")
        return any(item.text == item_name for item in items)
