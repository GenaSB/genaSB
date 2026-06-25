import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from base.base_class import Base
from utilites import logger
from utilites.logger import Logger


class Order_page(Base):
    def __init__(self, driver, selected_laptop_name=None, price2=None):  # ← Добавлены параметры
        super().__init__(driver)
        self.selected_item_name = None
        self.selected_laptop_name = selected_laptop_name  # ← Для сравнения названия
        self.price2 = price2  # ← Для сравнения цены





    #     super().__init__(driver)  # ← вызывает родительский класс Base
    #     self.price2 = price2  # ← сохраняет цену в атрибут объекта

    """ Заполнение формы оформления заказа.

        Шаги:
            1. Выбирает получателя "Физическое лицо"
            2. Выбирает способ получения "Самовывоз"
            3. Прокручивает страницу вниз
            4. Выбирает способ оплаты "Онлайн"
            5. Выбирает способ оплаты "QR"
            6. Заполняет поле комментария к заказу
            7. Подтверждает согласие на обработку персональных данных """



    #Locators
    individual_button = "body > div.site-main > div.main-row.row--blue.adptFix > div.wrapper > div.m-inner.order > div.form-title > div > label:nth-child(1) > span.radio-label"
    name_product = "a.s-basket__link"
    price_product = "div.s-basket__total"
    courier_button = "//span[@class='radio-label' and text()='Самовывоз']"
    payment_online_button = "//span[@class='radio-label' and text()='Онлайн']"
    payment_QR_button = "//span[@class='radio-label' and text()='QR']"
    field_order_comment = "//textarea[@id='OrderComment']"
    agreement_button = "//input[@id='ConfirmPersonalDataOrder']"


    #Getters
    def get_individual_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.individual_button)))
    def get_name_product(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.name_product)))
    def get_price_product(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.price_product)))
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
    def click_name_product(self):
        selected_item = self.get_name_product()
        self.selected_item_name = selected_item.text
        print(f"Название товара: {self.selected_item_name}")
    def click_price_product(self):
        sum_price = self.get_price_product()
        self.price = sum_price.text
        print(f"Цена товара: {self.price}")


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
        with allure.step("fill out the form"):
            Logger.add_start_step("fill_out_the_form")
            self.click_individual_button()
            self.get_current_url()
            self.click_name_product()
            self.assert_word(self.selected_laptop_name, self.selected_item_name)  # ← Сравнение названия
            self.click_price_product()
            self.assert_word(self.price, self.price2)  # ← Сравнение цены
            self.click_courier_button()
            self.driver.execute_script("window.scrollBy(0, 500)")
            self.click_payment_online_button()
            self.click_payment_QR_button()
            self.click_field_order_comment()
            self.click_agreement_button()
            # Logger.add_order_step("Order completed", "ORDER-CREATED", self.price2)  # ← Раскомментируйте если нужно
            Logger.add_end_step(self.driver.current_url, "fill_out_the_form")




















