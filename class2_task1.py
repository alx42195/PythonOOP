# Задание 1
# Напишите программу, которая спрашивает у пользователя  слова и выводит их
# разделёнными запятой.
user_vocabulary=[]

name=input("Please, enter your name > ")

def show_help():
    print(f""" Dear {name}! This is vocabulary builder.
Enter as many English words as you know.

for help type 'HELP'
to stop entering words type 'DONE' 
to show your vocabulary type 'SHOW'""")

def add_to_vocabulary(word):
    user_vocabulary.append(word)

# def show_vocabulary():
#     print("Here is your vocabulary!")
#     for item in user_vocabulary:
#         print(item, end=", ")

def show_vocabulary():
   print("Here is your vocabulary!")
   print(*user_vocabulary, sep=", ")

show_help()

while True:
    word=input("> ")

    if word.lower()=="done":
        break
    elif word.lower()=="help":
        show_help()
        continue
    elif word.lower()=="show":
        show_vocabulary()
        continue

    add_to_vocabulary(word)

show_vocabulary()

