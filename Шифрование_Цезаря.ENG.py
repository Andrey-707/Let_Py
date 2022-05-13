# Шифрование_Цезаря.ENG
'''
Написать программу с функцией encrypt. Эта функция должна принимать два аргумента —
исходную строку s и ключ k.

Функция encrypt должна шифровать исходную строку s c ключом k. При этом, шифруются только
символы, которые есть в алфавите. Знаки препинания, пробелы и другие символы функция
должна оставлять «как есть». Исходная строка должна быть преобразована к верхнему регистру.
То есть, в результате шифрования строки Hello world! с k=5 должно получится MJQQT WORLD!.
Ключ шифрования может быть каким угодно большим числом.

Все, что нужно для решения этой задачи вы уже знаете, но небольшая подсказка не помешает
используйте остаток от деления и строку, содержащую алфавит.

letters = "ABCDEFGHIJKLMNOPQRSTWXYZ"
При отрицательном значении аргумента k функция должна сдвигать символы не вправо, а влево.
Не забудьте проверить это.

Если все сделано правильно, то при таком использовании encrypt

message = "Привет world!"
encrypted_message = encrypt(message, 5)
decrypted_message = encrypt(encrypted_message, -5)
print(encrypted_message)
print(decrypted_message)

На экран должно быть выведено:
HELLO WORLD!
MJQQT WORLD!

То есть, первый вызов encrypt шифрует строку, а второй, с «минус» k расшифровывает.
'''
from rich import print


# Вариант решения с использованием цикла по всей строке для шифрования
def encrypt1(message, k):
    letters = "ABCDEFGHIJKLMNOPQRSTWXYZ"
    message = message.upper()
    result = ''
    for i in message:
        index = letters.find(i)
        if index != -1:
            # остаток от деления тут используется для того, 
            # чтобы не было выхода за пределы строки letters
            # и не возникала ошибка IndexError
            result += letters[(index + k) % len(letters)]
        else:
            result += i
    return result.capitalize() # методом .capitalize() возвращаем слово с большей буквы


# применяем шифрование
word = 'Root'
print(f"Зашифнуем слово '{word}', ключ шифрования равен 3")
en_word = encrypt1(word, 3)
print(f"Зашифрованное слово '{en_word}'")
un_en_word = encrypt1(en_word, -3)
print(f"Расшифрованное слово '{un_en_word}'")


# Вариант решения с использованием метода строк translate()
def encrypt2(message, k):
    letters = "ABCDEFGHIJKLMNOPQRSTWXYZ"
    message = str(message).upper()
    # в этой строке мы создаем сдвинутый на значение k алфавит
    # то есть, например, при ключе 3 алфавиту
    # ABCDEFGHIJKLMNOPQRSTWXYZ
    # будет соответствовать
    # DEFGHIJKLMNOPQRSTWXYZABC
    letters_tmp = letters[k % 24:] + letters[0:k % 24]
    # создание таблицы переводов для строки. Каждой
    # букве letters будет соответствовать буква из letters_tmp
    transtab = str.maketrans(letters, letters_tmp)
    # метод translate заменит все символы в строке согласно
    # таблице переводов transtab
    return message.translate(transtab).capitalize() # методом .capitalize() возвращаем слово с большей буквы


# применяем шифрование
word = 'Room'
print(f"Зашифнуем слово '{word}', ключ шифрования равен 3")
en_word = encrypt2(word, 3)
print(f"Зашифрованное слово '{en_word}'")
un_en_word = encrypt2(en_word, -3)
print(f"Расшифрованное слово '{un_en_word}'")
