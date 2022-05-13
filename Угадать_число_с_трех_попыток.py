# Угадай_рандомное_число_от_1_до_10_с_трех_попыток
from random import randint
from rich import print


# Способ_1.цикл while
print("[bold magenta]Program start[/]")

# сгенерируем рандомное число в заданном диапазоне
number = randint(1, 10)
print("Загаданное число: " + str(number)) # чтобы вывести на экран загаданное число

try_limit = 3 # число попыток
while try_limit > 0:
    # оставшееся число попыток
    print("Осталось попыток: " + str(try_limit))
    # программа просит ввести число с клавиатуры
    n = int(input("Угайдайте загаданное число: "))
    if number < n:
        print("[yellow]Загаданное число меньше.[/]")
    elif number > n:
        print("[cyan]Загаданное число больше.[/]")
    else:
        print("[green]Поздравляем!\nВы угадали![/]")
        # цель достигнута, выход из цикла
        break
    try_limit -= 1
# ОБЯЗАТЕЛЬНО ЧЕРЕЗ ЭЛС.
# Иначе будет: "Поздравляем!\nВы выиграли!" и "Попытки закончились.\nВы проиграли!"
else:
    # число не угадано с трех попыток
    print("[red]Попытки закончились.\nВы проиграли![/]")

print("[bold magenta]Program finish[/]")

print() # пустая строка

# Способ_2.цикл for
print("[bold magenta]Program start[/]")

# сгенерируем рандомное число в заданном диапазоне
number = randint(1, 10)
print("Загаданное число: " + str(number)) # чтобы вывести на экран загаданное число

for i in range(3):
    n = int(input("Угайдайте загаданное число: "))
    if number < n:
        print("[yellow]Загаданное число меньше.[/]")
    elif number > n:
        print("[cyan]Загаданное число больше.[/]")
    else:
        print("[green]Поздравляем!\nВы угадали![/]")
        break
else:
    print("[red]Попытки закончились.\nВы проиграли![/]")

print("[bold magenta]Program finish[/]")