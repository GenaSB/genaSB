from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from base.base_class import Base


class Laptop_selection_page(Base):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.selected_laptop_name = None
        self.selected_item_name = None
        self.price = None
        self.price2 = None

    #Locators
    choose_laptop = "span.catalog__name"
    name_product = "body > div.site-main > div.title-row > div > h1"
    name_page = "//a[@class='title-nav__item js-title-nav-scroll' and text()='Характеристики']"
    price_product = "//*[@id='sgoodscontainer']/div[1]/div[2]/div/a"
    price_product2 = "//span[@class='card__price card__price--orange']"


    #Getters
    def get_price_product(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.price_product)))
    def get_choose_laptop(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.choose_laptop)))

    def get_name_page(self):
        return WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, self.name_page)))
    def get_name_product(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.name_product)))
    def get_price_product2(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.price_product2)))


    #Actions
    def click_price(self):
        sum_price = self.get_price_product()
        self.price = sum_price.text
        print(f"Цена товара: {self.price}")
    def click_choose_laptop(self):
        laptop_element = self.get_choose_laptop()                   # Сначала получаем элемент
        self.selected_laptop_name = laptop_element.text             # Сохраняем текст
        print(f"Название ноутбука: {self.selected_laptop_name}")
        laptop_element.click()
        print("Click choose laptop")

    def click_name_page(self):
        page_name_element = self.get_name_page()
        page_name_text = page_name_element.text
        print(f"Cтраницa: {page_name_text}")

    def click_name_product(self):
        selected_item = self.get_name_product()
        self.selected_item_name = selected_item.text
        print(f"Название товара: {self.selected_item_name}")
    def click_price2(self):
        sum_price2 = self.get_price_product2()
        self.price2 = sum_price2.text
        print(f"Цена товара: {self.price2}")


    #Methods
    def selection_laptop(self):
        self.get_current_url()
        self.driver.maximize_window()
        self.click_price()
        self.click_choose_laptop()
        self.click_name_page()
        self.click_name_product()
        self.assert_word(self.selected_laptop_name, self.selected_item_name)
        self.click_price2()
        if '\n' in self.price:
            self.price = self.price.split('\n')[1]
        self.assert_word(self.price, self.price2)




















