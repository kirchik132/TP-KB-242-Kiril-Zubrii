from operations import dia, num
from functions import fun


def readDataFromFile(logfile, list):
    with open(logfile, "r") as file:
        for line in file:
            list.append(line.rstrip())


def saveData(logfile, list):
    with open(logfile, "w") as file:
        for name in list:
            file.write(f"{name}\n")


def main():
    logfile = "topic_06/task1/log_calc.txt"
    loglist = []

    while True:
        w = dia()
        a = num("Перше")
        b = num("Друге")
        f = fun(w, a, b)

        res = f"{a} {w} {b} = {f}"
        loglist.append(res)
        saveData(logfile, loglist)

        print(f"Результат: {f}")
        print('--------------------')


main()