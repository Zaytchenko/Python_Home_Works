'''
Требуется найти в массиве A[1..N] самый близкий по величине элемент
к заданному числу X. Пользователь в первой строке вводит натуральное 
число N – количество элементов в массиве. В последующих  строках 
записаны N целых чисел Ai. Последняя строка содержит число X

*Пример:*

5
    1 2 3 4 5
    6
    -> 5
    '''
number = int(input('Input natural number: '))
my_list = list(range(1, number))
print(my_list)
x = float(input('Enter the desired number X: '))
i = 0
nearby = my_list[0]
for i in range(number-2):
    if abs(x - my_list[i+1]) < abs(x - my_list[i]):
        nearby = my_list[i+1]
        i+=1
    else:
        i+=1
print(nearby)

    
