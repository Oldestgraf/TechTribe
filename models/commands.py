"""This module contains the Commands Enum class which is used to define the commands that the user can use in the application."""

from enum import Enum

class Commands(Enum):
    """Enum class for the commands that the user can use in the application."""
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

class CommandConfigItem:
    """Class for the commands configuration."""
    def __init__(self, description: str, hasParams: bool, usage_message: str, ask_args_message: str = None):
        self.description = description
        self.hasParams = hasParams
        self.usage_message = usage_message
        self.ask_args_message = ask_args_message

    def __str__(self):
        return f"{self.description} Usage: {self.usage_message}"

    def __repr__(self):
        return f"{self.description} Usage: {self.usage_message}"

commands_config = {
    Commands.ADD: CommandConfigItem(
        description="Add new contact to contacts.",
        hasParams=True,
        usage_message="add <name>, <phone>",
        ask_args_message="Enter name and phone"
    ),
    Commands.ADD_BIRTHDAY: CommandConfigItem(
        description="Add birthday date to existed contact.",
        hasParams=True,
        usage_message="add_birthday <name> <birthday> (dd.mm.yyyy)",
        ask_args_message="Enter name and birthday (dd.mm.yyyy)"
    ),
    Commands.ADD_ADDRESS: CommandConfigItem(
        description="Add an address to a contact.",
        hasParams=True,
        usage_message="add_address <name> <street> <city> <postal_code> <country>",
        ask_args_message="Enter name, street, city, postal code and country"),
    Commands.EDIT_ADDRESS: CommandConfigItem(
        description="Edit the address of a contact.",
        hasParams=True,
        usage_message="edit_address <name> <street> <city> <postal_code> <country>",
        ask_args_message="Enter name, street, city, postal code and country"),
    Commands.SHOW_CONTACT: CommandConfigItem(
        description="Show contact by name.",
        hasParams=True,
        usage_message="show_contact <name>",
        ask_args_message="Enter name"),
    Commands.FIND_CONTACTS: CommandConfigItem(
        description="Find contacts by name, phone, birthday.",
        hasParams=True,
        usage_message="find_contacts <query> <queryN>",
        ask_args_message="Enter search query (query1, query2, ...)"),
    Commands.SHOW_BIRTHDAY: CommandConfigItem(
        description="Show birthday for selected contact.",
        hasParams=True,
        usage_message="show_birthday <name>",
        ask_args_message="Enter name"),
    Commands.BIRTHDAYS: CommandConfigItem(
        description="Show all upcoming birthdays in next 7 days.",
        hasParams=False,
        usage_message="birthdays",
        ask_args_message="Enter upcoming days"),
    Commands.CHANGE: CommandConfigItem(
        description="Change phone number for existed contact.",
        hasParams=True,
        usage_message="change <name> <phone> <new_phone>",
        ask_args_message="Enter name, phone and new phone"),
    Commands.PHONE: CommandConfigItem(
        description="Show phone number(s) for selected contact.",
        hasParams=True,
        usage_message="phone <name>",
        ask_args_message="Enter name"),
    Commands.ALL: CommandConfigItem(
        description="Show all existed contacts with data",
        hasParams=False,
        usage_message="all",
        ask_args_message=None),
    Commands.ADD_NOTE: CommandConfigItem(
        description="Add new note to notes.",
        hasParams=True,
        usage_message="add_note <title>, <note>",
        ask_args_message="Enter title and note"),
    Commands.FIND_NOTE: CommandConfigItem(
        description="Search note by title.",
        hasParams=True,
        usage_message="find_note <title>",
        ask_args_message="Enter title"),
    Commands.EDIT_NOTE: CommandConfigItem(
        description="Edit note by title.",
        hasParams=True,
        usage_message="edit_note <title>, <note>",
        ask_args_message="Enter title and note"),
    Commands.DELETE_NOTE: CommandConfigItem(
        description="Delete note by title.",
        hasParams=True,
        usage_message="delete_note <title>",
        ask_args_message="Enter title"),
    Commands.HELP: CommandConfigItem(
        description="Show info about existed command for the bot",
        hasParams=False,
        usage_message="help",
        ask_args_message=None), 
}

class CommandsDescription(Enum):
    """Enum class for the commands that the user can use in the application."""
    HELLO = "'hello' - It's a pleasure to hear it!"
    ADD = "'add' - Add new contact to contacts. Usage: add <name>, <phone>"
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
