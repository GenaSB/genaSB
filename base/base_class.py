import datetime

class Base:
    def __init__(self, driver):
        self.driver = driver

    """Method get current url"""
    def get_current_url(self):
        get_url = self.driver.current_url
        print("Current URL " + get_url)

        """Method assert word"""
    def assert_word(self, word, result):
        # Проверяем тип: если это веб-элемент, берем текст
        if hasattr(word, 'text'):  # Проверяем есть ли атрибут 'text'
            value_word = word.text
        else:  # Если это уже строка
            value_word = word
        assert value_word == result
        print("Good value word")

    """Method screenshot"""

    def get_screenshot(self, test_name="test"):
        now_date = datetime.datetime.now().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = f'screenshot_{test_name}_{now_date}.png'
        self.driver.save_screenshot(f'C:\\Users\\Генадий\\PycharmProjects\\work_project\\screen\\{name_screenshot}')
        print(f"Скриншот сохранен: {name_screenshot}")

