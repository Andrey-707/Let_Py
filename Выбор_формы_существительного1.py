# Выбор_формы_существительного.
'''
Написать функцию для выбора правильной формы существительного в зависимости от переданного
количества. Функция должна называться choose_plural и принимать два параметра. Первый
параметр — это количество. Второй — это кортеж из трех вариантов склонения существительного.
Этот кортеж легко составить по мнемоническому правилу: один, два, пять. Например, для
слова «банан» это будет: банан, банана, бананов.

Эта функция должна возвращать подходящее существительное, склеенное с переданным
количеством. То есть, такой код:

result_1 = choose_plural(23, ("копейка", "копейки", "копеек"))
print(result_1)
result_2 = choose_plural(7, ("рубль", "рубля", "рублей"))
print(result_2)
result_3 = choose_plural(51, ("цент", "цента", "центов"))
print(result_3)

вывод на экран:

23 копейки
7 рублей
51 цент
'''
from rich import print


def choose_plural(amount, variants):
    if amount % 10 == 1 and amount % 100 != 11:
        variant = 0
    elif amount % 10 >= 2 and amount % 10 <= 4 and \
            (amount % 100 < 10 or amount % 100 >= 20):
        variant = 1
    else:
        variant = 2
    return "{} {}".format(amount, variants[variant])


print("[bold magenta]Program start[/]")

result_1 = choose_plural(23, ("копейка", "копейки", "копеек"))
print(result_1)

result_2 = choose_plural(7, ("рубль", "рубля", "рублей"))
print(result_2)

result_3 = choose_plural(51, ("цент", "цента", "центов"))
print(result_3)

print("[bold magenta]Program finish[/]")
