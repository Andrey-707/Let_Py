from rich import print

# LP_Parsing
# Получение информации (данных) с сайтов называют «парсингом» (от англ. parse).

'''
Написать программу, которая «распарсит» нашу простую, тренировочную страницу
https://letpy.com/simple-html-example/

«Добыть» нужно случайное число, которое отображается на странице. То есть из всего
текста страницы нужно оставить только число и вывести его на экран. Для этого можно
использовать методы строк, срезы, циклы — в общем все, что вы проходили до этого.
'''


# #################################################################################################
# Первый способ. Библиотека requests.
# import requests


# print("[bold magenta]Program start[/]")

# # Запрос к странице с заданием
# result = requests.get("https://letpy.com/simple-html-example/")

# # если вывести данные на экран result.text (они будут в формате HTML), то
# # мы увидиим, что число "зажато" между двумя строками <strong> и </strong>
# # print(result.text) # для просмотра раскомментировать

# # заменим </strong> на <strong>, чтобы по этой подстроке разбить текст на части
# text = result.text.replace("</strong>", "<strong>")

# # Вывод в формате HTML
# # print(text) # для просмотра раскомментировать

# # разбиваем строку на части
# parts = text.split("<strong>")

# # Вывод в виде списка. Список состоит из пяти (len(parts)) элементов.
# # print(parts) # для просмотра раскомментировать

# # Нас интересует число, это четвертый элемент списка.
# print(f"Случайное число: {parts[3]}")

# print("[bold magenta]Program finish[/]")


# ######################################################################################################
# # Второй способ. Библиотека bs4.
# # Так же подходит если не нужно делать запрос через requests.get() и данные хранятся в виде HTML на ПК
# import requests

# from bs4 import BeautifulSoup


# print("[bold magenta]Program start[/]")

# # запрос к странице с заданием
# result = requests.get("https://letpy.com/simple-html-example/")

# # создаем файл, записываем в него текстовые данные
# with open ("LP_Parsing.txt", "w") as file:
# 	file.write(result.text)

# # открываем текстовый файл на чтение
# with open ("LP_Parsing.txt") as file:
#     result = file.read() # в переменную 'result' сохраняем данные

# # скармливаем данные библиотеке BeautifulSoup
# soup = BeautifulSoup(data, "html.parser")

# # Вывод в формате HTML
# # print(soup) # для просмотра раскомментировать

# # Вывод в формате TXT
# # print(soup.text) # для просмотра раскомментировать

# # с помощью метода .find_all() находим содержимое ВСЕХ тегов "strong". Данные сохраняются в виде списка.
# page_strongs = soup.find_all("strong")

# # выводим на печать содержимое ВСЕХ тегов "strong", один тэг - элемент списка.
# # print(page_strongs) # для просмотра раскомментировать

# # т.к. page_strongs является списком, можем обращаться к его элементам по индексу
# # Вывод в формате HTML
# # print(page_strongs[1]) # для просмотра раскомментировать

# # Вывод в формате TXT
# print(f"Случайное число: {page_strongs[1].text}")

# print("[bold magenta]Program finish[/]")


######################################################################################################
# Третий способ. Библиотека bs4. Аналогичен предыдущему, но БЕЗ создания текстового файла.
import requests

from bs4 import BeautifulSoup


print("[bold magenta]Program start[/]")

# запрос к странице с заданием
result = requests.get("https://letpy.com/simple-html-example/")

# скармливаем данные библиотеке BeautifulSoup
soup = BeautifulSoup(result.text, "html.parser")

# Вывод в формате HTML
# print(soup) # для просмотра раскомментировать

# Вывод в формате TXT
# print(soup.text) # для просмотра раскомментировать

# с помощью метода .find_all() находим содержимое ВСЕХ тегов "strong". Данные сохраняются в виде списка.
page_strongs = soup.find_all("strong")

# выводим на печать содержимое ВСЕХ тегов "strong", один тэг - элемент списка.
# print(page_strongs) # для просмотра раскомментировать

# т.к. page_strongs является списком, можем обращаться к его элементам по индексу
# Вывод в формате HTML
# print(page_strongs[1]) # для просмотра раскомментировать

# Вывод в формате TXT
print(f"Случайное число: {page_strongs[1].text}")

print("[bold magenta]Program finish[/]")
