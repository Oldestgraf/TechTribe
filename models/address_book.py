import datetime
from collections import UserDict

from .fields import Name, Email
from .record import Record


class AddressBook(UserDict):
    def add_record(self, record: Record):
        if record.name in self.data:
            raise ValueError(f"Contact {record.name} already exists.")

        self.data[record.name] = record

    def find(self, name: str):
        name = Name(name)

        if name not in self.data:
            raise ValueError(f"Contact is not exist: {name}")

        return self.data[name]

    def delete(self, name: str):
        name = Name(name)

        if name in self.data:
            del self.data[name]

    def get_upcoming_birthdays(self, upcoming_days = 7):
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
    def add_email(self, name, email):
        name = Name(name)
        if name in self.data:
            record = self.data[name]
            if isinstance(email, Email):
                record.email = email
            else:
                raise ValueError("Invalid email format")
        else:
            raise ValueError(f"Contact {name} does not exist")

    def search_by_email(self, email):
        found_contacts = []
        for record in self.data.values():
            if record.email and record.email.value == email:
                found_contacts.append(record.name.value)
        return found_contacts