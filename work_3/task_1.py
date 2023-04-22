'''
Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите два варианта решения: через list и через dict.

Пример:
Введите номер месяца: 10
Результат через список: Осень
Результат через словарь: Осень
'''

# Способ с list/

month = int(input("Введите месяц в формате целого числа: "))
season_list = ["winter", "spring", "summer", "autumn"]
month_list = [i for i in range(1, 13)]
if 3 <= month <= 5:
    print(season_list[1])
elif 6 <= month <= 8:
   print(season_list[2])
elif 9 <= month <= 11:
    print(season_list[3])
else:
   print(season_list[0])

'''
# Способ через dict
month = int(input("Введите месяц в формате целого числа: "))
season_dict = {1: 'winter', 2: 'winter', 12: 'winter', 3: 'spring', 4: 'spring', 5: 'spring',
               6: 'summer', 7: 'summer', 8: 'summer', 9: 'autumn', 10: 'autumn', 11: 'autumn'}
print(season_dict.get(month))
'''