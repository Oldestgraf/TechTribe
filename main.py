"""Main module of the program."""

import pickle
import handlers
from models import Commands, AddressBook

def save_data(book: AddressBook, filename="addressbook.pkl"):
    """Saves the address book to a file."""
    with open(filename, "wb") as f:
        pickle.dump(book, f)

def load_data(filename="addressbook.pkl"):
    """Loads the address book from a file."""
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook()

def parse_input(user_input: str):
    """Parses user input."""
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def main():
    """Main function of the program."""
    print("Welcome to the assistant bot!")
    try:
        book = load_data()

        while True:
            user_input = input("Enter a command: ")
            command, *args = parse_input(user_input)

            # Check if command is valid
            if not Commands.is_valid(command):
                print(f"Invalid command. {command} is not found.")
                print(f"Existed commands: {Commands.get_commands()}")
                continue

            if command == Commands.HELLO.value:
                handlers.say_greeting()

            elif command == Commands.ADD.value:
                handlers.add_contact(*args, book)

            elif command == Commands.CHANGE.value:
                handlers.change_contact(*args, book)

            elif command == Commands.PHONE.value:
                name = args[0]
                handlers.show_phone(name, book)

            elif command == Commands.ALL.value:
                handlers.show_all(book)

            elif command == Commands.ADD_BIRTHDAY.value:
                handlers.add_birthday(*args, book)

            elif command == Commands.SHOW_CONTACT.value:
                handlers.show_contact(*args, book)

            elif command == Commands.FIND_CONTACTS.value:
                handlers.find_contacts(book, args)

            elif command == Commands.SHOW_BIRTHDAY.value:
                handlers.show_birthday(*args, book)

            elif command == Commands.BIRTHDAYS.value:
                handlers.birthdays(book, *args)

            elif command in [Commands.EXIT.value, Commands.CLOSE.value]:
                print("Goodbye!")
                break

            else:
                print("Invalid command.")

    except(ValueError, IndexError, KeyError) as err:
                print(f"Error: {err}")

    except(KeyboardInterrupt):
                print("Goodbye!")

    finally:
        save_data(book)

if __name__ == "__main__":
    main()