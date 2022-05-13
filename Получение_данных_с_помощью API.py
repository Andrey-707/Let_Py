# Курса доллар США относительно белорусского рубля
# Метод №1
import requests
import json


result = requests.get("https://www.nbrb.by/api/exrates/rates/usd?parammode=2")
# {"Cur_ID":431,"Date":"2022-05-12T00:00:00","Cur_Abbreviation":"USD","Cur_Scale":1,"Cur_Name":"Доллар США","Cur_OfficialRate":2.5945}
data = json.loads(result.text)
print(data["Cur_Name"])
print(data["Cur_OfficialRate"])

# Метод №2
import requests
import json


result = requests.get("https://www.nbrb.by/api/exrates/rates/usd?parammode=2")
# {"Cur_ID":431,"Date":"2022-05-12T00:00:00","Cur_Abbreviation":"USD","Cur_Scale":1,"Cur_Name":"Доллар США","Cur_OfficialRate":2.5945}
data = result.json()
print(data["Cur_Name"])
print(data["Cur_OfficialRate"])
