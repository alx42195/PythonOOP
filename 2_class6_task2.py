"""
Задание 2
Создайте программу, которая эмулирует работу сервиса по сокращению ссылок. Должна быть
реализована возможность ввода изначальной ссылки и короткого названия и получения изначальной
ссылки по её названию.

Задание 3
Ознакомьтесь при помощи документации с классами OrderedDict, defaultdict и ChainMap модуля
collections.  -- ОЗНАКОМИЛСЯ
"""

class LinksMaster:
    def __init__(self, url_full, url_short):
        self.url_full = url_full
        self.url_short = url_short

    @property
    def short_link(self):
        return self.url_short

    @short_link.setter
    def short_link(self, new_name):
        self.url_short = new_name

    @property
    def long_link(self):
        return self.url_full

    @long_link.setter
    def long_link(self, new_name):
        self.url_full = new_name

    def __repr__(self):
        return f"{self.url_full} | {self.url_short}"

    def __str__(self):
        return f"Short link: {self.url_short}, long link: {self.url_full}"


def main():
    data = input("Please enter your full link and your short name separated by space > ").split(" ")
    link = LinksMaster(*data)
    while True:
        keyboard_input = input("Enter your short address > ")
        try:
            if keyboard_input != link.short_link:
                raise ValueError("There is no such address")
            else:
                print(f"You are redirected to : {link.long_link}")
                break
        except ValueError as err:
            print(f"Oops, {err}")


if __name__ == "__main__":
    main()


