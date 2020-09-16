import json
import os.path
from users.validation import has_duplicate, password_correct, is_userindex
import webbrowser

def login():
    """
    Функция обслуживает опцию логина пользователя из точки входа программы.

    :return:
    """
    login_value = input("Enter your username > ")

    # Загрузка базы данных пользователей из файла data.json для последующей проверки существования поьзователя, его пароля
    # и подгрузки ссылок пользователя в случае успешного логина
    filename = os.path.join("repository", "data.json")
    with open(filename) as jsonfile:
        all_users = json.load(jsonfile)

    if has_duplicate(all_users, "login", login_value):
        password = input("Enter your password > ")
        if password_correct(all_users, login_value, password):
            # Загружаем ссылки данного пользователя из списка словарей, для этого находим индекс словаря в списке all_users
            # а затем подгружаем вложенный словарь по ключу links
            user_links = all_users[is_userindex(all_users, login_value)]["links"]

            while True:
                action_choice = int(input("Welcome ! Select your action: \n1 - add link, \n2 - edit link, \n3 - use links, \n4 - exit \n> "))
                if action_choice == 4:
                    break
                elif action_choice == 1:
                    # Проверяем есть ли словарь в ключе links, если нет, то создаем пустой словарь для записи
                    if user_links == None:
                        user_links = {}
                    short_link = input("Enter your short link > ")
                    # Проверка есть ли уже в словаре такая же коротка ссылка
                    if not short_link in user_links:
                        # Если дубликата короткой ссылки нет, то запрос длинной ссылки
                        long_link = input("Enter your long link to pair with short link > ")
                        # Добавление новой записи в словарь
                        user_links[short_link] = long_link
                        # Добавление новой записи в список словарей всех пользователей
                        all_users[is_userindex(all_users, login_value)]["links"] = user_links
                        # Сериализация обновленной базы данных пользователей
                        with open(filename, "w") as jsonfile:
                            json.dump(all_users, jsonfile, indent=4)
                    else:
                        print("Such link already exists!")
                        continue

                elif action_choice == 2:
                    short_link = input("Enter your short link > ")
                    # Проверка есть ли уже в словаре такая же коротка ссылка
                    if short_link in user_links:
                        # Если ссылка есть, то запрос новой ссылки для переименования
                        new_short_link = input("Enter your new short link > ")
                        user_links[new_short_link] = user_links.pop(short_link)
                        # Добавление новой записи в список словарей всех пользователей
                        all_users[is_userindex(all_users, login_value)]["links"] = user_links
                        # Сериализация обновленной базы данных пользователей
                        with open(filename, "w") as jsonfile:
                            json.dump(all_users, jsonfile, indent=4)
                    else:
                        print("There is no such short link")
                        continue

                elif action_choice == 3:
                    try:
                        short_link = input("Enter your short link > ")
                        webbrowser.open(user_links[short_link])
                        continue
                    except:
                        print(f"There is no such link")
                        continue
        else:
            raise ValueError("Wrong password !")
    else:
        raise ValueError("Such user does not exist!")
