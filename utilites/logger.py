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