'''
Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
'''
#sort()
'''
def my_func(a, b, c):
    my_list = [a, b, c]
    my_list.sort(reverse=True)
    print(my_list)
    sum_of_max = my_list[0] + my_list[1]
    print(sum_of_max)       

my_func(1, 2, 15)
'''
#без функции sort()
def my_func(a, b, c):
    my_list = [a, b, c]
    max_1 = my_list.pop(my_list.index(max(my_list)))
    max_2 = my_list.pop(my_list.index(max(my_list)))
    print(max_1 + max_2)
my_func(1, 2, 15)
