import datetime
import os
from pathlib import Path


class Logger():
    # Динамическое формирование пути к папке logs в корне проекта
    _PROJECT_ROOT = Path(__file__).resolve().parent.parent
    _LOGS_DIR = _PROJECT_ROOT / "logs"
    _LOGS_DIR.mkdir(parents=True, exist_ok=True)

    file_name = str(_LOGS_DIR / f"log_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log")

    @classmethod
    def write_log_to_file(cls, data: str):
        with open(cls.file_name, 'a', encoding='utf-8') as logger_file:
            logger_file.write(data)

    @classmethod
    def add_start_step(cls, method: str):
        test_name = os.environ.get('PYTEST_CURRENT_TEST')

        data_to_add = f"\n-----\n"
        data_to_add += f"Test: {test_name}\n"
        data_to_add += f"Start time: {str(datetime.datetime.now())}\n"
        data_to_add += f"Start name method: {method}\n"
        data_to_add += "\n"

        cls.write_log_to_file(data_to_add)

    @classmethod
    def add_end_step(cls, url: str, method: str):
        data_to_add = f"End time: {str(datetime.datetime.now())}\n"
        data_to_add += f"End name method: {method}\n"
        data_to_add += f"URL: {url}\n"
        data_to_add += f"\n-----\n"

        cls.write_log_to_file(data_to_add)

    @classmethod
    def add_product_step(cls, step_name: str, product_name: str, product_price: str):
        """Логирование товара на каждом этапе"""
        data_to_add = f"Product step: {step_name}\n"
        data_to_add += f"Product name: {product_name}\n"
        data_to_add += f"Product price: {product_price}\n"
        data_to_add += "\n"

        cls.write_log_to_file(data_to_add)

    @classmethod
    def add_assertion_step(cls, check_name: str, expected: str, actual: str, result: bool):
        """Логирование проверок"""
        status = "PASSED" if result else "FAILED"
        data_to_add = f"Assertion: {check_name} - {status}\n"
        data_to_add += f"Expected: {expected}\n"
        data_to_add += f"Actual: {actual}\n"
        data_to_add += "\n"

        cls.write_log_to_file(data_to_add)

    @classmethod
    def add_filter_step(cls, filter_name: str, filter_value: str):
        """Логирование применения фильтров"""
        data_to_add = f"Filter applied: {filter_name} = {filter_value}\n"
        data_to_add += "\n"

        cls.write_log_to_file(data_to_add)

    @classmethod
    def add_cart_step(cls, action: str, product_name: str = None, quantity: int = None):
        """Логирование действий с корзиной"""
        data_to_add = f"Cart action: {action}\n"
        if product_name:
            data_to_add += f"Product: {product_name}\n"
        if quantity:
            data_to_add += f"Quantity: {quantity}\n"
        data_to_add += "\n"

        cls.write_log_to_file(data_to_add)

    @classmethod
    def add_order_step(cls, step_name: str, order_number: str = None, total_price: str = None):
        """Логирование оформления заказа"""
        data_to_add = f"Order step: {step_name}\n"
        if order_number:
            data_to_add += f"Order number: {order_number}\n"
        if total_price:
            data_to_add += f"Total price: {total_price}\n"
        data_to_add += "\n"

        cls.write_log_to_file(data_to_add)