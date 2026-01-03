from operations import dia, num
from functions import function


class Calc:
    def calculator(self, w, a, b):

        if w == '+':
            self.result = function.add(a, b)
        elif w == '-':
            self.result = function.subtract(a, b)
        elif w == '*':
            self.result = function.multiply(a, b)
        elif w == '/':
            self.result = function.divide(a, b)
        else:
            self.result = f"{w} is no such operation"

        return self.result


def readDataFromFile(logfile, list):
    with open(logfile, "r") as file:
        for line in file:
            list.append(line.rstrip())


def saveData(logfile, list):
    with open(logfile, "w") as file:
        for name in list:
            file.write(f"{name}\n")


def main():
    logfile = "topic_07/task2/log_calc.txt"
    loglist = []

    while True:
        w = dia()
        a = num("Перше")
        b = num("Друге")
        c = Calc()
        f = c.calculator(w, a, b)
        print(f"Результат: {f}")

        res = f"{a} {w} {b} = {f}"
        loglist.append(res)
        saveData(logfile, loglist)

        print('--------------------')


main()