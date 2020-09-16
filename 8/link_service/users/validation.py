def has_duplicate(listdict, key_to_check, value_to_check):
    """
    Функция для проверки списка словарей, есть ли значие по заданному ключу в любом из списков словарей
    :param listdict:
    :param key_to_check:
    :param value_to_check:
    :return:
    """
    for pers in range(len(listdict)):
        if listdict[pers][key_to_check] == value_to_check:
            return True

def password_correct(listdict, username, pswd):
    """
    Проверка пароля пользователя из списка словарей по заданному пользователю
    :param listdict:
    :param username:
    :param pswd:
    :return:
    """
    for pers in range(len(listdict)):
        if listdict[pers]["login"] == username and listdict[pers]["password"] == pswd:
            return True

def is_userindex(listdict, username):
    """
    Определяет индекс словаря в списке словарей, в котором находится пользователь т.е. username

    :param listdict: список словарей, которые будут выгружены из файла data.json
    :param username: критерий поиска
    :return: возвращает индекс искомого словаря в списке словарей с данными пользователей
    """
    for pers in range(len(listdict)):
        if listdict[pers]["login"] == username:
            return pers