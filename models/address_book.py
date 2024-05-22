"""AddressBook module."""

import datetime
from collections import UserDict

from .fields import Name, Note
from .record import Record

class AddressBook(UserDict):
    """Class representing an address book."""

    def __init__(self, contacts=None, notes=None):
        super().__init__()
        self.notes = notes if notes else {}
        if contacts:
            self.data.update(contacts)

    def add_record(self, record: Record):
        """Adds a record to the address book."""
        if record.name in self.data:
            raise ValueError(f"Contact {record.name} already exists.")

        self.data[record.name] = record

    def find(self, name: str, raise_error: bool = True) -> Record | None:
        """Finds a record in the address book."""
        name = Name(name)

        if name not in self.data:
            if raise_error:
                raise ValueError(f"Contact is not exist: {name}")
            return None

        return self.data[name]

    def delete(self, name: str):
        """Deletes a record from the address book."""
        name = Name(name)

        if name in self.data:
            del self.data[name]

    def get_upcoming_birthdays(self, upcoming_days = 7):
        """Returns upcoming birthdays."""
        today = datetime.date.today()
        upcoming_birthdays = []
        upcoming_date = today + datetime.timedelta(upcoming_days)

        for user in self.data.values():
            if not user.birthday:
                continue
            birthday = user.birthday.value
            birthday_this_year = datetime.date(today.year, birthday.month, birthday.day)
            # 7 days including today is 6 days from today
            if today <= birthday_this_year <= upcoming_date:
                congratulation_date = birthday_this_year
                if birthday_this_year.weekday() in (5, 6):
                    congratulation_date = birthday_this_year + \
                        datetime.timedelta(days = 7 - birthday_this_year.weekday())

                upcoming_birthdays.append(
                    {
                        'name': user.name.value,
                        'congratulation_date': congratulation_date.strftime("%d.%m.%Y"),
                    }
                )


        sorted_upcoming_birthdays = sorted(upcoming_birthdays, key=lambda x: x["congratulation_date"])
        return sorted_upcoming_birthdays

    def add_note(self, title, text):
        if title in self.notes:
            raise ValueError("Note title already exists. Please use a unique title.")
        else:
            self.notes[title] = Note(title, text)
            return "Note added successfully."

    def find_note_by_title(self, title):
        note = self.notes.get(title)
        if note:
            return note
        else:
            return "Note not found."

    def edit_note_text(self, title, new_text):
        if title in self.notes:
            self.notes[title].text = new_text
            return "Note edited successfully."
        else:
            return "Note not found."

    def delete_note_by_title(self, title):
        if title in self.notes:
            del self.notes[title]
            return "Note deleted successfully."
        else:
            return "Note not found."
