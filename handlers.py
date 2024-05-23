"""This module contains functions for handling user input and address book operations."""

from models import CommandsDescription
from models import AddressBook, Record, Commands, commands_config, Colors
from decorator import input_error_decorator_factory
from dialogs.print_text import print_text

@input_error_decorator_factory(message = commands_config[Commands.ADD])
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

    print_text(message, Colors.SUCCESS)

@input_error_decorator_factory(message = commands_config[Commands.CHANGE])
def change_contact(name: str, phone: str, new_phone:str, book: AddressBook) -> None:
    """Changes the phone number of a contact."""
    record = book.find(name)
    record.edit_phone(phone, new_phone)

    print_text(f"Contact updated. \n Old: {phone} \n New: {new_phone}", Colors.SUCCESS)

@input_error_decorator_factory(message = commands_config[Commands.PHONE])
def show_phone(name: str, book: AddressBook) -> str:
    """Shows the phone number of a contact."""
    record = book.find(name)
    print(f"Contact: {record.name}")
    for phone in record.phones:
        print_text(phone, Colors.INFO)

def find_contacts(book: AddressBook, queries: list[str]):
    """Shows contacts by search queries."""
    found = book.find_by_query(queries)
    if len(found) == 0:
        print_text("No contacts found.", Colors.WARNING)
    for record in found:
        print_text("-----------------------", Colors.INFO)
        print_text(record, Colors.INFO)


@input_error_decorator_factory(message = commands_config[Commands.SHOW_CONTACT])
def show_contact(name: str, book: AddressBook) -> str:
    """Shows the contact information."""
    record = book.find(name)
    print_text(record, Colors.INFO)

def show_all(book) -> dict:
    """Shows all contacts in the address book."""
    for record in book.data.values():
        print_text("-----------------------", Colors.INFO)
        print_text(record, Colors.INFO)

@input_error_decorator_factory(message = commands_config[Commands.ADD_BIRTHDAY])
def add_birthday(name: str, birthday: str, book: AddressBook):
    """Adds a birthday to a contact."""
    record = book.find(name)
    record.add_birthday(birthday)
    print_text("Birthday added.", Colors.SUCCESS)

@input_error_decorator_factory(message = commands_config[Commands.SHOW_BIRTHDAY])
def show_birthday(name: str, book: AddressBook):
    """Shows the birthday of a contact."""
    record = book.find(name)
    if not record.birthday:
        print_text("Birthday is not set.")
        return
    print_text(record.birthday, Colors.INFO)

@input_error_decorator_factory(message = commands_config[Commands.BIRTHDAYS])
def birthdays(book, upcoming_days = 7):
    """Shows upcoming birthdays."""
    upcoming_birthdays = book.get_upcoming_birthdays(upcoming_days)
    if len(upcoming_birthdays) == 0:
        print_text("No upcoming birthdays.")
        return
    for item in upcoming_birthdays:
        print_text(f"{item["name"]}: {item["congratulation_date"]}", Colors.INFO)

@input_error_decorator_factory(message=commands_config[Commands.ADD_ADDRESS])
def add_address(name: str, street: str, city: str, postal_code: str, country: str, book: AddressBook):
    """Adds an address to a contact."""
    record = book.find(name)
    address = record.add_address(street, city, postal_code, country)
    print(f"Address added: {address}")

def help_info() -> dict:
    """Show list of available commands."""
    for command in CommandsDescription.get_commands_description():
        print_text(command, Colors.INFO)

@input_error_decorator_factory(message=commands_config[Commands.EDIT_ADDRESS])
def edit_address(name: str, street: str, city: str, postal_code: str, country: str, book: AddressBook):
    """Edits the address of a contact."""
    record = book.find(name)
    address = record.edit_address(street, city, postal_code, country)
    print(f"Address updated: {address}")
    
@input_error_decorator_factory()
def add_note(args, book):
    """Adds a note to the address book."""
    if len(args) < 2:
        raise IndexError
    title, *text = args
    fixed_text = " ".join(text)
    print_text(book.add_note(title, fixed_text), Colors.SUCCESS)


@input_error_decorator_factory()
def find_note_by_title(args, book):
    """Finds a note by title."""
    if len(args) < 1:
        raise IndexError
    title, = args
    print_text(book.find_note_by_title(title), Colors.INFO)


@input_error_decorator_factory(message=commands_config[Commands.EDIT_NOTE])
def edit_note_text(args, book):
    """Edits a note by title."""
    if len(args) < 2:
        print(f"Invalid command. Usage: {commands_config[Commands.EDIT_NOTE]}")
    title, *new_text = args
    fixed_text = " ".join(new_text)
    print_text(book.edit_note_text(title, fixed_text), Colors.SUCCESS)


@input_error_decorator_factory()
def delete_note_by_title(args, book):
    """Deletes a note by title."""
    if len(args) < 1:
        raise IndexError
    title, = args
    print_text(book.delete_note_by_title(title), Colors.SUCCESS)
