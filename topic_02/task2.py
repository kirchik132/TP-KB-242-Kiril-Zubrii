W = input("Введіть знак + - * /: ")
a = float(input("Переше число: "))
b = float(input("Друге число: "))

if W == "+":
    c = a+b
    print('Результат: '+str(c))

elif W == "-":
    c = a-b
    print('Результат: '+str(c))

elif W == "*":
    c = a*b
    print('Результат: '+str(c))

elif W == "/":
    c = a/b
    print('Результат: '+str(c))
else:
    print('Помилка!')