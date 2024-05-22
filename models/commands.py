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
    ADD_NOTE = "add-note"
    FIND_NOTE = "find-note"
    EDIT_NOTE = "edit-note"
    DELETE_NOTE = "delete-note"
    ADD_ADDRESS = "add_address"
    EDIT_ADDRESS = "edit_address"

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
