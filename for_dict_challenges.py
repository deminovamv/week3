# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика.
import collections


def name_count(students):
    name_dict = collections.Counter()
    for name in students:
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

def max_name(students):
  max_name =  students[0]
  name_count_max = students.count(max_name)
  for name in students[1:]:
      name_count = students.count(name)
      if name_count > name_count_max:
        max_name = name
        name_count_max = name_count
  return max_name['first_name']





def count_boys_and_girls(name_class):
    girls, boys = [0, 0]
    for name in name_class['students']:
      if is_male.get(name['first_name']):
          boys += 1    
      else:
          girls += 1 
    return  name_class['class'], boys, girls
    

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

print(f'Самое частое имя среди учеников: {max_name(students)}')  



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
for i, school_class in enumerate(school_students):
    print(f'Самое частое имя в классе {i + 1}: {max_name(school_class)}')  


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
max_boys , max_girls = [0,0]
for name_class in school:
    class_name, boys, girls = count_boys_and_girls(name_class)
    if boys > max_boys:
      class_boys = class_name 
    elif girls > max_girls:
      class_girls = class_name

print(f'Больше всего мальчиков в классе {class_boys}')
print(f'Больше всего девочек в классе {class_girls}')


# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a
