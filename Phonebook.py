""" Задача №49:
Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. Фамилия, имя, отчество, номер
телефона - данные, которые должны находиться в файле.
1. Программа должна выводить данные
2. Программа должна сохранять данные в текстовом файле
3. Пользователь может ввести одну из характеристик для поиска определенной записи (Например имя или фамилию человека)
4. Использование функций. Ваша программа не должна быть линейной
"""

import os
import json

def file_path(file_name='contact_list') -> str:
    return os.path.join(os.path.dirname(__file__), f'{file_name}.txt')

def load_from_file() -> list: ##Эта функция не вызывается
    path = file_path()

    with open(path, 'r', encoding='UTF-8') as file:
        data = json.load(file)

    return data

def save_to_file(contact: list) -> None:
    path = file_path()

    with open(path, 'w', encoding='UTF-8') as file:
        json.dump(contact, file, ensure_ascii=False)

def show_on_screen(contacts: list) -> None:
    decode_keys = dict(
        first_name='Имя:',
        second_name='Фамилия:',
        contacts='Телефон:'
    )
    pretty_text = str()
    for num, elem in enumerate(contacts, 1):
        pretty_text += f'Контакт №{num}:\n'
        pretty_text += '\n'.join(f'{decode_keys[k]} {v}' for k, v in elem.items())
        pretty_text += '\n________\n'
    print(pretty_text)

def tests():
    contact = dict(
        first_name='Иван',
        second_name='Абрамов',
        contacts='123'
    )
    contact2 = dict(
        first_name='Петр',
        second_name='Шитиков',
        contacts='893'
    )
    contact3 = dict(
        first_name='Суслик',
        second_name='Хомяков',
        contacts='1493'
    )
    contact4 = dict(
        first_name='Ульяна',
        second_name='Караваева',
        contacts='87584'
    )
    contacts = [contact, contact2, contact3, contact4]
    return contacts

def find_contact(contacts: list) -> None:
    what = input('Кого ищем?\n>>> ')
    found = list(filter(lambda el: what in el['first_name'] or what in el['second_name'], contacts))
    if found:
        show_on_screen(found)
    else:
        print('Никого не нашли ;(')

def new_contact(contacts: list) -> None:
    contacts.append(
        dict(
            first_name=input('Введите имя контакта:\n>>> '),
            second_name=input('Введите фамилию контакта:\n>>> '),
            contacts=input('Введите номер телефона:\n>>> ')
        )
    )

def menu():
    commands = [
        'Показать все контакты',
        'Найти контакт',
        'Создать контакт',
        'Удалить контакт',
        'Изменить контакт'
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
    
def main() -> None:
    print('Программа запущена...')
    data = load_from_file()

    command = menu()
    if command == 0:
        show_on_screen(data)
    elif command == 1:
        find_contact(data)
    elif command == 2:
        new_contact(data)
    elif command == 3:
        delete_member(data)
    elif command == 4:
        change_member(data)

    save_to_file(data)
    print('Конец программы!')

def delete_member(contacts: list) -> None:
    show_on_screen(contacts)
    deleted = int(input('Укажите номер того, кого хотите удалить\n>>>'))
    contacts.pop(deleted-1)
    print('Новый список контактов: ')
    show_on_screen(contacts)

def change_member(contacts: list) -> None:
    show_on_screen(contacts)
    changed = int(input('Укажите номер того, кого хотите изменить\n>>>'))
    print('Изменяем данного гражданина: ')
    print(contacts[changed-1])
    contacts[changed-1] = dict(
            first_name=input('Введите новое имя контакта:\n>>> '),
            second_name=input('Введите новую фамилию контакта:\n>>> '),
            contacts=input('Введите новый номер телефона:\n>>> ')
        )
    print('Новый список контактов: ')
    show_on_screen(contacts)

if __name__ == '__main__':
    main()





