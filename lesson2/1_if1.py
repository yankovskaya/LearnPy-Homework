"""
Домашнее задание №1
Условный оператор: Возраст
* Попросить пользователя ввести возраст при помощи input и положить 
  результат в переменную
* Написать функцию, которая по возрасту определит, чем должен заниматься пользователь: 
  учиться в детском саду, школе, ВУЗе или работать
* Вызвать функцию, передав ей возраст пользователя и положить результат 
  работы функции в переменную
* Вывести содержимое переменной на экран
"""



def users_age():
    age = input('Сколько тебе лет?')
    age = int(age)
    if 0 <= age <= 6:
        return 'Tебе пара в детский сад!'
    elif 7 <= age <= 17:
        return 'Ты ходишь в школу!'
    elif 18 <= age <= 22: 
        return 'Ты ходишь в ВУЗ!'
    else: 
        return 'Ты работаешь?'
users_age()


    