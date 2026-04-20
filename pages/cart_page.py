from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from base.base_class import Base

class Cart_page(Base):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    #Locators
    order_button = "//a[@class='u-f-right btn_yellow']"
    page_name = "//h1[text()='Оформление заказа']"


    #Getters
    def get_order_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.order_button)))
    def get_page_name(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.page_name)))


    #Actions
    def click_order_button(self):
        self.get_order_button().click()
        print("Click order button")
    def click_page_name(self):
        page_name_element = self.get_page_name()
        page_name_text = page_name_element.text
        print(f"Заголовок страницы: {page_name_text}")


    #Methods
    def place_an_order(self):
        self.get_current_url()
        self.driver.maximize_window()
        self.click_order_button()
        self.click_page_name()

















