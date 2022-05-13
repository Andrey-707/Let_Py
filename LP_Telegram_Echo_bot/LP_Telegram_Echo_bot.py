# LP_Telegram_Echo_bot

# Имя бота: LP_Echo_bot
# Никнейм бота: @LetPy1Bot
import requests

from config import TOKEN


print("Program start")

def send_message(chat_id, message):
    requests.get(
        f"https://api.telegram.org/bot" + str(TOKEN) + "/sendMessage",
        params={'chat_id': chat_id, 'text': message})
    
last_update_id = 0

while True:
    result = requests.get("https://api.telegram.org/bot" + str(TOKEN) + "/getUpdates",
        params={"offset": last_update_id + 1})
    data = result.json()
    for update in data["result"]:
        # print("update id:", update["update_id"]) # вывод данных в терминал
        # print("text:", update["message"]["text"]) # вывод данных в терминал

        last_update_id = update["update_id"]
        chat_id = update["message"]["chat"]["id"]
        first_name = update["message"]["from"]["first_name"]
        user_message = update["message"]["text"].lower()

        # реакция на сообщение от пользователя
        send_result = requests.get("https://api.telegram.org/bot" + str(TOKEN) + "/sendMessage",
            params={"chat_id": chat_id, "text": "LP_Echo_bot отвечает"})
        
        # ответ на сообщения пользователя
        if user_message == "привет":
            send_message(chat_id, f'И тебе привет,  {update["message"]["from"]["first_name"]} !')
        elif user_message == "пока":
            send_message(chat_id, f'И тебе пока,  {update["message"]["from"]["first_name"]} !')
        else:
            send_message(chat_id, "LP_Echo_bot реагирует на слова \"привет\" и \"пока\"")
        
print("Program finish")
