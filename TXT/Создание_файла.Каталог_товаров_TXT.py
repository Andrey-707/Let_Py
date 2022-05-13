# Создание_файла.Каталог_товаров_TXT
from rich import print


catalog = {}

# Каталог из трех товаров (три итерации).
for i in range(3):
    name = input("Введите наименование товара: ")
    count = int(input("Введите количество товара: "))
    # если ключ (наименование товара) уже есть в словаре
    if name in catalog:
        # увеличить его значение на count
        catalog[name] += count
    else:
        # иначе создать ключ со значением count 
        catalog[name] = count

# Каждый ключ и значение в каталоге записать в файл через символ разделитель (двоеточие или др.)            
with open("catalog.txt", "w") as f:
    for i in catalog:
        f.write(i + ": " + str(catalog[i]) + "\n")


# # ############################## OPTIONS ##############################################
# # Программа откроет существующий каталог и дополнит его новыми данными от пользователя.
# catalog = {}

# with open("catalog.txt", "r") as f:
#     # Каждая строка файла должна быть
#     # разбита на две части по двоеточию.
#     # Часть до двоеточия -- наименование. 
#     # После двоеточия -- количество.
#     lines = f.readlines()
#     for line in lines:
#         name, count = line.split(":")
#         catalog[name] = int(count)
#         # print(line) # раскоментировать для просмотра
    
# # Добавить в каталог ЕЩЁ три товара, если они имеют уникальный key или увеличить value старых (три итерации).
# for i in range(3):
#     name = input("Введите наименование товара: ")
#     count = int(input("Введите количество товара: "))
#     # если ключ (наименование товара) уже есть в словаре
#     if name in catalog:
#         # увеличить его значение на count
#         catalog[name] += count
#     else:
#         # иначе создать ключ со значением count 
#         catalog[name] = count

# # Каждый ключ и значение в каталоге записать в файл через символ разделитель (двоеточие или др.)           
# with open("catalog.txt", "w") as f:
#     for i in catalog:
#         f.write(i + ": " + str(catalog[i]) + "\n")

# Чтение файла
with open("catalog.txt", "r") as f:
    print(f.read())
