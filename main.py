"""Main module of the program."""
import pickle
from prompt_toolkit import prompt
import handlers
from dialogs import ask_command, ask_dialog_usage, print_text
from models import Commands, AddressBook, Colors

def save_data(book, filename="addressbook.pkl"):
    """Saves the address book to a file."""
    with open(filename, "wb") as f:
        pickle.dump(book, f)

def load_data(filename="addressbook.pkl"):
    """Loads the address book from a file."""
    try:
        with open(filename, "rb") as f:
            data = pickle.load(f)
            contacts = data.get("contacts", {})
            notes = data.get("notes", {})
            book = AddressBook(contacts, notes)
            return book
    except FileNotFoundError:
        return AddressBook()

def parse_input(user_input: str):
    """Parses user input."""
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def main():
    """Main function of the program."""

    book = load_data()
    if book is None:
        book = AddressBook()

    dialog_selection_enabled = ask_dialog_usage()

    try:
        while True:
            if dialog_selection_enabled:
                command, args = ask_command()
            else:
                user_input = prompt("Enter command: ")
                command, *args = parse_input(user_input)

            # Check if command is valid
            if not Commands.is_valid(command):
                print(f"Invalid command. {command} is not found.")
                print(f"Existed commands: {Commands.get_commands()}")
                continue


            elif command == Commands.ADD.value:
                handlers.add_contact(*args, book)

            elif command == Commands.CHANGE.value:
                handlers.change_contact(*args, book)

            elif command == Commands.PHONE.value:
                handlers.show_phone(*args, book)

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

            elif command == Commands.HELP.value:
                handlers.help_info()

            elif command == Commands.ADD_NOTE.value:
                handlers.add_note(args, book)

            elif command == Commands.FIND_NOTE.value:
                handlers.find_note_by_title(args, book)

            elif command == Commands.EDIT_NOTE.value:
                handlers.edit_note_text(args, book)

            elif command == Commands.DELETE_NOTE.value:
                handlers.delete_note_by_title(args, book)

            elif command == Commands.SHOW_NOTES.value:
                handlers.show_notes(book)

            elif command == Commands.ADD_TAGS.value:
                handlers.add_tags_to_note(args, book)

            elif command == Commands.REMOVE_TAGS.value:
                handlers.remove_tags_from_note(args, book)

            elif command == Commands.FIND_BY_TAGS.value:
                handlers.find_notes_by_tags(args, book)

            elif command == Commands.ADD_ADDRESS.value:
                handlers.add_address(*args, book)

            elif command == Commands.EDIT_ADDRESS.value:
                handlers.edit_address(*args, book)

            elif command in [Commands.EXIT.value, Commands.CLOSE.value]:
                print_text("Goodbye!", Colors.SUCCESS)
                break

            else:
                print_text("Invalid command.", Colors.ERROR)

            if dialog_selection_enabled:
                print_text("Press Enter when you are ready to continue...", Colors.INFO)
                prompt()

    except(ValueError, IndexError, KeyError) as err:
        print(f"Error: {err}")

    except(KeyboardInterrupt):
        print("Goodbye!")

    finally:
        save_data({"contacts": book.data, "notes": book.notes}, "addressbook.pkl")

if __name__ == "__main__":
    main()
