"""
Домашнее задание №1
Цикл while: ask_user со словарём
* Создайте словарь типа "вопрос": "ответ", например:
  {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"} и так далее
* Напишите функцию ask_user() которая с помощью функции input()
  просит пользователя ввести вопрос, а затем, если вопрос есть
  в словаре, программа давала ему соотвествующий ответ. Например:
    Пользователь: Что делаешь?
    Программа: Программирую
    
"""

questions = {"Как дела?": "Хорошо!", "Что делаешь?": "Программирую", "Что будешь делать завтра?": "Программировать!"}

def ask_user():
    answer = questions.get('question')
    while True:
        users_question = input("Задай вопрос!")
        if users_question == "Как дела?":
            print("Хорошо!")
        elif users_question == "Что делаешь?":
            print("Программирую")
        elif users_question == "Что будешь делать завтра?":
            print("Программировать!")
        else: 
            print("Задай другой вопрос!")

if __name__ == "__main__":
    ask_user()