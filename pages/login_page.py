from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from base.base_class import Base


class login_page(Base):

    url = "https://e.intant.ru/"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    #Locators
    popup_button = "//a[@class='js-choosecity-close']"
    cookie_button = "//button[@id='reject-cookies']"
    button_authorization = "//a[@class='h__auth js-mw_open']"
    user_mail = "//input[@id='Login']"
    password = "//input[@id='Password']"
    login_button = "//input[@class='btn_emp']"
    name_user_word = "//a[@class='js-dropdown-open' and contains(text(), 'User2')]"


    #Getters
    def get_popup_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.popup_button)))
    def get_cookie_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.cookie_button)))
    def get_button_authorization(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self. button_authorization)))
    def get_user_mail(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.user_mail)))
    def get_password(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.password)))
    def get_login_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.login_button)))
    def get_name_user_word(self):
        return WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, self.name_user_word)))


        #Actions
    def click_popup_button(self):
        self.get_popup_button().click()
        print("Click popup element")
    def click_cookie_button(self):
        self.get_cookie_button().click()
        print("Click cookie button")
    def click_button_authorization(self):
        self.get_button_authorization().click()
        print("Click authorization button")
    def input_user_mail(self, user_mail):
        self.get_user_mail().send_keys(user_mail)
        print("input mail or login")
    def input_password(self, password):
        self.get_password().send_keys(password)
        print("input password")
    def click_login_butoon(self):
        self.get_login_button().click()
        print("Click Login button")
    def show_name_user(self):
        name = self.get_name_user_word()
        name_text = name.text
        print(f"Имя авторизованного пользователь: {name_text}")


        #Methods
    def authorization(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.click_popup_button()
        self.click_cookie_button()
        self.click_button_authorization()
        self.input_user_mail("autotezter@mail.ru")
        self.input_password("autotezter@mail.ru")
        self.click_login_butoon()
        self.assert_word(self.get_name_user_word(), "User2")
        self.show_name_user()










