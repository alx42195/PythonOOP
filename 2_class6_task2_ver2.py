"""
Задание 2
Создайте программу, которая эмулирует работу сервиса по сокращению ссылок. Должна быть
реализована возможность ввода изначальной ссылки и короткого названия и получения изначальной
ссылки по её названию.
"""


def links_master(long_name, short_name):
    return dict(long_link=long_name, short_link=short_name)

def main():
    data = input("Please enter your full link and your short name separated by space > ").split(" ")
    link = links_master(*data)
    while True:
        keyboard_input = input("Enter your short address > ")
        try:
            if keyboard_input != link["short_link"]:
                raise ValueError("There is no such address")
            else:
                print(f"You are redirected to : {link['long_link']}")
                break
        except ValueError as err:
            print(f"Oops, {err}")


if __name__ == "__main__":
    main()


