"""
Домашнее задание №2
Работа csv
1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. 
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv
"""
import csv

user_list = [
        {'name': 'Маша', 'age': 25, 'job': 'Scientist'}, 
        {'name': 'Вася', 'age': 8, 'job': 'Programmer'}, 
        {'name': 'Эдуард', 'age': 48, 'job': 'Big boss'},
        {'name': 'Катя', 'age': 29, 'job': 'Scientist'},
        {'name': 'Миша', 'age': 38, 'job': 'Programmer'} 

    ]
def main():
    with open('users.csv', 'w', encoding='utf-8', newline='') as f:
          fields = ['name', 'age', 'job']
          writer = csv.DictWriter(f, fields, delimiter=',')
          writer.writeheader()
          for user in user_list:
              writer.writerow(user)

if __name__ == "__main__":
    main()
