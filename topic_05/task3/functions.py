def fun(w, a, b):
    if w == 'exit':
        return 'exit'
    
    match w:
        case "+":
            c = a+b
            return c
        case "-":
            c = a-b
            return c
        case "*":
            c = a*b
            return c
        case "/":
            try:
                c = a/b
                return c
            except ZeroDivisionError:
                return "ZeroDivisionError: Помилка: Ділення на нуль"
        case _:
                return 'Помилка: Невідома операція!'