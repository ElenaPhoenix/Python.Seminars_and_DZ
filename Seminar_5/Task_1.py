# Последовательностью Фибоначчи называется последовательность чисел a0, a1, ..., an, ..., где a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1). Требуется 
# найти N-е число Фибоначчи. Задание необходимо решать через рекурсию

def Fibonacci(n:int):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)

for i in range(int(input('Введите порядковый номер числа Фибоначчи: '))):
    num_fib=Fibonacci(i)
    print(i+1, '-', num_fib)

print(i+1, 'число Фибоначчи - ', num_fib)