a = int(input("a = "))
b = int(input("b = "))
op = input("Доступные операции (+, -, *, /) : ")

if op == "+":
    print(a + b)
elif op == "-":
    print(a - b)
elif op == "*":
    print(a * b)
elif op == "/":
    print(b / a)
else:
    print("Неверная операция")