# Задание 1
# Создайте класс Editor, который содержит методы view_document и edit_document. Пусть метод
# edit_document выводит на экран информацию о том, что редактирование документов недоступно для
# бесплатной версии. Создайте подкласс ProEditor, в котором данный метод будет переопределён.
# Введите с клавиатуры лицензионный ключ и, если он корректный, создайте экземпляр класса ProEditor,
# иначе Editor. Вызовите методы просмотра и редактирования документов.

class Editor:
    def view_document(self):
        return f"You are in view mode."

    def edit_document(self):
        return f"No editing in free version, please buy a full version!"

class ProEditor(Editor):
    def edit_document(self):
        license_key = input("Please, enter your license key > ")
        if  license_key == "123abc)*":
            print("You are now using full version.")
            return object
        else:
            print("Your key is incorrect")
            
    def __str__(self):
        return f"You are using license version"

try1 = Editor()
print(try1.view_document())
print(try1.edit_document())
print()
try2 = ProEditor()
print(try2.view_document())
try2.edit_document()





