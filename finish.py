from collections import UserDict

class Field:
    pass


class Name(Field):
    def add_name(self, name):
        self.value = name


class Phone(Field):
    pass


class AddressBook(UserDict):
    data = {}

    def add_record(self, record):
        self.data[Record.name.value] = record


class Record:
    name = Name()
    phone = []

    def add_phone(self, phone):
        if phone in self.phone:
            return "This phone has existed already."
        self.phone.append(phone)

    def delete_phone(self, phone):
        self.phone.remove(phone)

    def edit_phone(self, old_phone, new_phone):
        self.add_phone(new_phone)
        self.delete_phone(old_phone)










