from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class InventoryPage:
    def __init__(self, driver):
        self.driver = driver

    def add_to_cart(self, item_name):
        button = self.driver.find_element(By.XPATH, f"//div[text()='{item_name}']/ancestor::div[@class='inventory_item']//button")
        button.click()
