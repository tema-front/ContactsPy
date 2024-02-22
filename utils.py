from constants import FILE_CONTACT_PATH, TAB

# Возвращает номер, если он уникальный (не встречается контактов в справочнике с таким же номером)
def get_unique_number_for_contact(inputTxt: str, exception: str = ''):
  new_number = input(inputTxt)

  existing_numbers = get_existing_numbers(exception)

  if new_number in existing_numbers:
    print(f'{TAB}Контакт с данным номером ({new_number}) уже существует. Попробуйте ещё раз')
    get_unique_number_for_contact(inputTxt)

  return new_number


# Возвращает список номеров всех контактов из справочника
def get_existing_numbers(exception: str = '') -> list[str]:
  contact_numbers = []
  with open(FILE_CONTACT_PATH, 'r', encoding='utf-8') as contacts:
    contact_numbers = [item.split(' - ')[1] for item in contacts if item.split(' - ')[1] != exception]

  return contact_numbers