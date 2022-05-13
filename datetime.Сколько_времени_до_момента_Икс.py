# timedelta. Сколько времени до момента "Икс"
import datetime

from rich import print


def choose_plural(amount, variants):
    '''Функция выбора формы существительного'''
    if amount % 10 == 1 and amount % 100 != 11:
        variant = 0
    elif amount % 10 >= 2 and amount % 10 <= 4 and \
            (amount % 100 < 10 or amount % 100 >= 20):
        variant = 1
    else:
        variant = 2
    return "{} {}".format(amount, variants[variant])


print("[bold magenta]Program start[/]")

try:
    # Получаем и преобразуем нужные данные от пользователя
    datetime_str = input("Введите дату и время момента 'Икс' в формате ДД.ММ.ГГГГ ЧЧ:ММ\n")
    date_x = datetime.datetime.strptime(datetime_str,"%d.%m.%Y %H:%M")
    date_now = datetime.datetime.now().replace(second=0, microsecond=0)

    # Программа должна начать выполнять эту часть кода если дата момента "Икс" больше текущей даты
    if date_x > date_now:
        delta = date_x - date_now

        # Получаем количество дней, часов и минут, оставшихся до момента "Икс"
        days = delta.days
        hours = delta.seconds // 3600
        minutes = (delta.seconds - hours * 3600) // 60
        
        result = ""

        # Нужная строка формируется согласно условию задачи
        if days > 0:
            result = choose_plural(days, ("день", "дня", "дней"))
            if hours > 0:
                result += " и " + choose_plural(hours, (" час", "часа", "часов"))
        elif hours > 0:
            result = choose_plural(hours, ("час", "часа", "часов"))
            if minutes > 0:
                result += " и " + choose_plural(minutes, ("минута", "минуты", "минут"))
        else:
            result = choose_plural(minutes, ("минута", "минуты", "минут"))
        print(f"[bold green]До момента 'Икс' {result}[/]")
    else:
        print("[bold red]Момент 'Икс' уже прошел.[/]")
# Если пользователь введет дату не по формату, отработает этот обработчик исключения
except ValueError:
    print("[bold red]Ошибка! Введите дату по указанному формату.[/]")

print("[bold magenta]Program finish[/]")
