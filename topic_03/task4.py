type_list = [5, 4, 6, 8, 11, 90, 3] # Початковий список

type_list.sort() # Сортуємо список
print("Відсортований список:", type_list)

num = int(input('Введіть ваше число: ')) # Запит числа у користувача

def vstavka(type_list, num):
    for i, e in enumerate(type_list):  # Функція шукає позицію для вставки числа num.
        if num <= e:
            return i
    return len(type_list)

pos = vstavka(type_list, num) # Отримання результату
print('Ваша позиція для вставки: ', pos)