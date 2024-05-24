"""Module for record model"""

from .fields import Name, Phone, Birthday, Address, Email
from typing import List

class Record:
    """Class representing a record in the address book."""
    def __init__(self, name: str):
        self.name = Name(name)
        self.phones = []
        self.birthday = None
        self.address = None
        self.email = None

    def __str__(self):
        message = f"Contact name: {self.name.value}\n"
        message += f"Phones: {'; '.join(p.value for p in self.phones)}\n"
        message += f"Birthday: {self.birthday or 'Not set'}\n"
        message += f"Address: {self.address or 'Not set'}\n"
        message += f"Email: {self.email or 'Not set'}"
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

    def add_email(self, email: str):
        """Add email to the record."""
        self.email = Email(email)

    def edit_email(self, new_email: str):
        """Edit email in the record."""
        if not self.email:
            raise ValueError("No email to edit. Add an email first.")
        self.email = Email(new_email)

    def remove_email(self):
        """Remove a email from the record."""
        if self.email:
            self.email = None
        else:
            raise ValueError("No email to remove.")

    def search_by_email(self, email: str) -> List['Record']:
        """Search for contacts by their email addresses."""
        found_contacts = []
        if self.email and self.email.value == email:
            found_contacts.append(self)
        return found_contacts

    def add_address(self, street: str, city: str, postal_code: str, country: str):
        """Add address to the record."""
        self.address = Address(street, city, postal_code, country)
        return self.address

    def edit_address(self, street: str, city: str, postal_code: str, country: str):
        """Edit address in the record."""
        self.address = Address(street, city, postal_code, country)
        return self.address
