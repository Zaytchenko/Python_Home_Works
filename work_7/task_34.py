"""
Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку
разобраться в его кричалках не настолько просто, насколько легко он их
придумывает, Вам стоит написать программу. Винни-Пух считает, что ритм
есть, если число слогов (т.е. число гласных букв) в каждой фразе
стихотворения одинаковое. Фраза может состоять из одного слова, если во
фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг
 от друга пробелами. Стихотворение  Винни-Пух вбивает в программу с
 клавиатуры. В ответе напишите “Парам пам-пам”, если с ритмом все в
 порядке и “Пам парам”, если с ритмом все не в порядке

*Пример:*

**Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да
    **Вывод:** Парам пам-пам
"""


def phrase(words):
    return sum(1 for i in words if i in 'аеёиоуыэюя')


c = str(input('Текст, который печатает Винни-Пух: '))
# c = "Хорошо-живет-на-свете-Винни-Пух! От-того-поет-он-эти-песни-вслух!"
# c = "И-не-важно,-чем-он-занят,Если-он-худеть-не-станет,"
st = c.lower().split()
vowel = phrase(st[0])
if all([phrase(i) == vowel for i in st]):
    print('Парам пам-пам')
else:
    print('Пам парам')
