'''
Требуется вычислить, сколько раз встречается некоторое число X
в массиве A[1..N]. Пользователь в первой строке вводит натуральное 
число N – количество элементов в массиве. В последующих  строках
записаны N целых чисел Ai. Последняя строка содержит число X

*Пример:*

5
    1 2 3 4 5
    3
    -> 1
'''
number = int(input('Input natural number: '))
my_list = list(range(number))
print(my_list)
x = int(input('Enter the desired number X: '))
print(my_list.count(x))