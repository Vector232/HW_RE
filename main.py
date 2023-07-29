from pprint import pprint
## Читаем адресную книгу в формате CSV в список contacts_list:
import csv
from module import *
with open("phonebook_raw.csv", encoding='utf-8') as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)

## 1. Выполните пункты 1-3 задания.
phonebook = phonebook_fixer(contacts_list)
phonebook.fix()
phonebook_list = phonebook.get_list()

## 2. Сохраните получившиеся данные в другой файл.
## Код для записи файла в формате CSV:
with open("phonebook.csv", "w", encoding='utf-8') as f:
  datawriter = csv.writer(f, delimiter=',')
  
## Вместо contacts_list подставьте свой список:
  datawriter.writerows(phonebook_list)