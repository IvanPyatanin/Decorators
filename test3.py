from datetime import datetime
import requests


def logger(old_function):
    def new_function(*args, **kwargs):
        name_fuction = old_function.__name__
        date_active = datetime.now().__format__('%H: %M: %S')
        result = requests.get(old_function(*args, **kwargs))

        return result.status_code

    return new_function


@logger
def web_connect():
    url = 'https://netology.ru'
    return url


if web_connect() == 200:
    print("Успех")


if __name__ == '__main__':
    web_connect()