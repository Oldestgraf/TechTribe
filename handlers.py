"""This module contains functions for handling user input and address book operations."""

from models import AddressBook, Record
from decorator import input_error_decorator_factory

contacts = {}

def say_greeting():
    """Greets the user."""
    print("How can I help you?")        

@input_error_decorator_factory(args_length = 3, message = "Invalid command. Usage: add <name> <phone>")
def add_contact(name: str, phone: str, book: AddressBook) -> None:
    """Adds a contact to the address book or adds new phone if contact exists."""
    record = book.find(name, raise_error=False)
    message = "Contact added." if record is None else "Contact updated."

    if record is None:
        record = Record(name)
        book.add_record(record)
        message = f"{message} \nName: {name}"
    if phone:
        added_phone = record.add_phone(phone)
        message = f"{message} \nPhone: {added_phone}"

    print(message)

@input_error_decorator_factory(args_length = 3, message = "Invalid command. Usage: change <name> <phone> <new_phone")
def change_contact(name: str, phone: str, new_phone:str, book: AddressBook) -> None:
    """Changes the phone number of a contact."""
    record = book.find(name)
    record.edit_phone(phone, new_phone)

    print(f"Contact updated. \n Old: {phone} \n New: {new_phone}")

@input_error_decorator_factory(args_length = 2, message = "Invalid command. Usage: phone <name>")
def show_phone(name: str, book: AddressBook) -> str:
    """Shows the phone number of a contact."""
    record = book.find(name)
    print(f"Contact: {record.name}")
    for phone in record.phones:
        print(phone)

def find_contacts(book: AddressBook, queries: list[str]):
    """Shows contacts by search queries."""
    found = book.find_by_query(queries)
    if len(found) == 0:
        print("No contacts found.")
    for record in found:
        print("-----------------------")
        print(record)


@input_error_decorator_factory(args_length = 2, message = "Invalid command. Usage: show_contact <name>")
def show_contact(name: str, book: AddressBook) -> str:
    """Shows the contact information."""
    record = book.find(name)
    print(record)

def show_all(book) -> dict:
    """Shows all contacts in the address book."""
    for record in book.data.values():
        print("-----------------------")
        print(record)

@input_error_decorator_factory(args_length = 3, message = "Invalid command. Usage: add_birthday <name> <birthday>")
def add_birthday(name: str, birthday: str, book: AddressBook):
    """Adds a birthday to a contact."""
    record = book.find(name)
    record.add_birthday(birthday)
    print("Birthday added.")

@input_error_decorator_factory(args_length = 2, message = "Invalid command. Usage: show_birthday <name>")
def show_birthday(name: str, book: AddressBook):
    """Shows the birthday of a contact."""
    record = book.find(name)
    if not record.birthday:
        print("Birthday is not set.")
        return
    print(record.birthday)

@input_error_decorator_factory(message = "Invalid command. Usage: birthdays <upcoming_days>")
def birthdays(book, upcoming_days = 7):
    """Shows upcoming birthdays."""
    upcoming_birthdays = book.get_upcoming_birthdays(upcoming_days)
    if len(upcoming_birthdays) == 0:
        print("No upcoming birthdays.")
        return
    for item in upcoming_birthdays:
        print(f"{item["name"]}: {item["congratulation_date"]}")