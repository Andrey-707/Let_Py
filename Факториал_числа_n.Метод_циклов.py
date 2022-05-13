# Факториал_числа_n.Метод_циклов
from rich import print


# Метод циклов while
def factorial(n:int):
    '''Факториал числа методом циклов while'''
    assert n >= 0, "Факториал отрицаельного числа не определен."
    if n == 0:
        return 1

    f = 1
    i = 0

    while i < n:
        i += 1
        f = f * i
    return f

number = int(input("Введите число: ")) # Факториал числа 5 = 120
print("Факориал числа {n} равен {f}".format(n=number, f=factorial(number)))

# Метод циклов for
def factorial(n:int):
    '''Факториал числа методом циклов for'''
    result = 1 # В этой переменной мы будем "накапливать" факториал числа
    for i in range(1, n + 1):
        # каждую итерацию цикла нужно умножать
        # число из последовательности на переменную result
        result = result * i 
    return result

number = int(input("Введите число: ")) # Факториал числа 5 = 120
print("Факориал числа {n} равен {result}".format(n=number, result=factorial(number)))
