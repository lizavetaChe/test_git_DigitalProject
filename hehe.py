import datetime

def helloworld(p):
    if p == 'print':
        print("Привет!")
    elif p == 'time':
        print(f"Текущее время: {datetime.datetime.now().strftime('%H.%M.%S')}")
    elif p == 'date':
        print(f"Текущая дата: {datetime.datetime.today().strftime('%d-%m-%Y')}")
    else:
        print(f"Ошибка: {p}")

helloworld('print')