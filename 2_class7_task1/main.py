"""
Задание 1
Перепишите домашнее задание предыдущего урока (сервис для сокращения ссылок) таким образом,
чтобы у него была основная часть, которая отвечала бы за логику работы и предоставляла обобщённый
интерфейс, и модуль представления, который отвечал бы за взаимодействие с пользователем. При
замене последнего на другой, взаимодействующий с пользователем иным способом, программа
должна продолжать корректно работать.

Задание 2
Повторите информацию о рассмотренных на уроке стандартных модулях. Ознакомьтесь также с
модулями calendar, heapq, bisect, array, enum.  -- ОЗНАКОМИЛСЯ
"""

# Модуль links_master отвечает за замену ссылок
# Модуль communication отвечает за диалог с пользователем

from links_master import LinksMaster
from communication import enter_full_link, enter_short_link, show_result
from exceptions import AddressError

def main():
    full_link = enter_full_link()
    short_link = enter_short_link()
    link = LinksMaster(full_link, short_link)
    while True:
        keyboard_input = enter_short_link()
        try:
            if keyboard_input != link.short_link:
                raise AddressError("There is no such address, please try again!")
            else:
                print(f"You are redirected to : {link.long_link}")
                break
        except AddressError as err:
            print(f"Opps, {err}")

if __name__ == "__main__":
    main()