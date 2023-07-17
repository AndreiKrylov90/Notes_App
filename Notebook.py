""" Реализовать консольное приложение заметки, с сохранением, чтением,
добавлением, редактированием и удалением заметок. Заметка должна
содержать идентификатор, заголовок, тело заметки и дату/время создания или
последнего изменения заметки. Сохранение заметок необходимо сделать в
формате json или csv формат (разделение полей рекомендуется делать через
точку с запятой). Реализацию пользовательского интерфейса студент может
делать как ему удобнее, можно делать как параметры запуска программы
(команда, данные), можно делать как запрос команды с консоли и
последующим вводом данных, как-то ещё, на усмотрение студента.
"""

import os
import json
import datetime

def file_path(file_name='notes') -> str:
    return os.path.join(os.path.dirname(__file__), f'{file_name}.json')

def load_from_file() -> list: 
    path = file_path()

    with open(path, 'r', encoding='UTF-8') as file:
        data = json.load(file)

    data = sorted(data, key=lambda x: x['time']) #Added for sort
    return data

def save_to_file(note: list) -> None:
    path = file_path()

    with open(path, 'w', encoding='UTF-8') as file:
        json.dump(note, file, ensure_ascii=False, default=str) #Added last argument

def show_on_screen(notes: list) -> None:
    decode_keys = dict(
        title='Заголовок:',
        body='Тело заметки:',
        time='Дата создания/изменения:'
    )
    pretty_text = str()
    for num, elem in enumerate(notes, 1):
        pretty_text += f'Заметка №{num}:\n'
        pretty_text += '\n'.join(f'{decode_keys[k]} {v}' for k, v in elem.items())
        pretty_text += '\n________\n'
    print(pretty_text)


def find_note(notes: list) -> None:
    what = input('Какую заметку ищем, введите заголовок или часть текста или дату?\n>>> ')
    found = list(filter(lambda el: what.lower() in el['title'].lower() or what in el['body'].lower() or what in el['time'], notes))
    if found:
        show_on_screen(found)
    else:
        print('Ничего не нашли ;(')

def new_note(notes: list) -> None:
    notes.append(
        dict(
            title=input('Введите заголовок заметки:\n>>> '),
            body=input('Введите тело заметки:\n>>> '),
            time= datetime.datetime.now()
        )
    )

def menu():
    commands = [
        'Показать все заметки',
        'Найти заметку',
        'Создать заметку',
        'Удалить заметку',
        'Изменить заметку',
        'Выход из программы'
    ]
    print('Укажите номер команды:')
    print('\n'.join(f'{n}. {v}' for n, v in enumerate(commands, 1)))
    choice = input('>>> ')

    try:
        choice = int(choice)
        if choice < 0 or len(commands) < choice:
            raise Exception('Такой команды пока нет ;(')
        choice -= 1
    except ValueError as ex:
        print('Я вас не понял, повторите...')
        menu()
    except Exception as ex:
        print(ex)
        menu()
    else:
        return choice
    

def delete_note(notes: list) -> None:
    show_on_screen(notes)
    deleted = int(input('Укажите номер заметки, которую хотите удалить\n>>>'))
    notes.pop(deleted-1)
    print('Новый список заметок: ')
    show_on_screen(notes)

def change_note(notes: list) -> None:
    show_on_screen(notes)
    changed = int(input('Укажите номер заметки, которую хотите изменить\n>>>'))
    print('Изменяем данную заметку: ')
    print(notes[changed-1])
    notes[changed-1] = dict(
            title=input('Введите новый заголовок:\n>>> '),
            body=input('Введите новое тело заметки:\n>>> '),
            time= datetime.datetime.now()
        )
    print('Новый список заметок: ')
    show_on_screen(notes)


def main() -> None:
    data = load_from_file()

    command = menu()
    if command == 0:
        show_on_screen(data)
    elif command == 1:
        find_note(data)
    elif command == 2:
        new_note(data)
    elif command == 3:
        delete_note(data)
    elif command == 4:
        change_note(data)
    elif command == 5:
        return

    save_to_file(data)
    print('Команда выполнена!')
    print('________')
    main()

if __name__ == '__main__':
    main()





