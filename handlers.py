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

def show_all(book) -> dict:
    """Shows all contacts in the address book."""
    for record in book.data.values():
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
    print(record.birthday.value.strftime("%d.%m.%Y"))

@input_error_decorator_factory(message = "Invalid command. Usage: birthdays <upcoming_days>")
def birthdays(book, upcoming_days = 7):
    """Shows upcoming birthdays."""
    upcoming_birthdays = book.get_upcoming_birthdays(upcoming_days)
    if len(upcoming_birthdays) == 0:
        print("No upcoming birthdays.")
        return
    for item in upcoming_birthdays:
        print(f"{item['name']}: {item['congratulation_date']}")


@input_error_decorator_factory()
def add_note(args, book):
    if len(args) < 2:
        raise IndexError
    title, *text = args
    fixed_text = " ".join(text)
    print(book.add_note(title, fixed_text))


@input_error_decorator_factory()
def find_note_by_title(args, book):
    if len(args) < 1:
        raise IndexError
    title, = args
    print(book.find_note_by_title(title))


@input_error_decorator_factory()
def edit_note_text(args, book):
    if len(args) < 2:
        print("Invalid command. Usage: edit_note_text <title> <text>")
    title, *new_text = args
    fixed_text = " ".join(new_text)
    print(book.edit_note_text(title, fixed_text))


@input_error_decorator_factory()
def delete_note_by_title(args, book):
    if len(args) < 1:
        raise IndexError
    title, = args
    print(book.delete_note_by_title(title))
