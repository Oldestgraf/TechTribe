"""This module contains the Commands Enum class which is used to define the commands that the user can use in the application."""

from enum import Enum

class Commands(Enum):
    """Enum class for the commands that the user can use in the application."""
    HELLO = "hello"
    ADD = "add"
    ADD_BIRTHDAY = "add_birthday"
    SHOW_CONTACT = "show_contact"
    FIND_CONTACTS = "find_contacts"
    SHOW_BIRTHDAY = "show_birthday"
    BIRTHDAYS = "birthdays"
    CHANGE = "change"
    PHONE = "phone"
    ALL = "all"
    EXIT = "exit"
    CLOSE = "close"
    ADD_ADDRESS = "add_address"
    EDIT_ADDRESS = "edit_address"
    HELP = "help"
    ADD_NOTE = "add_note"
    FIND_NOTE = "find_note"
    EDIT_NOTE = "edit_note"
    DELETE_NOTE = "delete_note"

    def __str__(self):
        return self.value

    @classmethod
    def get_commands(cls):
        """Returns a list of all the commands."""
        return [str(command) for command in cls]

    @classmethod
    def is_valid(cls, command: str):
        """Checks if the given command is valid."""
        return command in cls.get_commands()

class CommandsDescription(Enum):
    """Enum class for the commands that the user can use in the application."""
    HELLO = "'hello' - It's a pleasure to hear it!"
    ADD = "'add' - Add new contact to contacts. Usage: add <name>, <phone> (can be added several phone numbers)"
    ADD_BIRTHDAY = "'add_birthday' - Add bithday date to existed contact. Usage: add_birthday <name> <birthday> (dd.mm.yyyy)"
    SHOW_BIRTHDAY = "'show_birthday' - Show birthday for selected contact. Usage: show_birthday <name>"
    BIRTHDAYS = "'birthdays' - Show all upcoming birthdays in next 7 days."
    CHANGE = "'change' - Change phone number for existed contact. Usage: change <name> <phone> <new_phone>"
    PHONE = "'phone' - Show phone number(s) for selected contact. Usage: phone <name>"
    ALL = "'all' - Show all existed contacts with data"
    ADD_NOTE = "'add_note' - Add new note to notes. Usage: add_note <title>, <note>"
    FIND_NOTE = "'find_note' - Searh note by title. Usage: find_note <title>"
    EDIT_NOTE = "'edit_note' - Edit note by title. Usage: edit_note <title>, <note>"
    DELETE_NOTE = "'delete_note' - Delete note by title. Usage: find_note <title>"
    EXIT = "'exit' - Save data and close the bot"
    CLOSE = "'close' - Save data and close the bot"
    HELP = "'help' - Show info about existed command for the bot"

    def __str__(self):
        return self.value

    @classmethod
    def get_commands_description(cls):
        """Returns a list of all existed commands."""
        return [str(command) for command in cls]
