from users.profiles import User
import json
import os.path
from users.validation import has_duplicate, password_correct

def signup():

    USERDATA = {
        "name": input("Enter you name > "),
        "email": input("Enter you email > "),
        "login": input("Enter your login > "),
        "password": input("Create you password > "),
        "links": None
    }
    new_user = User(**USERDATA)

    filename = os.path.join("repository", "data.json")

    with open(filename) as jsonfile:
        new_user.all_users = json.load(jsonfile)

    if not has_duplicate(new_user.all_users, "login", new_user.login):
        new_user.all_users.append(USERDATA)

    with open(filename, "w") as jsonfile:
        json.dump(new_user.all_users, jsonfile, indent=4)