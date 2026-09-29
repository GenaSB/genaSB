import allure
from selenium import webdriver
from pages.cart_page import Cart_page
from pages.order_page import Order_page
from pages.product_page import Product_page
from pages.laptop_selection_page import Laptop_selection_page
from pages.login_page import login_page
from pages.main_page import Main_page
from pages.product_selection_page import Product_selection_page
from base.base_class import Base
from utilites.logger import Logger

@allure.description("Test buy product")
def test_buy_product():
    options = webdriver.ChromeOptions()
    options.add_argument("--guest")
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)
    base = Base(driver)

    # try:
    print("Start test")

    login = login_page(driver)
    login.authorization()  # авторизация на главной странице



    mp = Main_page(driver)
    mp.go_to_catalog()  # выбор наименования товаров в каталоге



    psp = Product_selection_page(driver)
    psp.selection_product()  # выбор параметров искомого товара через фильтры



    lsp = Laptop_selection_page(driver)
    lsp.selection_laptop()  # выбор товара и проверка названия с ценой



    pp = Product_page(driver)
    pp.add_to_cart(lsp.price2, lsp.selected_item_name)  # добавление товара в корзину и проверка данных



    cp = Cart_page(driver)
    cp.place_an_order()  # переход к оформлению заказа

    op = Order_page(driver, lsp.selected_laptop_name, lsp.price2)
    op.fill_out_the_form()  # оформление заказа


    # except Exception as e:
    #     print(f"Тест упал: {e}")
    #     base.get_screenshot("test_buy_product")
    #     Logger.add_error_log(str(e), "test_buy_product_screenshot.png")
    #     raise