from selenium import webdriver
from pages.cart_page import Cart_page
from pages.order_page import Order_page
from pages.product_page import Product_page
from pages.laptop_selection_page import Laptop_selection_page
from pages.login_page import login_page
from pages.main_page import  Main_page
from pages.product_selection_page import Product_selection_page


def test_buy_product():
    options = webdriver.ChromeOptions()
    options.add_argument("--guest")
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)

    print("Start test")
    login = login_page(driver)
    login.authorization()

    mp = Main_page(driver)
    mp.go_to_catalog()

    psp = Product_selection_page(driver)
    psp.selection_product()

    lsp = Laptop_selection_page(driver)
    lsp.selection_laptop()

    pp = Product_page(driver)
    pp.add_to_cart(lsp.price2, lsp.selected_item_name)

    cp = Cart_page(driver)
    cp.place_an_order()

    op = Order_page(driver)
    op.fill_out_the_form()

