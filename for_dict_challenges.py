# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика.
def name_count(students):
    name_dict = {}
    for name in students:
        if not name['first_name'] in name_dict:
            name_dict[name['first_name']] = 1
        else:
            name_dict[name['first_name']] += 1
    return name_dict


def count_name_dict(name_dict):
    name_count = {}
    for key, value in name_dict.items():
        if name_count.get(value):
            name_count[value] = str(name_count[value]) +' ' + str(key)
        else:
            name_count[value] = key 
    return name_count 

def count_boys_and_girls(name_class):
    girls, boys = [0, 0]
    for k,v in name_class.items():
        if k == 'students':
            for name in v:
             for key, value in name.items():
                if is_male.get(value):
                    boys+=1    
                else:
                    girls+=1 
        else:
            class_name = v 
    return  class_name, boys, girls
    

students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Петя'},
]
name_dict = name_count(students)

for key, value in name_dict.items():
  print("{0}: {1}".format(key,value))

# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2


# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя.
students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Оля'},
]
name_dict = name_count(students)
dict_name_count = count_name_dict(name_dict)
print(f'Самое частое имя среди учеников: {dict_name_count[max(dict_name_count)]}')  



# Пример вывода:
# Самое частое имя среди учеников: Маша

# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
school_students = [
  [  # это – первый класс
    {'first_name': 'Вася'},
    {'first_name': 'Вася'},
  ],
  [  # это – второй класс
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
  ]
]
i = 0
for school_class in school_students:
    i +=1
    name_dict = name_count(school_class)
    dict_name_count = count_name_dict(name_dict)
    print(f'Самое частое имя в классе {i}: {dict_name_count[max(dict_name_count)]}')  


# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша


# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
school = [
  {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
  {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
  'Маша': False,
  'Оля': False,
  'Олег': True,
  'Миша': True,
}

for name_class in school:
    class_name, boys, girls = count_boys_and_girls(name_class)
    print(f'В классе {class_name} {girls} девочки и {boys} мальчика')

# Пример вывода:
# В классе 2a 2 девочки и 0 мальчика.
# В классе 3c 0 девочки и 2 мальчика.


# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков.
school = [
  {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
  {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
  'Маша': False,
  'Оля': False,
  'Олег': True,
  'Миша': True,
}
for name_class in school:
    class_name, boys, girls = count_boys_and_girls(name_class)
    if boys > girls:
        print(f'Больше всего мальчиков в классе {class_name}')
    else:
        print(f'Больше всего девочек в классе {class_name}')


# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a
