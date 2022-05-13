# CSV.Каталог_товаров
import csv

from rich import print


print("[bold magenta]Program start[/]")

catalog = {}

# создать файл из программы
with open("catalog.csv", "w", newline="") as f: # newline="" выключает создание пустой строки
    # получаем объект для записи в файл
    writer = csv.writer(f)
    row = ["Яблоки", "6"]
    # и с его помощью записываем информацию в файл
    writer.writerow(row)

# читаем файл csv построчно и сразу распаковываем каждую строку в две переменных
# чтобы прочитать файл, он должен быть создан вручную (как пустой текстовый документ в формате .csv)
# или из программы 
with open("catalog.csv", "r") as f:
    for name, count in csv.reader(f):
        catalog[name] = int(count)

# Три итерации. Добавляем количество или создаем товар если такого нет и добавляем его количество
# В input() прописал яблоки - 2, груши - 3, бананы - 11
for i in range(3):
    name = input("Введите наименование товара: ")
    count = int(input("Введите количество товара: "))
    # если ключ (наименование товара) уже есть в словаре, то увеличиваем его значение на count
    if name in catalog:
        catalog[name] += count
    # иначе создаем ключ со значением count
    else:
        catalog[name] = count

# Каждый ключ и значение в каталоге нужно записать в файл. Метод словаря .items() возвращает
# пару ключ-значение в виде кортежа, а это как раз подходит нам для записи строки csv
with open("catalog.csv", "w", newline="") as f:
    writer = csv.writer(f)
    for row in catalog.items():
        writer.writerow(row)

# Чтение данных из CSV файла
with open("catalog.csv", "r") as f:
    # print(f.read()) # целиковое чтение файла и вывод в терминал
    # print(list(csv.reader(f))) # вывод данных в виде списка списков
    rows = csv.reader(f)
    for row in rows:
        print(row) # каждая строка является списком по типу данных <class 'list'>

print("[bold magenta]Program finish[/]")
