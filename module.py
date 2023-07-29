def name_fixer(last, first, surname):
    def disconnector(string):
        pass
    def relocator(first, second, third):
        pass
    pass

def phones_fixer(phone):
    pass

def coupler(first, second):
    pass

def phonebook_fixer(phonebook_raw):
    phonebook = ['N', phonebook_raw[0]]
    for n, note in enumerate(phonebook_raw[1:]):
        phonebook.append([n, note])
    return phonebook