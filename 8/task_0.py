"""
Задание
Создайте список товаров в интернет-магазине. Сериализуйте его при помощи pickle и сохраните в JSON.
"""

import json
import pickle

webshop = {
    "shampoo": 12000,
    "soap": 10000,
    "tooth paste": 8000,
    "washing powder": 14000,
}

with open("webshop.pkl", "wb") as file:
    pickle.dump(webshop, file)

with open("webshop.json", "w") as file:
    json.dump(webshop, file)

with open("webshop.pkl", "rb") as rbfile:
    result = pickle.load(rbfile)

print(result)

with open("webshop.json") as jsonfile:
    result = json.load(jsonfile)

print(result)
