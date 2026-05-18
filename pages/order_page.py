from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from base.base_class import Base

class Order_page(Base):



    #Locators
    individual_button = "body > div.site-main > div.main-row.row--blue.adptFix > div.wrapper > div.m-inner.order > div.form-title > div > label:nth-child(1) > span.radio-label"
    courier_button = "//span[@class='radio-label' and text()='Самовывоз']"
    payment_online_button = "//span[@class='radio-label' and text()='Онлайн']"
    payment_QR_button = "//span[@class='radio-label' and text()='QR']"
    field_order_comment = "//textarea[@id='OrderComment']"
    agreement_button = "//input[@id='ConfirmPersonalDataOrder']"


    #Getters
    def get_individual_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.individual_button)))
    def get_courier_button(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.courier_button)))
    def get_payment_online_button(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.payment_online_button)))
    def get_payment_QR_button(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.payment_QR_button)))
    def get_field_order_comment(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.field_order_comment)))
    def get_agreement_button(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.agreement_button)))


    #Actions
    def click_individual_button(self):
        self.get_individual_button().click()
        print("The recipient button has been pressed.")
        time.sleep(2)
    def click_courier_button(self):
        self.get_courier_button().click()
        print("courier button is clicked")
        time.sleep(2)
    def click_payment_online_button(self):
        self.get_payment_online_button().click()
        print("Payment online button is clicked")
    def click_payment_QR_button(self):
        self.get_payment_QR_button().click()
        print("Payment QR button is clicked")
    def click_field_order_comment(self):
        self.get_field_order_comment().click()
        self.get_field_order_comment().send_keys("I want to buy this product as soon as possible.")
        print("Field of the order comment is full")
    def click_agreement_button(self):
        self.get_agreement_button().click()
        print("The agreement has been clicked. Everything is fine. Now click the Place Order button. The test has passed.")


    #Methods
    def fill_out_the_form(self):
        self.click_individual_button()
        self.get_current_url()
        self.click_courier_button()
        self.driver.execute_script("window.scrollBy(0, 500)")
        self.click_payment_online_button()
        self.click_payment_QR_button()
        self.click_field_order_comment()
        self.click_agreement_button()



















