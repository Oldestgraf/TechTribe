from .fields import Name, Phone, Birthday, Email
from typing import Union


class Record:
    def __init__(self, name: str):
        self.name = Name(name)
        self.phones = []
        self.birthday = None
        self.email = None

    def __str__(self):
            return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

    def add_phone(self, phone: str):
        if self.find_phone(phone):
            raise ValueError("Phone already exists.")
        phone = Phone(phone)
        self.phones.append(phone)
        return phone

    def remove_phone(self, phone: str):
        phone_to_remove = self.find_phone(phone)
        if phone_to_remove:
            self.phones.remove(phone_to_remove)

    def edit_phone(self, phone: str, new_phone: str):
        phone_to_update = self.find_phone(phone)
        if not phone_to_update:
            raise ValueError("Phone does not exist")

        self.phones[self.phones.index(phone_to_update)] = Phone(new_phone)

    
    def find_phone(self, phone: str) -> Union[Phone, None]:
        phone = Phone(phone)
        for p in self.phones:
            if p == phone:
                return p

        return None

    def add_birthday(self, birthday: str):
         self.birthday = Birthday(birthday)

    def add_email(self, email: str):
        self.email = Email(email)
    def edit_email(self, new_email: str):
        if not self.email:
            raise ValueError("No email to edit. Add an email first.")
        self.email = Email(new_email)
    def remove_email(self):
        if self.email:
            self.email = None
        else:
            raise ValueError("No email to remove.")