"""AddressBook module."""

import datetime
from collections import UserDict

from .fields import Name, Phone, Birthday
from .record import Record

class AddressBook(UserDict):
    """Class representing an address book."""

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

    def find_by_query(self, queries: list[str]) -> list[Record]:
        """Finds records by a search query list."""
        found = []
        for query in queries:
            found.extend(self._find_by_query(query))

        return found

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

    def _find_by_query(self, query: str) -> list[Record]:
        """Finds records by a search query."""
        found = []
        query = query.lower()

        for record in self.data.values():
            if query in record.name.value.lower():
                found.append(record)

            try:
                phone = Phone(query)
                if phone in record.phones:
                   found.append(record)
            except ValueError:
                pass

            try:
                if record.birthday:
                   birthday = Birthday(query)
                   if birthday == record.birthday:
                      found.append(record)
            except ValueError:
                pass

        return found