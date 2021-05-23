# Вывести последнюю букву в слове
from typing import Counter


word = 'Архангельск'
print(word[-1])

# Вывести количество букв "а" в слове
word = 'Архангельск'
print(word.lower().count('а'))


# Вывести количество гласных букв в слове
word = 'Архангельск'
word = word.lower()
k = 0
for w in word:
    if w in 'ауоыиэяюёе':
        k +=1
print(k)


# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
print(len(sentence.split()))


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
sentence = sentence.split()
for word in sentence:
    print(word[0])

# Вывести усреднённую длину слова.
sentence = 'Мы приехали в гости'
sentence = sentence.split()
length = 0
for word in sentence:
    length += len(word)
print(length/len(sentence))
