from constants import FILE_CONTACT_PATH, TAB
from database.contacts_manager import create_contact, delete_contact_by_number, edit_contact, find_contact, show_all_contacts


def show_control():
  print('')
  print(f'''{TAB}Справочник контактов. Управление:''')
  
  for action_number in CONTACTS_CONTROL:
    print(TAB, end='')
    print(f'''{action_number} - {CONTACTS_CONTROL[action_number]['info']}''')

  print('')
  get_action_number()


def do_action(action):
  action()
  print('')
  show_control()


def get_action_number():
  action_number = int(input(f'{TAB}Чтобы выполнить действие, ведите его номер: '))
  print('')

  possible_action_numbers = [action_number for action_number in CONTACTS_CONTROL]
  action_by_number = (CONTACTS_CONTROL.get(action_number) or dict()).get('action')

  if action_number in possible_action_numbers:
    if action_by_number:
      do_action(action_by_number)
  else:
    print(f'{TAB}Номера действия ({action_number}) не существует. Попробуйте ещё раз')
    get_action_number()


# Управление справочников
# Пользователь вводит цифру, которая является ключом этого словаря
# И по этому ключу вызывается функция в поле 'action'
CONTACTS_CONTROL = {
  3: { 'info': 'Показать все контакты', 'action': show_all_contacts },
  4: { 'info': 'Создать контакт', 'action': create_contact },
  5: { 'info': 'Найти контакт', 'action': find_contact },
  6: { 'info': 'Изменить контакт', 'action': edit_contact },
  7: { 'info': 'Удалить контакт', 'action': delete_contact_by_number },
  8: { 'info': 'Выход', 'action': None },
}

show_control()