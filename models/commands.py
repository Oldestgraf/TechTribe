from enum import Enum

class Commands(Enum):
    HELLO = "hello"
    ADD = "add"
    ADD_BIRTHDAY = "add_birthday"
    SHOW_BIRTHDAY = "show_birthday"
    BIRTHDAYS = "birthdays"
    CHANGE = "change"
    PHONE = "phone"
    ALL = "all"
    EXIT = "exit"
    CLOSE = "close"

    def __str__(self):
        return self.value

    @classmethod
    def get_commands(cls):
        return [str(command) for command in cls]

    @classmethod
    def is_valid(cls, command: str):
        return command in cls.get_commands()