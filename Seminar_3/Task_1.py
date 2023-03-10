# Список уникальных элементов можно получить через множества.
my_list=[2, 3, 5, 7, 4, 3, 5, 3, 2, 45, 6, 3, 12, 5, 7, 4, 5]
new_set=set(my_list)                # пространство
new_list=list(set(my_list))         # list - упорядоченный список
new_tuple=tuple(set(my_list))       # Кортеж - неизменяемый тип данных, более безопасный, быстрее работает (требует меньше ресурсов)
cur_tuple=new_tuple[:-3]
new_tuple=cur_tuple

print(*my_list)
print(*my_list, sep=' ', end='\n')
print(*my_list, sep='@', end='-')   # *- распаковывает все элементы списка в строку, sep - разделитель между элементами принта, end - конец строки
print(new_set)
print(*my_list, sep='\n') # печать каждого элемента с новой строки