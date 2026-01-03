class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Ім'я відсутнє")
        self._name = name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        try:
            number = int(value)
        except ValueError:
            raise ValueError("Це не число")

        if number < 0 or number > 110:
            raise ValueError("Помилка! Вік має бути від 0 до 110 років")
        self._age = number

    def __str__(self):
        return f"Студент: {self.name}, Вік: {self.age}"

# ------------------------------------------------------------------


def get_student_list():
    students = []

    while True:
        name = input("Введіть ім'я: ")
        if name == 'ex':
            break
        age = (input("Введіть вік: "))
        print("------------------")

        slovnuk = Student(name, age)
        students.append(slovnuk)

    return students
# ------------------------------------------------------------------


def znch_sort():
    while True:
        m = input("За чим сортувати (ім'я/вік): ")
        if m != "name" and m != "age":
            print("Помилка! Спробуйте ще раз.")
        else:
            return m


def sort(listochek, namekey):
    for elem in sorted(listochek, key=lambda x: getattr(x, namekey)):
        print(elem)

# ------------------------------------------------------------------


def main():

    spusok = get_student_list()
    c = znch_sort()
    print("------------------")
    sort(spusok, c)


main()