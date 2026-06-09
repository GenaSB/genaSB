# from selenium import webdriver
# from pages.cart_page import Cart_page
# from pages.order_page import Order_page
# from pages.product_page import Product_page
# from pages.laptop_selection_page import Laptop_selection_page
# from pages.login_page import login_page
# from pages.main_page import Main_page
# from pages.product_selection_page import Product_selection_page
# from base.base_class import Base
# from utilites.logger import Logger
#
#
# def test_buy_product():
#     options = webdriver.ChromeOptions()
#     options.add_argument("--guest")
#     options.add_experimental_option("detach", True)
#     driver = webdriver.Chrome(options=options)
#     base = Base(driver)
#
#     try:
#         print("Start test")
#         login = login_page(driver)
#         login.authorization()    # авторизация на главной странице
#
#         mp = Main_page(driver)
#         mp.go_to_catalog()       # выбор наименования товаров в каталоге
#
#         psp = Product_selection_page(driver)
#         psp.selection_product()  # выбор параметров искомого товара через фильтры
#
#         lsp = Laptop_selection_page(driver)
#         lsp.selection_laptop()   # выбор товара и проверка названия с ценой
#
#         pp = Product_page(driver)
#         pp.add_to_cart(lsp.price2, lsp.selected_item_name)  # добавление товара в корзину и проверка данных
#
#         cp = Cart_page(driver)
#         cp.place_an_order()      # переход к оформлению заказа
#
#         op = Order_page(driver)
#         op.fill_out_the_form()   # оформление заказа
#
#     except Exception as e:
#         print(f"Тест упал: {e}")
#         base.get_screenshot("test_buy_product")
#         raise


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


def test_buy_product():
    options = webdriver.ChromeOptions()
    options.add_argument("--guest")
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)
    base = Base(driver)

    try:
        print("Start test")

        Logger.add_start_step("authorization")
        login = login_page(driver)
        login.authorization()  # авторизация на главной странице
        Logger.add_end_step(driver.current_url, "authorization")

        Logger.add_start_step("go_to_catalog")
        mp = Main_page(driver)
        mp.go_to_catalog()  # выбор наименования товаров в каталоге
        Logger.add_end_step(driver.current_url, "go_to_catalog")

        Logger.add_start_step("selection_product")
        psp = Product_selection_page(driver)
        psp.selection_product()  # выбор параметров искомого товара через фильтры
        Logger.add_end_step(driver.current_url, "selection_product")

        Logger.add_start_step("selection_laptop")
        lsp = Laptop_selection_page(driver)
        lsp.selection_laptop()  # выбор товара и проверка названия с ценой
        Logger.add_product_step("Selected laptop", lsp.selected_item_name, lsp.price2)
        Logger.add_end_step(driver.current_url, "selection_laptop")

        Logger.add_start_step("add_to_cart")
        pp = Product_page(driver)
        pp.add_to_cart(lsp.price2, lsp.selected_item_name)  # добавление товара в корзину и проверка данных
        Logger.add_cart_step("add to cart", lsp.selected_item_name, 1)
        Logger.add_end_step(driver.current_url, "add_to_cart")

        Logger.add_start_step("place_an_order")
        cp = Cart_page(driver)
        cp.place_an_order()  # переход к оформлению заказа
        Logger.add_end_step(driver.current_url, "place_an_order")

        Logger.add_start_step("fill_out_the_form")
        op = Order_page(driver)
        op.fill_out_the_form()  # оформление заказа
        Logger.add_order_step("Order completed", "ORDER-CREATED", lsp.price2)
        Logger.add_end_step(driver.current_url, "fill_out_the_form")

    except Exception as e:
        print(f"Тест упал: {e}")
        base.get_screenshot("test_buy_product")
        Logger.add_error_log(str(e), "test_buy_product_screenshot.png")
        raise