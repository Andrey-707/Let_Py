# LP_Telegram_Encryptor

# БОТ - шифровальщик. Использует шифр Цезаря (или сдвиг Цезаря).
# Бот получает сообщение, проводит кодировку текста и выводит зашифрованный текс на экран.
# Ключ шифрования задается как целое число, без кавычек.
# Текст для шифрования задается без символов и цифр в двойных кавычках.
import requests

from config import TOKEN


def encrypt(string, k):
    global con
    r_letters = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    e_letters = "ABCDEFGHIJKLMNOPQRSTWXYZ"
    con = ""
    for i in string:
        con += "1" if i.isupper() else "0"
    string = string.upper()
    rez = ""
    for i in string:
        if i in r_letters:
            j = r_letters.find(i)
            if j > -1: 
                j = (r_letters.find(i) + k) % 33
                rez = rez + r_letters[j]
            else: rez = rez + i
        elif i in e_letters:
            j = e_letters.find(i)
            if j > -1: 
                j = (e_letters.find(i) + k) % 24
                rez = rez + e_letters[j]
            else: rez = rez + i   
    return rez


def send_mes(text):
    global chat_id
    s_r = "https://api.telegram.org/bot" + str(TOKEN) + "/sendMessage"
    resalt1 = requests.get(s_r, params={"chat_id": chat_id, "text": text})


ks = -1
l_m = 0
key_ = None
text_ = None

while True:
    result = requests.get("https://api.telegram.org/bot" + str(TOKEN) + "/getUpdates",
    params = {"offset": l_m + 1})
    data = result.json()
    for ms in data["result"]:
        l_m = ms["update_id"]
        chat_id = ms["message"]["chat"]["id"]
        bd = ms["message"]["text"]
        
        # Поиск в сообщении текста для шифрования/расшифровки
        kt = -1
        nt = bd.find('"')
        if nt >= 0:
            kt = bd.find('"', nt + 1)
            if kt > 0:
                text_ = bd[nt + 1:kt]
                bd = bd.replace(text_, "")
        
        # Поиск в сообщении ключа для шифрования/расшифровки
        ns = -1
        i = -1
        for sym in bd:
            i += 1 
            if sym.isdigit():
                if ns == -1: ns = i
            elif ns >= 0:
                ks = i
                break
        else: 
            if ns >= 0:
                ks = i + 1 
            else: key_n = key_
        if ns >= 0:
            key_n = int(bd[ns:ks])
            if bd[ns - 1] == "-": key_n = -key_n

        # Подготовка текста сообщения
        if text_ != None and key_n != None:
            text_n = encrypt(text_,key_n)
            text_n1 = ""
            k = 0
            for i in con:
                text_n1 += text_n[k].lower() if i == "0" else text_n[k]
                k += 1 
        
        if key_n == None:
            send_mes("Укажите ключ шифрования.")
            if text_ == None:
                send_mes("Напишите текст для шифрования (в двойных кавычках).")
            else:
                send_mes("Напишите повторно текст для шифрования (в двойных кавычках).")
        else:
            if key_n != key_:
                if key_ != None:
                    send_mes("Вы изменили ключ для шифрования с {} на {}.".format(key_,key_n))
                else:
                    send_mes("Вы указали ключ для шифрования: {}.".format(key_n))            
            if text_ == None:
                send_mes("Напишите текст для шифрования (в двойных кавычках).")
            else:
                send_mes('Результат:  "{}"'.format(text_n1))
        text_ = None
        key_ = key_n
