from constants import FILE_CONTACT_PATH, TAB
from utils import get_unique_number_for_contact


def show_all_contacts():
  with open(FILE_CONTACT_PATH, 'r', encoding='utf-8') as contacts:
    print(f'{TAB}Все контакты:')
    for line in contacts:
      print(f'{TAB}{line}', end='')


def create_contact():
  print(f'{TAB}Создание контакта: ')

  name = input(f'{TAB}Введите имя и фамилию для нового контакта: ')
  number = get_unique_number_for_contact(f'{TAB}Введите номер для нового контакта: ')
  comment = input(f'{TAB}Введите комментарий для нового контакта: ')

  new_contact = f'{name} - {number} - {comment}'

  with open(FILE_CONTACT_PATH, 'a', encoding='utf-8') as contacts:
    contacts.write(f'\n{new_contact}')

    print(f'{TAB}Контакт успешно добавлен')


def find_contact():
  search_contact = input(f'{TAB}Введите номер / имя / комментарий контакта, чтобы найти его: ')

  with open(FILE_CONTACT_PATH, 'r', encoding='utf-8') as contacts:
    contacts_by_search = [line for line in contacts if search_contact.lower() in line.lower()]

    print(f'{TAB}Результаты поиска:')

    if len(contacts_by_search):
      for line in contacts_by_search:
        print(f'{TAB}{line}', end='')
    else:
      print(f'{TAB}Ничего не найдено')