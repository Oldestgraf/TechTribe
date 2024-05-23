"""This module contains functions for handling user input and address book operations."""

from models import CommandsDescription
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

@input_error_decorator_factory(args_length = 3, message = "Invalid command. Usage: change <name> <phone> <new_phone>")
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

@input_error_decorator_factory(args_length = 6, message = "Invalid command. Usage: add_address <name> <street> <city> <postal_code> <country>")
def add_address(name: str, street: str, city: str, postal_code: str, country: str, book: AddressBook):
    """Adds an address to a contact."""
    record = book.find(name)
    address = record.add_address(street, city, postal_code, country)
    print(f"Address added: {address}")

def help_info() -> dict:
    """Show list of available commands."""
    for command in CommandsDescription.get_commands_description():
        print(command)

@input_error_decorator_factory(args_length = 6, message = "Invalid command. Usage: edit_address <name> <street> <city> <postal_code> <country>")
def edit_address(name: str, street: str, city: str, postal_code: str, country: str, book: AddressBook):
    """Edits the address of a contact."""
    record = book.find(name)
    address = record.edit_address(street, city, postal_code, country)
    print(f"Address updated: {address}")

@input_error_decorator_factory()
def add_note(args, book):
    if len(args) < 2:
        raise IndexError("Invalid command. Usage: add_note <title> <text>")
    title, *text = args
    fixed_text = " ".join(text)
    print(book.add_note(title, fixed_text))


@input_error_decorator_factory()
def find_note_by_title(args, book):
    if len(args) < 1:
        raise IndexError("Invalid command. Usage: find_note <title>")
    title, = args
    print(book.find_note_by_title(title))


@input_error_decorator_factory()
def edit_note_text(args, book):
    if len(args) < 2:
        raise IndexError("Invalid command. Usage: edit_note <title> <text>")
    title, *new_text = args
    fixed_text = " ".join(new_text)
    print(book.edit_note_text(title, fixed_text))


@input_error_decorator_factory()
def delete_note_by_title(args, book):
    if len(args) < 1:
        raise IndexError("Invalid command. Usage: delete_note <title>")
    title, = args
    print(book.delete_note_by_title(title))


def show_notes(book):
    """Shows all notes in the address book."""
    if len(book.notes) > 0:
        for record in book.notes.values():
            print("-----------------------")
            print(f"Title: {record.title}")
            print(f"Text: {record.text}")
            print(f"Tags: {record.tags}")
    else:
        print("No notes found.")


@input_error_decorator_factory()
def add_tags_to_note(args, book):
    if len(args) < 2:
        raise IndexError("Invalid command. Usage: add_tags_to_note <title> <tag1> <tag2> ...")
    title, *tags = args
    print(book.add_tags_to_note(title, tags))


@input_error_decorator_factory()
def remove_tags_from_note(args, book):
    if len(args) < 2:
        raise IndexError("Invalid command. Usage: remove_tags_from_note <title> <tag1> <tag2> ...")
    title, *tags = args
    print(book.remove_tags_from_note(title, tags))


@input_error_decorator_factory()
def find_notes_by_tags(args, book):
    if len(args) < 1:
        raise IndexError("Invalid command. Usage: find_notes_by_tags <tag1> <tag2> ...")
    tags = args
    print(tags)
    found_notes = book.find_notes_by_tags(tags)
    if found_notes:
        for note in found_notes:
            print("-----------------------")
            print(note)
            print(f"Tags: {note.tags}")
    else:
        print("No notes found with the provided tags.")
