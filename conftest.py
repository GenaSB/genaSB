import pytest
from selenium import webdriver
from pages.login_page import login_page
from pages.cart_page import Cart_page


@pytest.fixture
def driver():
    """Фикстура: создание драйвера, авторизация, очистка корзины"""
    options = webdriver.ChromeOptions()
    options.add_argument("--guest")
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()

    # Авторизация
    login = login_page(driver)
    login.authorization()

    # Очистка корзины перед тестом
    cart = Cart_page(driver)
    cart.clear_cart()

    yield driver


    driver.quit()
