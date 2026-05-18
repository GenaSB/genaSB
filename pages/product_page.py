from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from base.base_class import Base

class Product_page(Base):


    #Locators
    add_product_button = "//a[@class='add-basket card__add-basket--yellow  card__add-basket js-add-basket']"
    cart_button = "//*[@id='headBasketCount']"
    page_name = "//h1[text()='Корзина']"
    item_in_cart = "//span[@class='basket__name']"
    final_price = "//span[@class='price basket__pay-price']"


    #Getters
    def get_add_product_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.add_product_button)))
    def get_cart_button(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.cart_button)))
    def get_page_name(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.page_name)))
    def get_item_in_cart(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.item_in_cart)))
    def get_final_price(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.final_price)))

    #Actions
    def click_add_product_button(self):
        self.get_add_product_button().click()
        print("Click add product button")
    def click_cart_button(self):
        self.get_cart_button().click()
        print("Click button")
    def click_page_name(self):
        page_name_element = self.get_page_name()
        page_name_text = page_name_element.text
        print(f"Заголовок страницы: {page_name_text}")
        return page_name_text
    def click_item_in_cart(self):
        product_in_cart = self.get_item_in_cart()
        self.in_cart = product_in_cart.text
    def click_final_price(self):
        pay_money = self.get_final_price()
        self.price_in_cart = pay_money.text


    #Methods
    def add_to_cart(self, price2, selected_item_name):
        self.get_current_url()
        self.driver.maximize_window()
        self.click_add_product_button()
        self.click_cart_button()
        self.click_page_name()
        self.click_item_in_cart()
        self.click_final_price()
        self.assert_word(self.in_cart, selected_item_name)
        self.assert_word(self.price_in_cart, price2)
















