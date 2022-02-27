
def hello_user():
     while True:
        user_say = input('Что нового?')
        print('Сам ты {}'.format(user_say))
        try:
            if user_say == 'Пока':
                print('Пока') 
                break
        except KeyboardInterrupt:
            print('Ошибка') 

if __name__ == '__main__':
    print(hello_user())