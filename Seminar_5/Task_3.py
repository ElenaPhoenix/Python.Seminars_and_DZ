# Напишите функцию, которая принимает одно число и проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое имеет 2 делителя: 1 и n(само число)
n=int(input("Введите натуральное число: "))

def simple_num(x):
    for i in range(2,int(x**0.5)+1):            # Возводим в степень 0,5, чтобы при проверке больших чисел было в 2 раза меньше циклов использовано для проверки
        if x%i==0:
            return 'Число не является простым'
    return 'Число является простым'

print(simple_num(n))