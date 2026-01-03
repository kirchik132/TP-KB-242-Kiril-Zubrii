import requests

response = requests.get(
    "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchangenew?json")

def funds():
    while True:
        try:
            num = (input("Введіть суму:"))
            sum = float(num)
            return sum
        except ValueError:
            print(f"{num}: не є числом")

def main():

    while True:
        currency = input("Виберіть валюту (EUR, USD, PLN): ").upper()

        if currency == "EXIT":
            break

        elif currency not in ["EUR", "USD", "PLN"]:
            print("Помилка! Спробуйте ще раз!")
            continue

        else:
            for elem in response.json():
                if elem['cc'] == currency:
                    moneyrate = elem['rate']
                    break

        s = funds()
        result = moneyrate*s
        print(f"{s} {currency} = {result} UAH"+"\n --------")

main()