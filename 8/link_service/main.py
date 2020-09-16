from users.interaction.logins import login
from users.interaction.signups import signup

def main():
    """
    Структура программы:
    папка interaction - работа с логином и созданием пользователей - login, signup
    profiles - конструктор пользователя (используется в signup)
    папка repository - база данных пользователей, которые сериализуются/десериализуютя при помощи data.json
    папка validation - функции для работы с модулями login/signup


    :return:
    """
    while True:
        choice = int(input("""
        Select an action:
        1 - Log In;
        2 - Sign Up;
        3 - Exit;
        > """))
        try:
            if choice == 3:
                break
            elif choice == 1:
                try:
                    login()
                    continue
                except ValueError as err:
                    print(f"Opps.. {err}")
            elif choice == 2:
                signup()
                continue
            else:
                raise ValueError("Such option does not exist, please try again!")
        except ValueError as err:
            print(f"Oops.. {err}")

if __name__ == '__main__':
    main()



