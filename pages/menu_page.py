from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MenuPage:
    def __init__(self, driver):
        self.driver = driver

    def open_menu(self):
        self.driver.find_element(By.ID, "react-burger-menu-btn").click()

    def click_menu_item(self, item_text):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, item_text))
        ).click()
