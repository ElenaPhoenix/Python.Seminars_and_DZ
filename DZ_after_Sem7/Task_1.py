# Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в его кричалках не на столько просто, насколько легко он их 
# придумывает, Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения 
# одинаковое. Фраза может состоять из 1 слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг от друга пробелами. 
# Стихотворение Винни-Пух вбивает в программу с клавиатуры. В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом 
# все не в порядке.

import os
os.system('cls')

my_list=input(f'Введите через пробел стихи Винни-Пуха: ').lower().split()
print(my_list)
dictionary = {}
vowels = 'ауоыиэяюёе'

for word in my_list:
    count = 0
    for letter in word:
        if letter in vowels:
            count = count + 1
    dictionary[word] = count

print(dictionary)

dict_values = list(dictionary.values())
print(dict_values)
if all([i == dict_values[0] for i in dict_values]):
    print("Парам пам-пам")
else:
    print("Пам парам")