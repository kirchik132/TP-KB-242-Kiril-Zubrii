while True:
    W = input("Введіть знак + - * /: ")
    if W == "Вихід":
        print('Завершення роботи...')
        break
    a = float(input("Переше число: "))
    b = float(input("Друге число: "))

    match W:
        case "+":
            c = a+b
            print('Результат: '+str(c))
        case "-":
            c = a-b
            print('Результат: '+str(c))
        case "*":
            c = a*b
            print('Результат: '+str(c))
        case "/":
            c = a/b
            print('Результат: '+str(c))
        case _:
            print('Помилка!')