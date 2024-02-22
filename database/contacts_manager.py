from constants import FILE_CONTACT_PATH, TAB


def show_all_contacts():
  with open(FILE_CONTACT_PATH, 'r', encoding='utf-8') as contacts:
    print(f'{TAB}Все контакты:')
    for line in contacts:
      print(f'{TAB}{line}', end='')