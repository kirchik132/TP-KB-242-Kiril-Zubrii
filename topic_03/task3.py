people = {'name': 'Андрій', 'age': 30, 'sex': 'male'}
print(people)

people.update({'age': 22, 'eyes': 'blue'}) # додавання нових пар ключ-значень
print(people)

del people['name']  # видалення за ключем
print(people)

print(people.keys())  # отримати всі ключі
print(people.values())  # отримати всі значення
print(people.items())  # отримати всі пари ключ-значень

people.clear()
print(people)