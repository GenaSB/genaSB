from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from utilites import logger
from utilites.logger import Logger


class Main_page(Base):

    """  Переход в каталог ноутбуков.

        Шаги:
            1. Открывает текущую страницу
            2. Нажимает кнопку каталога
            3. Нажимает пункт меню "Ноутбуки"
            4. Проверяет успешность перехода по слову "Ноутбуки" """


    #Locators
    catalog_button = "//a[@class='h__catalog-toggle catalog-toggle js-catalog-toggle']"
    menu_button = "//a[@href='/catalog/portable-devices/notebooks']"
    product_type_word = "body > div.site-main > div > div.wrapper > div.bc > a:nth-child(2)"

    #Getters
    def get_catalog_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.catalog_button)))
    def get_menu_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.menu_button)))
    def get_main_word(self):
            return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.product_type_word)))

        #Actions
    def click_catalog_button(self):
        self.get_catalog_button().click()
        print("Click catalog button")
    def click_menu_button(self):
        self.get_menu_button().click()
        print("Click menu button")
    def show_section_titl(self):
        titles = self.get_main_word()
        text = titles.text
        print(f"Раздел: {text}")

        #Methods
    def go_to_catalog(self):
        self.get_current_url()
        self.click_catalog_button()
        self.click_menu_button()
        self.assert_word(self.get_main_word(), "Ноутбуки")
        self.show_section_titl()













