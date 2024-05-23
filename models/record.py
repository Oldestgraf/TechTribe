"""Module for record model"""

from .fields import Name, Phone, Birthday

class Record:
    """Class representing a record in the address book."""
    def __init__(self, name: str):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def __str__(self):
            message = f"Contact name: {self.name.value}\n"
            message += f"Phones: {'; '.join(p.value for p in self.phones)}\n"
            message += f"Birthday: {self.birthday or 'Not set'}"
            return message

    def add_phone(self, phone: str):
        """Adds a phone to the record."""
        if self.find_phone(phone):
            raise ValueError("Phone already exists.")
        phone = Phone(phone)
        self.phones.append(phone)
        return phone

    def remove_phone(self, phone: str):
        """Remove a phone from the record."""
        phone_to_remove = self.find_phone(phone)
        if phone_to_remove:
            self.phones.remove(phone_to_remove)

    def edit_phone(self, phone: str, new_phone: str):
        """Edit a phone in the record."""
        phone_to_update = self.find_phone(phone)
        if not phone_to_update:
            raise ValueError("Phone does not exist")

        self.phones[self.phones.index(phone_to_update)] = Phone(new_phone)

    def find_phone(self, phone: str) -> Phone | None:
        """Find phones in the record."""
        phone = Phone(phone)
        for p in self.phones:
            if p == phone:
                return p

        return None

    def add_birthday(self, birthday: str):
         """Add birthday to the record."""
         self.birthday = Birthday(birthday)