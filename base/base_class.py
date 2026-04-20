

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

