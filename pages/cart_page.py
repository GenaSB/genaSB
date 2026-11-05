import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from base.base_class import Base
from utilites import logger
from utilites.logger import Logger


class Cart_page(Base):

    """ Страница корзины с товаром, переход на страницу оформления заказа

    Шаги:
        1. открывает текущую страницу
        2. нажимает на кнопку "Оформить заказ
        3. переходит на страницу оформления заказа
        4. выводит заголовок страницы """



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
        with allure.step("place an order"):
            Logger.add_start_step("place_an_order")
            self.get_current_url()
            self.driver.maximize_window()
            self.click_order_button()
            self.click_page_name()
            Logger.add_end_step(self.driver.current_url, "place_an_order")

    def clear_cart(self):
        """Очистка корзины перед тестом"""
        with allure.step("clear cart"):
            Logger.add_start_step("clear_cart")
            self.driver.get("https://e.intant.ru/basket/")

            # Проверяем, есть ли кнопка очистки корзины
            clear_buttons = self.driver.find_elements(By.CSS_SELECTOR, "a.js-clear-basket")

            if clear_buttons:
                print(f"Корзина не пуста. Найдено кнопок очистки: {len(clear_buttons)}")
                clear_buttons[0].click()

                # Ждём alert «Вы уверены?» и принимаем
                try:
                    alert = WebDriverWait(self.driver, 5).until(EC.alert_is_present())
                    print(f"Alert: {alert.text}")
                    alert.accept()
                    print("Alert принят")
                    self.driver.refresh()  # ← обновить страницу
                    time.sleep(1)  # ← дать загрузиться
                except Exception as e:
                    print(f"Alert не появился: {e}")
            else:
                print("Корзина уже пуста — очистка не требуется")

            Logger.add_end_step(self.driver.current_url, "clear_cart")



















