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
    ADD_EMAIL = "add_email"
    REMOVE_EMAIL = "remove_email"
    CHANGE_EMAIL = "edit_email"
    ADD_ADDRESS = "add_address"
    EDIT_ADDRESS = "edit_address"
    DELETE_ADDRESS = "delete_address"
    SEARCH_BY_EMAIL = "search_by_email"
    HELP = "help"
    ADD_NOTE = "add_note"
    FIND_NOTE = "find_note"
    EDIT_NOTE = "edit_note"
    DELETE_NOTE = "delete_note"
    SHOW_NOTES = "show_notes"
    ADD_TAGS = "add_tags"
    REMOVE_TAGS = "remove_tags"
    FIND_BY_TAGS = "find_by_tags"
    DELETE = "delete"
    DELETE_ALL = "delete_all"

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
        ask_args_message="Enter name and phone"),
    Commands.ADD_BIRTHDAY: CommandConfigItem(
        description="Add birthday date to existed contact.",
        hasParams=True,
        usage_message="add_birthday <name> <birthday> (dd.mm.yyyy)",
        ask_args_message="Enter name and birthday (dd.mm.yyyy)"),
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
    Commands.DELETE_ADDRESS: CommandConfigItem(
        description="Delete the address of a contact.",
        hasParams=True,
        usage_message="delete_address <name>",
        ask_args_message="Enter name"),
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
    Commands.SHOW_NOTES: CommandConfigItem(
        description="Show all notes.",
        hasParams=False,
        usage_message="show_notes",
        ask_args_message=None),
    Commands.DELETE_NOTE: CommandConfigItem(
        description="Delete note by title.",
        hasParams=True,
        usage_message="delete_note <title>",
        ask_args_message="Enter title"),
    Commands.ADD_TAGS: CommandConfigItem(
        description="Add many tags to note.",
        hasParams=True,
        usage_message="add_tags <title> <tag1> <tag2> <tag3>",
        ask_args_message="Enter title and tag(s)"),
    Commands.REMOVE_TAGS: CommandConfigItem(
        description="Remove many tags from note.",
        hasParams=True,
        usage_message="remove_tags <title> <tag1> <tag2> <tag3>",
        ask_args_message="Enter title tag(s)"),
    Commands.FIND_BY_TAGS: CommandConfigItem(
        description="Find note by tag.",
        hasParams=True,
        usage_message="find_by_tags <tag1> <tag2> <tag3>",
        ask_args_message="Enter tag(s)"),
    Commands.HELP: CommandConfigItem(
        description="Show info about existed command for the bot",
        hasParams=False,
        usage_message="help",
        ask_args_message=None),
     Commands.ADD_EMAIL: CommandConfigItem(
        description="Add email to contact.",
        hasParams=True,
        usage_message="add_email <name> <email>",
        ask_args_message="Enter name and email"
    ),
    Commands.CHANGE_EMAIL: CommandConfigItem(
        description="Change email by contact.",
        hasParams=True,
        usage_message="edit_email <email> <new_email>",
        ask_args_message="Enter email and new email"
),
    Commands.REMOVE_EMAIL: CommandConfigItem(
        description="Remove email from contact.",
        hasParams=True,
        usage_message="remove_email <name> <email>",
        ask_args_message="Enter name and email"
    ),
    Commands.SEARCH_BY_EMAIL: CommandConfigItem(
        description="Search contacts by email.",
        hasParams=True,
        usage_message="search_by_email <email>",
        ask_args_message="Enter email"
    ),
    Commands.DELETE: CommandConfigItem(
        description="Delete a contact by name.",
        hasParams=True,
        usage_message="delete <name>",
        ask_args_message="Enter name"
    ),
    Commands.DELETE_ALL: CommandConfigItem(
        description="Delete all contacts.",
        hasParams=False,
        usage_message="delete_all",
        ask_args_message=None
    ),
}

class CommandsDescription(Enum):
    """Enum class for the commands that the user can use in the application."""
    ADD = "'add' - Add new contact to contacts. Usage: add <name>, <phone>"
    ADD_BIRTHDAY = "'add_birthday' - Add a bithday date to existed contact. Usage: add_birthday <name> <birthday> (dd.mm.yyyy)"
    SHOW_BIRTHDAY = "'show_birthday' - Show a birthday for selected contact. Usage: show_birthday <name>"
    BIRTHDAYS = "'birthdays' - Show all upcoming birthdays in next 7 days."
    ADD_ADDRESS = "'add_address' - Add an address to selected contact. Usage: add_address <name> <street> <city> <postal_code> <country>"
    EDIT_ADDRESS = "'edit_address' - Edit an address for selected contact. Usage: edit_address <name> <street> <city> <postal_code> <country> "
    DELETE_ADDRESS = "'delete_address' - Delete the address of a contact. Usage: delete_address <name>"
    CHANGE = "'change' - Change a phone number for existed contact. Usage: change <name> <phone> <new_phone>"
    PHONE = "'phone' - Show a phone number(s) for selected contact. Usage: phone <name>"
    ALL = "'all' - Show all existed contacts with data"
    ADD_NOTE = "'add_note' - Add a new note to notes. Usage: add_note <title> <note>"
    FIND_NOTE = "'find_note' - Searh a note by title. Usage: find_note <title>"
    EDIT_NOTE = "'edit_note' - Edit a note by title. Usage: edit_note <title> <note>"
    DELETE_NOTE = "'delete_note' - Delete a note by title. Usage: find_note <title>"
    SHOW_NOTES = "'show_notes' - Show all notes that were saved. Usage: show_notes"
    EXIT = "'exit' - Save data and close the bot"
    CLOSE = "'close' - Save data and close the bot"
    HELP = "'help' - Show info about existed command for the bot"
    ADD_TAGS = "'add_tags' - Add many tags to note. Usage: add_tags <title> <tag1> <tag2> <tag3>"
    REMOVE_TAGS = "'remove_tags' - Removes tags from note. Usage: remove_tags <title> <tag1> <tag2> <tag3>"
    FIND_BY_TAGS = "'find_by_tags' - Show notes with mentioned tags. Usage: find_by_tags <tag1> <tag2> <tag3>"
    ADD_EMAIL = "'add_email' - Add email to contact. Usage: add_email <name> <email>"
    CHANGE_EMAIL = "'change_email' - Change email for existed contact. Usage: change_email <name> <email> <new_email>"
    REMOVE_EMAIL = "'remove_email' - Remove email from contact. Usage: remove_email <name> <email>"
    SEARCH_BY_EMAIL = "'search_by_email' - Search contacts by email. Usage: search_by_email <email>"
    DELETE = "'delete' - Delete a contact by name. Usage: delete <name>"
    DELETE_ALL = "'delete_all' - Delete all contacts. Usage: delete_all"

    def __str__(self):
        return self.value

    @classmethod
    def get_commands_description(cls):
        """Returns a list of all existed commands."""
        return [str(command) for command in cls]
