while True:
    try:
        W = input("Введіть знак + - * /: ")
        if W == "Вихід":
            print('Завершення роботи...')
            break
        num = (input("Переше число: "))
        a = int(num)
        num = (input("Друге число: "))
        b = int(num)

        match W:
            case "+":
                c = a + b
                print('Результат: ' + str(c))
            case "-":
                c = a - b
                print('Результат: ' + str(c))
            case "*":
                c = a * b
                print('Результат: ' + str(c))
            case "/":
                try:
                    c = a / b
                    print('Результат: ' + str(c))
                except ZeroDivisionError:
                    print("Помилка: Ділення на нуль!")
            case _:
                print('Помилка!')
    except ValueError:
        print(f"{num}: Помилка: Введене значення не є цілим числом!")