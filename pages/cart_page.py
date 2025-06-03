from selenium.webdriver.common.by import By


class CartPage:
    def __init__(self, driver):
        self.driver = driver

    def open_cart(self):
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    def add_all_products_with_text(self, keyword):
        products = self.driver.find_elements(By.CLASS_NAME, "inventory_item")
        for product in products:
            title = product.find_element(By.CLASS_NAME, "inventory_item_name").text
            if keyword.lower() in title.lower():
                button = product.find_element(By.TAG_NAME, "button")
                button.click()

    def verify_all_products_in_cart(self, keyword):
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        cart_items = self.driver.find_elements(By.CLASS_NAME, "inventory_item_name")
        matched_items = [item.text for item in cart_items if keyword.lower() in item.text.lower()]
        return len(matched_items) > 0 and all(keyword.lower() in name.lower() for name in matched_items)

    def is_item_in_cart(self, item_name):
        items = self.driver.find_elements(By.CLASS_NAME, "inventory_item_name")
        return any(item.text == item_name for item in items)
