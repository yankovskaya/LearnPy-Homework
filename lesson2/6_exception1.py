def hello_user(): 
        while True:
            user_say = input('Что нового?')
            if user_say == 'Пока':
                print('Пока')
                raise KeyboardInterrupt
                break
            else:
                print('Сам ты {}'.format(user_say))
        

hello_user()