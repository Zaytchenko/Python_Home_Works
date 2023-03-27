'''
Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город 
проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.

Пример:
Иван Иванов 1846 года рождения, проживает в городе Москва,
email: jackie@gmail.com, телефон: 01005321456
'''

name = input('Input Name: ') + ', '
surname = input('Input Surname: ') + ', '
birthday = input('Input birthday: ') + ', '
place_of_living = 'place_of_living: ' + input('Input place_of_living: ') + ', '
email = 'email: ' + input('Input email: ') + ', '
phone = 'phone: ' + input('Input phone: ') + ', '
data = lambda name, surname, birthday, place_of_living, email, phone: name + surname + birthday + place_of_living + email + phone
res = data(name, surname, birthday, place_of_living, email, phone)
print(res)
