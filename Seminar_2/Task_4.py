#Иван Васильевич пришел на рынок и решил купить 2 арбуза: один для себя, а другой для тещи. Для себя нужно выбрать арбуз потяжелей, а для тещи полегче. Арбузов слишком много и он не знает: 
#как выбрать самый легкий и самый тяжелый арбуз. 
#Пользователь вводит число n - количество арбузов. Вторая строка содержит n чисел, записанных на новой строке каждое. Здесь каждое число - масса соответствующего арбуза.
#Input: 5 -> 5 1 6 5 9
#Output: 1 9
import os
os.system('cls')                                        #Самоочистка терминала
import random
n=int(input('Введите количество арбузов: \n'))
numb=random.randint(1,9)
print(f'1 арбуз весит {numb} кг.')
min1= numb
max1=numb
for i in range(2, n+1):
    numb=random.randint(1,9)
    print(f'{i} арбуз весит {numb} кг.')
    if numb>max1:
        max1=numb
    elif numb<min1:
        min1=numb
print(f'\n Самый легкий арбуз весит {min1} кг, самый тяжелый арбуз весит {max1} кг')