import json
import datetime

def add_note(notebook):
    id = input("Введите ID записки: ")
    title = input("Введите заголовок записки: ")
    body = input("Введите содержание записки: ")
    created_at = datetime.datetime.now().strftime("%d-%m-%Y")
    updated_at = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    notebook.append({"id": id, "title": title, "body": body,
                  "created_at": created_at, "updated_at": updated_at})
    print("Записка создана")
    save_file(notebook)

def show_note(notebook):
    id = input("Введите ID записки: ")
    for note in notebook:
        if note['id'] == " " or note['id'] != id:
            print("Записка не найдена")
            break
        elif note['id'] == id:
            print(f"ID: {note['id']}")
            print(f"Заголовок: {note['title']}")
            print(f"Содержание: {note['body']}")
            print(f"Дата/время создания: {note['created_at']}")
            print(f"Дата/время последнего изменения: {note['updated_at']}")

def show_notes(notebook):
    for note in notebook:
        print(
            f"ID: {note['id']}, Заголовок: {note['title']}, Дата/время создания: {note['created_at']}")

def edit_note(notebook):
    id = input("Введите ID записки для редактирования: ")
    for note in notebook:
        if note['id'] == " " or note['id'] != id:
            print("Записка не найдена")
            break
        elif note['id'] == id:
            title = input("Введите новый заголовок записки: ")
            body = input("Введите новое содержание записки: ")
            note['title'] = title
            note['body'] = body
            note['updated_at'] = datetime.datetime.now().strftime(
                "%d-%m-%Y %H:%M:%S")
            break
    save_file(notebook)

def delete_note(notebook):
    id = input("Введите ID записки для удаления: ")
    for note in notebook:
        if note['id'] == id:
            notebook.remove(note)
            break
        else:
            print("Записка не найдена")
    save_file(notebook)

def load_file():
    try:
        with open("Notebook.json", "r") as file:
            notebook = json.load(file)
    except FileNotFoundError:
        notebook = []
    return notebook

def save_file(notebook):
      with open("Notebook.json", "w") as file:
         json.dump(notebook, file)