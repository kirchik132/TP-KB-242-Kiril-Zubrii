class function:

    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b

    @staticmethod
    def multiply(a, b):
        return a * b

    @staticmethod
    def divide(a, b):

        if b == 0:

            return "ZeroDivisionError: Помилка: Ділення на нуль"
        return a / b