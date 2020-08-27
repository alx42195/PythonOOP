"""
Дополнительное задание

Создайте словарь с ключами-строками и значениями-числами. Создайте функцию, которая принимает
произвольное количество именованных параметров. Вызовите её с созданным словарём и явно
указывая параметры.
"""

def device_print(**kwargs):
    print(f"WiFi router id: {kwargs['device_id']} | WiFi password: {kwargs['password']}")

wifi1 = {
    "device_id": 12345,
    "year of installation": 2015,
    "speed": 500,
    "password": 1234567890
}

wifi2 = {
    "device_id": 34526,
    "year of installation": 2020,
    "speed": 100,
    "password": 5642390127
}

devices = wifi1, wifi2

for item in devices:
    device_print(**item)

for item,value in wifi1.items():
    print(item,value)
