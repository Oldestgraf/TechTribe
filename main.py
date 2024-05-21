from collections import UserDict
from datetime import datetime
from dateutil.relativedelta import relativedelta
import pickle

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    pass

class Phone(Field):
    def __init__(self, value):
        if len(value) != 10 or not value.isdigit():
            raise ValueError("Phone number should has 10 digits.")
        super().__init__(value)

class Birthday(Field):
    def __init__(self, value):
        try:
            value_date = datetime.strptime(value, "%d.%m.%Y").date()
            super().__init__(value_date)
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_birthday(self, birthday):
        try:
            self.birthday = Birthday(birthday)
        except ValueError as e:
            print(e)

    def add_phone(self, phone):
        try:
            self.phones.append(Phone(phone))
        except ValueError as e:
            print(e)

    def remove_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                self.phones.remove(phone)
        print(f"Phone number {phone} isn't found")

    def edit_phone(self, old_phone, new_phone):
        for p in self.phones:
            if p.value == old_phone:
                try:
                    p.value = new_phone
                except ValueError as e:
                    print(e)

    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p.value
        return None

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}, birthday: {self.birthday}"

class AddressBook(UserDict):

    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]

    def get_upcoming_birthdays(self):
        """Celebrating birthdays in next 7 days"""

        date_now = datetime.today().date()
        birthdays = []

        for record in self.data.values():
            if record.birthday is not None:
                user_birthday = record.birthday.value

                # Calculate user birthday in current year
                current_year = date_now.year
                user_birthday_in_current_year = user_birthday.replace(year=current_year)

                # Calculate celebrating including weekends
                congratulation_day = user_birthday_in_current_year.isoweekday()
                if congratulation_day > 5:
                    if congratulation_day == 6:
                        birthday = user_birthday_in_current_year + relativedelta(days=2)
                    else: birthday = user_birthday_in_current_year + relativedelta(days=1)
                else: birthday = user_birthday_in_current_year

                # Calculate celebrating year
                if birthday < date_now:
                    congratulation_date = birthday + relativedelta(years=1)
                else: congratulation_date = birthday

                # Calculate birthdays in the next 7 days
                if date_now < congratulation_date < (date_now + relativedelta(days=7)):
                    congratulation_date_str = congratulation_date.strftime("%Y.%m.%d")
                    current_user = {"name": record.name.value}
                    current_user.update({"congratulation_date": congratulation_date_str})
                    birthdays.append(current_user)

        return birthdays

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except(IndexError, ValueError) as e:
            print("Input error:", e)
    return inner

def parse_input(user_input):
    command, *args = user_input.split()
    command = command.strip().lower()
    return command, *args


@input_error
def add_contact(args, book: AddressBook):
    name, phone, *_ = args
    record = book.find(name)
    message = "Contact updated."
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    if phone:
        record.add_phone(phone)
    return message

@input_error
def change_phone(args, book: AddressBook):
    name, old_phone, new_phone = args
    record = book.find(name)
    if record:
        record.edit_phone(old_phone, new_phone)
        return "Phone number updated."
    else:
        return "Contact not found."

@input_error
def show_phone(args, book: AddressBook):
    name, *_ = args
    record = book.find(name)
    if record:
        return "; ".join(str(phone) for phone in record.phones)
    else:
        return "Contact not found."

@input_error
def show_all(book: AddressBook):
    if book:
        return "\n".join(str(record) for record in book.values())
    else:
        return "Address book is empty."

@input_error
def add_birthday(args, book: AddressBook):
    name, birthday = args
    record = book.find(name)
    if record:
        record.add_birthday(birthday)
        return "Birthday added."
    else:
        return "Contact not found."

@input_error
def show_birthday(args, book: AddressBook):
    name, *_ = args
    record = book.find(name)
    if record and record.birthday:
        return str(record.birthday)
    else:
        return "Birthday not found."

@input_error
def birthdays(book: AddressBook):
    return book.get_upcoming_birthdays()

def save_data(book, filename="addressbook.pkl"):
    with open(filename, "wb") as f:
        pickle.dump(book, f)

def load_data(filename="addressbook.pkl"):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook()  # Return new adress book if file not found

def main():

    book = load_data()

    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, book))
        elif command == "change":
            print(change_phone(args, book))
        elif command == "phone":
            print(show_phone(args, book))
        elif command == "all":
            print(show_all(book))
        elif command == "add-birthday":
            print(add_birthday(args, book))
        elif command == "show-birthday":
            print(show_birthday(args, book))
        elif command == "birthdays":
            print(birthdays(book))
        else:
            print("Invalid command.")

    save_data(book)

if __name__ == "__main__":
    main()