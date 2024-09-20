"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""
from datetime import datetime, timedelta
import locale
locale.setlocale(locale.LC_ALL, "ru_RU.UTF8")


def print_days():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    date_now = datetime.now()
    date_yesterday = date_now - timedelta(days=1)
    date_30_days_ago = date_now - timedelta(days=30)
    
    print(f"Дата вчера: {date_yesterday.strftime('%A%d-%B-%Y')}\nДата сегодня: {date_now.strftime('%A:%d-%B-%Y')}\nДата 30 дней назад: {date_30_days_ago.strftime('%A:%d-%B-%Y')} ")


def str_2_datetime(date_string):
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
   
    return datetime.strptime(date_string, '%m/%d/%Y %H:%M:%S.%f')
    

if __name__ == "__main__":
    print_days()
    print(str_2_datetime('01/01/2020 12:10:03.234567'))
