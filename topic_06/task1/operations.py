def dia():
    w = input("Операція (+, -, *, /): ")
    if w == "ex":
        return 'exit'
    else:
        return w


def num(nomer):
    while True:
        try:
            num = (input(f"{nomer} num: "))
            n = float(num)
            return n
        except ValueError:
            print(f"Помилка: '{num}' - не число")