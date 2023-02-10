import requests
from datetime import datetime


def get_duration(some_time):
    """
    Функция вычисляет разность во времени, возвращает значение в минутах
    :param some_time: datetime
    :return: datetime
    """
    duration = datetime.now() - some_time
    duration_in_s = duration.total_seconds()
    minutes = divmod(duration_in_s, 60)[0]
    return minutes


def get_price():
    """
    Функция обращается к API Binance, в реальном времени получает цену фьючерса XRP/USDT и сравнивает
    с максимальной ценой за последний час
    :return:
    """
    start_time = datetime.now()  # время начала работы скрипта
    values_price = set()  # множество с уникальными значениями цены фьючерса XRP/USDT
    print(start_time)
    while True:
        response = requests.get("https://fapi.binance.com/fapi/v1/ticker/24hr", params={'symbol': 'XRPUSDT'})
        current_price = float(response.json()["lastPrice"])  # цена фьючерса XRP/USDT
        values_price.add(current_price)

        if get_duration(start_time) == 60.0:
            if current_price < max(values_price) * 0.99:
                print('Цена фьючерса XRP/USDT упала на 1% от максимальной цены за последний час')

            start_time = datetime.now()
            values_price.clear()


def main():
    get_price()


if __name__ == '__main__':
    main()
