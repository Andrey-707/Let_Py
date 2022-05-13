# Parsing_currency_price.Recursion
# Программа нон-стоп получает данные по курсу USD к рублю через google. Оповещает звуковым сигналом и,
# сообщением если курс опустился или поднялся в интервале времени 10 сек.

# Программа расчитана на число итераций, равное глубине рекурсии (имеет значение по умолчанию 1000).

'''
Увеличить число итераций можно, увеличив глубину рекурсии
import sys
sys.setrecursionlimit(1500)

Можно перехватывать RecursionError

Можно запустить программу в бесконечный цикл while
'''
import requests
import time
import winsound

from datetime import datetime
from threading import Thread
from bs4 import BeautifulSoup
from config import s_path1, s_path2
from rich import print


def get_currency_price():
    '''Получить курс USD, вернуть данные в формате дробного числа'''
    full_page = requests.get(USR_RUB, headers=headers)
    soup = BeautifulSoup(full_page.content, "html.parser")

    # добавить данные к выборке тэгов
    # convert = soup.find_all("span", {"class": "DFlfde"})

    # вывод результата (слишком много тэгов, т.е. слишком много элементов в списке)
    # print(convert)
    '''OUT:
    [<span class="DFlfde eNFL1">1</span>, <span class="DFlfde SwHCTb" data-precision="2" data-value="64.75">64,75</span>]
    '''

    # добавить дополнительные данные к вывобке тэгов, чтобы сузить поиск
    convert = soup.find_all("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})

    # вывод результата (список, состоящий из одного элемента)
    # print(convert)
    '''OUT:
    [<span class="DFlfde SwHCTb" data-precision="2" data-value="64.9375">64,94</span>]
    '''

    # вернуть первый элемент списка через TXT (курса 1 USD в RUB) в формате float
    return float(convert[0].text.replace(",", "."))


def alert_DOWN():
    '''Воспроизвести звуковй сигнал при понижении цены'''
    def music():winsound.PlaySound(s_path1, False)
    Thread(target=music, daemon=True).start()


def alert_UP():
    '''Воспроизвести звуковй сигнал при повышении цены'''
    def music():winsound.PlaySound(s_path2, False)
    Thread(target=music, daemon=True).start()


def check_currency():
    '''Отслеживать курс USD'''
    old_price = get_currency_price() # получить курс 1 USD в RUB в формате float
    # пауза 10 сек
    time.sleep(10)
    new_price = get_currency_price() # получить курс 1 USD в RUB в формате float

    # программа оповещает звуковым сигналом и сообщением при понижении цены USD
    if new_price < old_price:
        now = datetime.now().strftime("%d.%m.%Y %H:%M")
        print(f"[green]Currency price is lower! {now}[/]")
        alert_DOWN()
        print(f"1 USD = {new_price} RUB")
    # программа оповещает звуковым сигналом и сообщением при повышении цены USD
    elif new_price > old_price:
        now = datetime.now().strftime("%d.%m.%Y %H:%M")
        print(f"[red]Currency price is upper! {now}[/]")
        alert_UP()
        print(f"1 USD = {new_price} RUB")
    # иначе выводит текущий курс 1 USD в RUB
    else:
        print(f"1 USD = {new_price} RUB")

    # рекурсия (функция вызывает сама себя)
    check_currency()


# run
if __name__ == "__main__":
    # в google поиске прописать "курс доллара к рублю", копируем URL
    USR_RUB = "https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80%D0%B0+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&newwindow=1&sxsrf=ALiCzsa76uCYIAPYSxAKp81ycSNOv4zYUg%3A1652372969384&ei=6TV9YsiDF9CTwPAPqIGu2AU&ved=0ahUKEwiInIH_sNr3AhXQCRAIHaiAC1sQ4dUDCA4&uact=5&oq=%D0%BA%D1%83%D1%80%D1%81+%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80%D0%B0+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&gs_lcp=Cgdnd3Mtd2l6EAMyEAgAEIAEELEDEIMBEEYQggIyCAgAEIAEELEDMggIABCABBCxAzIKCAAQgAQQhwIQFDIICAAQgAQQsQMyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDoECCMQJzoQCAAQgAQQhwIQsQMQgwEQFDoLCAAQgAQQsQMQgwE6BAgAEEM6CggAELEDEIMBEEM6BwgAELEDEEM6DQgAEIAEEIcCELEDEBQ6CAgAELEDEIMBOgsIABCABBCxAxDJA0oECEEYAEoECEYYAFAAWN4nYOopaABwAXgAgAGUAYgB6QmSAQQxOS4xmAEAoAEBwAEB&sclient=gws-wiz"
   
    # в google поиске прописать "my user agent", копируем строку с результатом
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36"}

    # стартовое значение времени
    now = datetime.now().strftime("%d.%m.%Y %H:%M")
    print(f"[yellow]Start {now}[/]")

    # стартовое значение курса
    print(f"1 USD = {get_currency_price()} RUB")

    # запуск рекурсии
    check_currency()
