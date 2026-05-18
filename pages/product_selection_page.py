from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from base.base_class import Base


class Product_selection_page(Base):

    #Locators
    checkbox_label = "(//span[@class='checkbox-ps'])[5]"
    ssd_capacity = "//div[text()='Объем SSD']"
    checkbox_ssd = "//span[@class='checkbox-label' and text()='512 ГБ']"
    drive_type = "//div[text()='Тип привода']"
    checkbox_drive = "//span[@class='checkbox-label' and text()='НЕТ']"
    graphics_controller_type = "//div[text()='Тип графического контроллера']"
    checkbox_dgraphics_controller = "//span[@class='checkbox-label' and text()='Интегрированный']"
    weight = "//div[text()='Вес']"
    kilograms = "//span[@class='checkbox-label' and text()='От 1,5 до 2 кг']"
    show_all_button = "//button[@id='applyFilter']"
    main_word = "//a[@class='bc__item' and text()='Ноутбуки']"


    #Getters
    def get_checkbox_label(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.checkbox_label)))
    def get_ssd_capacity(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.ssd_capacity)))
    def get_checkbox_core(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.checkbox_ssd)))
    def get_drive_type(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.drive_type)))
    def get_checkbox_drive(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.checkbox_drive)))
    def get_graphics_controller_type(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.graphics_controller_type)))
    def get_checkbox_dgraphics_controller(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.checkbox_dgraphics_controller)))
    def get_weight(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.weight)))
    def get_kilograms(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.kilograms)))
    def get_show_all_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.show_all_button)))
    def get_main_word(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.main_word)))


        #Actions
    def click_checkbox_label(self):
        self.get_checkbox_label().click()
        print("Click checkbox label")
    def click_ssd_capacity(self):
        self.get_ssd_capacity().click()
        print("Click ssd capacity")
    def click_checkbox_core(self):
        self.get_checkbox_core().click()
        print("Click checkbox core")
    def click_drive_type(self):
        self.get_drive_type().click()
        print("Click drive type")
    def click_checkbox_drive(self):
        self.get_checkbox_drive().click()
        print("Click checkbox drive")
    def click_graphics_controller_type(self):
        self.get_graphics_controller_type().click()
        print("Click drive type")
    def click_checkbox_dgraphics_controller(self):
        self.get_checkbox_dgraphics_controller().click()
        print("Click checkbox drive")
    def click_weight(self):
        self.get_weight().click()
    def click_kilograms(self):
        self.get_kilograms().click()
        print("Click kilograms")
    def click_show_all_button(self):
        self.get_show_all_button().click()
        print("Click show all button")
    def show_section_titl(self):
        titles = self.get_main_word()
        text = titles.text
        print(f"Раздел выбранного ноутбука: {text}")

        #Methods
    def selection_product(self):
        self.get_current_url()
        self.driver.maximize_window()
        self.click_checkbox_label()
        self.driver.execute_script("window.scrollBy(0, 1000)")
        time.sleep(2)
        self.click_ssd_capacity()
        self.click_checkbox_core()
        self.click_drive_type()
        self.click_checkbox_drive()
        self.click_graphics_controller_type()
        self.click_checkbox_dgraphics_controller()
        self.driver.execute_script("window.scrollBy(0, 500)")
        self.click_weight()
        self.click_kilograms()
        self.click_show_all_button()
        self.assert_word(self.get_main_word(), "Ноутбуки")
        self.show_section_titl()











