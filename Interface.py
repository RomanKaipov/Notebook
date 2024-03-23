from Notebook import *

def interface(notebook):
    with open('Notebook.json', 'a', encoding='UTF-8'):
        pass
    command = '-1'
    while command != '6':
        print('Возможные варианты взаимодействия:\n'
              '1. Добавить записку\n'
              '2. Вывести на экран все записки\n'
              '3. Вывести на экран записку по id\n'              
              '4. Редактирование записки\n'
              '5. Удаление записки\n'
              '6. Выход из программы\n')

        command = input('Введите номер действия: ')

        while command not in ('1', '2', '3', '4', '5', '6'):
            print('Некорректные данные, нужно ввести число комманды')
            command = input('Введите номер действия: ')

        match command:
            case '1':
                add_note(notebook)
            case '2':
                show_notes(notebook)
            case '3':
                show_note(notebook)
            case '4':
                edit_note(notebook)
            case '5':
                delete_note(notebook)
            case '6':
                print('Всего хорошего!')