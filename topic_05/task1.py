import random


def rund():
    return random.choice(["камінь", "ножиці", "папір"])


def battle(a, b):
    if a == b:
        return "Нічия"
    elif (a == "камінь" and b == "ножиці") or \
         (a == "ножиці" and b == "папір") or \
         (a == "папір" and b == "камінь"):
        return "Ви перемогли"
    else:
        return "Ви програли"


def main():
    while True:
        word = input("Введіть ваше слово: ").lower().strip()
        
        if word == "вихід":
            print("Бувай")
            break

        elif word not in ["камінь", "ножиці", "папір"]:
            print("Помилка!")

        else:
            wrandom = rund()
            print(f"Вибір комп'ютера: {wrandom}")
            r = battle(word, wrandom)
            print(r)
main()