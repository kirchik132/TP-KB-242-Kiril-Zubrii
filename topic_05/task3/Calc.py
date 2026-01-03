from operations import dia, num
from functions import fun

while True:
    w = dia()
    
    if w == 'exit':
        print("Вихід з програми...")
        break
    
    a = num("Перше")
    b = num("Друге")

    f = fun(w, a, b)

    print(f"Результат: {f}")
    print('--------------------')