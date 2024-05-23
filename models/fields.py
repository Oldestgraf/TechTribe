"""Main module for fields."""

import re
import datetime
from .field import Field

class Name(Field):
    """Class representing Name."""
    def __init__(self, name: str):
        super().__init__(name)


class Phone(Field):
    """Class representing Phone."""
    pattern = r"[+\d]"
    country_code = "38"

    def __init__(self, phone_number: str):
        phone_number = "".join(re.findall(self.pattern, phone_number))

        if not phone_number.startswith("+"):
            phone_number = re.sub(fr"^({self.country_code})?", f"+{self.country_code}", phone_number)

        if len(phone_number) != 13:
            raise ValueError(f"Invalid phone number: {phone_number}")

        super().__init__(phone_number)

class Birthday(Field):
    """Class representing Birthday."""
    def __init__(self, value):
        try:
            if not re.match(r"\d{2}\.\d{2}\.\d{4}", value):
                raise ValueError("Invalid date format. Use DD.MM.YYYY")
            value = datetime.datetime.strptime(value, "%d.%m.%Y")
            if value > datetime.datetime.now():
                raise ValueError("Invalid date. Birthday can't be in the future.")
            super().__init__(value)
        except ValueError as e:
            raise ValueError(e) from e

    def __str__(self) -> str:
        return str(self.value.strftime("%d.%m.%Y"))

class Address(Field):
    """Class representing an Address."""

    def __init__(self, street: str, city: str, postal_code: str, country: str):
        self.street = street
        self.city = city
        self.postal_code = postal_code
        self.country = country
        value = f"{street}, {city}, {postal_code}, {country}"
        super().__init__(value)

    def __str__(self) -> str:
        return self.value

    def __eq__(self, other) -> bool:
        if not isinstance(other, Address):
            return False
        return (self.street, self.city, self.postal_code, self.country) == (other.street, other.city, other.postal_code, other.country)

    def __hash__(self):
        return hash((self.street, self.city, self.postal_code, self.country))

class Note:
    def __init__(self, title, text, tags=None):
        self.title = title
        self.text = text
        self.tags = tags if tags is not None else []

    def __str__(self):
        return f"Title: {self.title}\nText: {self.text}\nTags: {self.tags}"

    def add_tags(self, tag):
        self.tags.append(tag)

    def remove_tags(self, tags):
        for tag in tags:
            if tag in self.tags:
                self.tags.remove(tag)

