# JSON.Каталог_товаров
# Чтобы программа запутилась, в файле catalog.json должны храниться зашифрованные данные,
# например:
# "Стол": 2
# "Стул": 5
# "Кровать": 1
# именно в таком виде, в виде шифра!!!:
# {"\u0421\u0442\u043e\u043b": 2, "\u0421\u0442\u0443\u043b": 5, "\u041a\u0440\u043e\u0432\u0430\u0442\u044c": 1}
import json

from rich import print


print("[bold magenta]Program start[/]")

# Создаем файл каталога (!!! в конце последнего элемента стоит запятая !!!)
catalog = {
    "Стол": 2,
    "Стул": 5,
    "Кровать": 1,
}

# Сохранить в файл 'catalog.json' (файл можно открыть в блокноте)
with open("catalog.json", "w") as file:
    json.dump(catalog, file) # метод .dump() - если нужно json сохранить в файл

# мы можем прочитать все содержимое файла json в переменную и сразу преобразовать с помощью json.loads
with open("catalog.json", "r") as f:
    content = f.read()
    catalog = json.loads(content) # метод .loads() - для загрузки файла
    print(catalog)

for i in range(3):
    name = input("Введите наименование товара: ")
    count = int(input("Введите количество товара: "))
    # если ключ (наименование товара) уже есть в словаре, увеличиваем его значение на count
    if name in catalog:
        catalog[name] += count
    # иначе создаем ключ со значением count 
    else:
        catalog[name] = count

# записываем все строку, полученную с помощью json.dumps в файл
with open("catalog.json", "w") as f:
    content = json.dumps(catalog)
    f.write(content)

# Чтение файла
with open("catalog.json", "r") as f:
    content = f.read()
    catalog = json.loads(content) # метод .loads() - для загрузки файла
    print(catalog)

print("[bold magenta]Program finish[/]")
