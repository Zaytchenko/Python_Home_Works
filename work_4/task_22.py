'''
Даны два неупорядоченных набора целых чисел (может быть, с 
повторениями). Выдать без повторений в порядке возрастания все те 
числа, которые встречаются в обоих наборах.
Пользователь вводит 2 числа. n - кол-во элементов первого множества. 
m - кол-во элементов второго множества. Затем пользователь вводит 
сами элементы множеств.
'''
number_a = int(input('Input the number of elements of the first array: '))
number_b = int(input('Input the number of elements of the second array: '))
a = [int(input()) for i in range (number_a)]
b = [int(input()) for i in range (number_b)]

print('Entery arrays:')
print(a) 
print(b)
matching_numbers = set(a) & set(b)
matching_numbers_list = sorted(list(matching_numbers))
print(f'matching numbers:', matching_numbers_list)