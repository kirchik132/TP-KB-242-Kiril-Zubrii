while True:
    try:
        W = input("Введіть знак + - * /: ")
        if W == "Вихід":
            print('Завершення роботи...')
            break
        a = int(input("Переше число: "))

        b = int(input("Друге число: "))

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
    except Exception as wr:
        print(wr)