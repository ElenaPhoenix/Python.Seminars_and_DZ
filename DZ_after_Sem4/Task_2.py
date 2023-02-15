# В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, причем кусты высажены только по окружности. Таким образом, у
# каждого куста есть ровно два соседних. Всего на грядке растет N кустов. Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них
# выросло различное число ягод – на i-ом кусте выросло ai ягод. В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта 
# система состоит из управляющего модуля и нескольких собирающих модулей. Собирающий модуль за один заход, находясь непосредственно перед некоторым
# кустом, собирает ягоды с этого куста и с двух соседних с ним. Напишите программу для нахождения максимального числа ягод, которое может собрать за 
# один заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.

n = int( input( 'Введите количество кустов на круглой грядке: ' ) )
my_list = [ int(x) for x in input( 'Введите через пробел количество ягод на каждом кусте: ' ).split() ]
n = len(my_list)
my_list = my_list + my_list[:2]                                                 # Прибавляем к списку кустов первую половину списка, чтобы посчитать как по кругу ягоды с соседних кустов
max_berries = 0
for i in range(n):
    max_berries = max( max_berries, my_list[i] + my_list[i+1] + my_list[i+2] )  # Используем max 
print(f'Максимум ягод, который может собрать за 1 заход собирающий модуль: {max_berries}')
