import csv


def readDataFromFile(list):
    with open("topic_06/Book.csv") as file:
        reader = csv.DictReader(file)
        for row in reader:
            list.append(
                {"name": row["StudentName"], "mark": int(row["StudentMark"])})

# ------------------------------


def znch_sort():
    while True:
        m = input("За чим сортувати: ")
        if m != "name" and m != "mark":
            print("Помилка! Спробуй ще раз.")
        else:
            return m


def sort(list, namekey):
    for elem in sorted(list, key=lambda x: x[namekey]):
        print(f"Ім'я = {elem['name']}  Оцінка = {elem["mark"]}")

# ------------------------------


def main():
    list = []
    с = znch_sort()
    readDataFromFile(list)
    sort(list, с)


main()