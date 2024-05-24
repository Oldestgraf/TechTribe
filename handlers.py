"""This module contains functions for handling user input and address book operations."""

from models import CommandsDescription
from models import AddressBook, Record, Commands, commands_config, Colors, Email
from decorator import input_error_decorator_factory
from dialogs.print_text import print_text


@input_error_decorator_factory(message=commands_config[Commands.ADD])
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


@input_error_decorator_factory(message=commands_config[Commands.CHANGE])
def change_contact(name: str, phone: str, new_phone: str, book: AddressBook) -> None:
    """Changes the phone number of a contact."""
    record = book.find(name)
    record.edit_phone(phone, new_phone)

    print(f"Contact updated. \n Old: {phone} \n New: {new_phone}")


@input_error_decorator_factory(message=commands_config[Commands.PHONE])
def show_phone(name: str, book: AddressBook) -> str:
    """Shows the phone number of a contact."""
    record = book.find(name)
    print_text(f"Contact: {record.name}", Colors.INFO)
    for phone in record.phones:
        print(phone)


def find_contacts(book: AddressBook, queries: list[str]):
    """Shows contacts by search queries."""
    found = book.find_by_query(queries)
    if len(found) == 0:
        print_text("No contacts found.", Colors.WARNING)
    for record in found:
        print_text("-----------------------", Colors.INFO)
        print(record)


@input_error_decorator_factory(message=commands_config[Commands.SHOW_CONTACT])
def show_contact(name: str, book: AddressBook) -> str:
    """Shows the contact information."""
    record = book.find(name)
    print(record)


def show_all(book) -> dict:
    """Shows all contacts in the address book."""
    if len(book.data) == 0:
        print_text("No contacts found.", Colors.WARNING)
        return

    for record in book.data.values():
        print_text("-----------------------", Colors.INFO)
        print(record)


@input_error_decorator_factory(message=commands_config[Commands.ADD_BIRTHDAY])
def add_birthday(name: str, birthday: str, book: AddressBook):
    """Adds a birthday to a contact."""
    record = book.find(name)
    record.add_birthday(birthday)
    print_text("Birthday added.", Colors.SUCCESS)


@input_error_decorator_factory(message=commands_config[Commands.SHOW_BIRTHDAY])
def show_birthday(name: str, book: AddressBook):
    """Shows the birthday of a contact."""
    record = book.find(name)
    if not record.birthday:
        print_text("Birthday is not set.")
        return
    print(record.birthday)


@input_error_decorator_factory(message=commands_config[Commands.BIRTHDAYS])
def birthdays(book, upcoming_days=7):
    """Shows upcoming birthdays."""
    upcoming_birthdays = book.get_upcoming_birthdays(upcoming_days)
    if len(upcoming_birthdays) == 0:
        print_text("No upcoming birthdays.")
        return
    for item in upcoming_birthdays:
        print_text(f"{item['name']}: {item['congratulation_date']}", Colors.INFO)


@input_error_decorator_factory(message="Invalid command. Usage: add_email <name> <email>")
def add_email(name: str, email: str, book: AddressBook):
    record = book.find(name)
    record.add_email(email)
    print(f"Email added for {name}: {email}")


@input_error_decorator_factory(message="Invalid command. Usage: edit_email <name> <new_email>")
def edit_email(name: str, new_email: str, book: AddressBook):
    record = book.find(name)
    record.edit_email(new_email)
    print(f"Email updated for {name}: {new_email}")


@input_error_decorator_factory(message="Invalid command. Usage: search_by_email <email>")
def search_by_email(email: str, book: AddressBook):
    found_records = []
    for record in book.data.values():
        if record.email and record.email.value == email:
            found_records.append(record)

    if found_records:
        print("Found contacts:")
        for record in found_records:
            print(record)
    else:
        print("No contacts found with the provided email.")


@input_error_decorator_factory(message="Invalid command. Usage: remove_email <name>")
def remove_email(name: str, book: AddressBook):
    record = book.find(name)
    record.remove_email()
    print(f"Email removed for {name}")


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


@input_error_decorator_factory(message=commands_config[Commands.DELETE_ADDRESS])
def delete_address(name: str, book: AddressBook):
    """Deletes the address of a contact."""
    record = book.find(name)
    record.delete_address()
    print(f"Address deleted for {name}")


@input_error_decorator_factory(message="Invalid command. Usage: delete <name>")
def delete_contact(name: str, book: AddressBook):
    """Deletes a contact from the address book."""
    book.delete(name)
    print(f"Contact {name} deleted.")


def delete_all_contacts(book: AddressBook):
    """Deletes all contacts from the address book."""
    book.data.clear()
    print("All contacts have been deleted.")


@input_error_decorator_factory()
def add_note(args, book):
    """Adds a note to the address book."""
    if len(args) < 2:
        raise IndexError("Invalid command. Usage: add_note <title> <text>")
    title, *text = args
    fixed_text = " ".join(text)
    print(book.add_note(title, fixed_text))


@input_error_decorator_factory()
def find_note_by_title(args, book):
    """Finds a note by title."""
    if len(args) < 1:
        raise IndexError("Invalid command. Usage: find_note <title>")
    (title,) = args
    print(book.find_note_by_title(title))


@input_error_decorator_factory(message=commands_config[Commands.EDIT_NOTE])
def edit_note_text(args, book):
    """Edits a note by title."""
    if len(args) < 2:
        raise IndexError("Invalid command. Usage: edit_note <title> <text>")
    title, *new_text = args
    fixed_text = " ".join(new_text)
    print(book.edit_note_text(title, fixed_text))


@input_error_decorator_factory()
def delete_note_by_title(args, book):
    """Deletes a note by title."""
    if len(args) < 1:
        raise IndexError("Invalid command. Usage: delete_note <title>")
    (title,) = args
    print(book.delete_note_by_title(title))


def show_notes(book):
    """Shows all notes in the address book."""
    if len(book.notes) > 0:
        for note in book.notes.values():
            print("-----------------------")
            print(note)
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
    found_notes = book.find_notes_by_tags(tags)
    if found_notes:
        for note in found_notes:
            print("-----------------------")
            print(note)
    else:
        print("No notes found with the provided tags.")
