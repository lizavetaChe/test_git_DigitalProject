def helloworld(mode='print'):
    message = "Hello, world!"
    if mode == 'print':
        print(message)
    elif mode == 'return':
        return message
    else:
        print("Неизвестный режим:", mode)

helloworld('print')

user_mode = input("Введите режим (print / return): ")
result = helloworld(user_mode)
if result:
    print("Функция вернула:", result)