# Программа шифрования номера телефона абонента
from rich import print


# Способ_1
number = input("Введите номер: ")
simbol = "*"

'''узнаем длину строки пользователя
print(len(number))'''
i = int(len(number))

'''задаем последние четыре видимые цифры'''
a = number[-4:]
print(a)

'''задаем всем цифрам символ *, кроме последних 
четырех'''
b = number[:-4]
print(b)
b = simbol*len(b)
print(b)

if i >= 8 and number.isdigit():
    print(str(b) + str(a))
else:
    print("Ошибка")

print() # пустая строка

# Способ_2
number = input("Введите номер: ")

'''узнаем длину строки пользователя
print(len(number))'''
i = int(len(number))

'''задаем последние четыре видимые цифры'''
a = number[-4:]
print(a)

'''задаем всем цифрам символ *, кроме последних 
четырех'''
stars_count = len(number) - 4
b = "*" * stars_count
print(b)

if i >= 8 and number.isdigit():
    print(str(b) + str(a))
else:
    print("Ошибка")

print() # пустая строка

# Способ_3
number = input("Введите номер: ")
if len(number) >= 8 and number.isdigit():
    stars_count = len(number) - 4
    stars = "*" * stars_count           
    result = stars + number[-4:]
    print(result)
else:
    print("Ошибка")

print() # пустая строка

# Способ_4
number = input("Введите номер: ")
if len(number) >= 8 and number.isdigit():
    print("*" * (len(number) - 4) + number[-4:])
else:
    print("Ошибка")
