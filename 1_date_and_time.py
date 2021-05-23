"""
Домашнее задание №2
Дата и время
1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime
"""
from datetime import date, timedelta, datetime
import locale

def print_days():
    locale.setlocale(locale.LC_ALL, "russian")
    dt_now = date.today()
    dt_yesterday = dt_now - timedelta(days=1)
    dt_month = dt_now - timedelta(days=30)

    print('Дата сегодня:', dt_now.strftime('%A %d %B %Y'))
    print('Дата вчера:', dt_yesterday.strftime('%A %d %B %Y'))
    print('Дата 30 дней назад:', dt_month.strftime('%A %d %B %Y'))
    

def str_2_datetime(date_string):
    return datetime.strptime(date_string, '%m/%d/%y %H:%M:%S.%f')

if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/20 12:10:03.234567"))