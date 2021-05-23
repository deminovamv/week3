"""
Домашнее задание №2
Работа с файлами
1. Скачайте файл по ссылке https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=0
2. Прочитайте содержимое файла в перменную, подсчитайте длинну получившейся строки
3. Подсчитайте количество слов в тексте
4. Замените точки в тексте на восклицательные знаки
5. Сохраните результат в файл referat2.txt
"""

from os import write


def main():
    with open('referat.txt', 'r', encoding ='utf-8') as f:
        i=0
        count_words = 0
        for line in f:
            i += 1
            count_words += len(line.split())
            print(f'Количество символов в {i} строке: {len(line)}')
            line_2 = line.replace('.','!')
            with open('referat2.txt', 'a', encoding ='utf-8') as f_2:
                f_2.write(f'{line_2}')
        print(f'Kоличество слов в тексте: {count_words}')

if __name__ == "__main__":
    main()
