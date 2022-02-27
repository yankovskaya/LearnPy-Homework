"""
Домашнее задание №1
Условный оператор: Сравнение строк
* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты
"""


def strings(first, second):

    if not isinstance(first, str) or not isinstance(second, str):
      return 0
    if first == second:
      return 1
    if len(first) > len(second):
      return 2
    if second == 'learn':
      return 3

strings('meow', 'meow')

strings(1, 2)

strings('meow', 'meow')

strings('meow', 'meoow')

strings('meow', 'learn')

strings('meoow', 'meow')

strings(2, 'meow')




