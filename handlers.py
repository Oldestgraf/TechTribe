import re
from models import AddressBook, Record
from decorator import input_error_decorator_factory

contacts = {}

def say_greeting():
    print("How can I help you?")        

@input_error_decorator_factory(args_length = 3, message = "Invalid command. Usage: add <name> <phone>")
def add_contact(name: str, phone: str, book: AddressBook) -> None:
    record = Record(name)
    added_phone = record.add_phone(phone)
    book.add_record(record)
    print(f"Contact added. \n Name: {name} \n Phone: {added_phone}")

@input_error_decorator_factory(args_length = 3, message = "Invalid command. Usage: change <name> <phone> <new_phone")
def change_contact(name: str, phone: str, new_phone:str, book: AddressBook) -> None:
    record = book.find(name)
    record.edit_phone(phone, new_phone)

    print(f"Contact updated. \n Old: {phone} \n New: {new_phone}")

@input_error_decorator_factory(args_length = 2, message = "Invalid command. Usage: phone <name>")
def show_phone(name: str, book: AddressBook) -> str:
    record = book.find(name)
    print(f"Contact: {record.name}")
    for phone in record.phones:
        print(phone)

def show_all(book) -> dict:
    for name, record in book.data.items():
        print(record)

@input_error_decorator_factory(args_length = 3, message = "Invalid command. Usage: add_birthday <name> <birthday>")
def add_birthday(name: str, birthday: str, book: AddressBook):
    record = book.find(name)
    record.add_birthday(birthday)
    print("Birthday added.")

@input_error_decorator_factory(args_length = 2, message = "Invalid command. Usage: show_birthday <name>")
def show_birthday(name: str, book: AddressBook):
    record = book.find(name)
    print(record.birthday.value.strftime("%d.%m.%Y"))

@input_error_decorator_factory(message = "Invalid command. Usage: birthdays <upcoming_days>")
def birthdays(book, upcoming_days = 7):
    upcoming_birthdays = book.get_upcoming_birthdays(upcoming_days)
    if len(upcoming_birthdays) == 0:
        print("No upcoming birthdays.")
        return
    for item in upcoming_birthdays:
        print(f"{item["name"]}: {item["congratulation_date"]}")