import re


class phonebook_fixer:
    def __init__(self, phonebook_raw) -> None:
        self.phonebook_raw = phonebook_raw
        self.phonebook = [phonebook_raw[0]]

    def __str__(self, phonebook) -> str:
        output = ''
        for note in phonebook:
            output = output + note
        return output
    
    def get_list(self):
        return self.phonebook

    # основа алгоритма
    def fix(self):
        temp_phonebook = []
        # собирает данные из двух записей в одну
        def coupler(note1, note2):
            for i, val in enumerate(note1):
                if val == '':
                    note1[i] = note2[i]
            return note1

        # приводит в порядок ФИО
        def name_fixer(last, first, surname):
            lastname_list = last.split(sep=" ")
            firstname_list = first.split(sep=" ")

            if len(lastname_list) == 3:
                last, first, surname = lastname_list
            elif len(lastname_list) == 2:
                last, first = lastname_list
            elif len(firstname_list) == 2:
                first, surname = firstname_list

            return [last, first, surname]

        # приводит телефонные номера к одному стандарту
        def phones_fixer(phone):
            patern = r'(\+7|8)?\s*\(?(\d{3})\)?[-\s]*(\d{0,3})[-\s]*(\d{2})[-\s]*(\d{2,4})(\s*\(?доб\.\s*(\d{4})\)?)?'
            replace_add = r'+7(\2)\3-\4-\5 доб.\7'
            replace = r'+7(\2)\3-\4-\5'

            if re.search(r'доб', phone) != None:
                standart_phone = re.sub(patern, replace_add, phone)
            else:
                standart_phone = re.sub(patern, replace, phone)

            return standart_phone
        
        # приводим в порядок данные
        for note in self.phonebook_raw[1:]:
            temp_phonebook.append(name_fixer(*note[:3]))
            temp_phonebook[-1].extend([note[3], note[4]])
            temp_phonebook[-1].extend([phones_fixer(note[5])])
            temp_phonebook[-1].extend([note[6]])

        # избавляемся от дублей
        for i, note1 in enumerate(temp_phonebook):
            f = True
            for j, note2 in enumerate(temp_phonebook[i+1:]):
                if (note1[0], note1[1]) == (note2[0], note2[1]):
                    temp_phonebook[j+i+1] = coupler(note1, note2)
                    f = False
                    break
            if f: self.phonebook.append(note1)
                    
        return True