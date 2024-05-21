import re
import datetime
from .field import Field

class Name(Field):
    def __init__(self, name: str):
        super().__init__(name)


class Phone(Field):
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
    def __init__(self, value):
        try:
            if not re.match(r"\d{2}\.\d{2}\.\d{4}", value):
                raise ValueError("Invalid date format. Use DD.MM.YYYY")
            value = datetime.datetime.strptime(value, "%d.%m.%Y")
            print(value)
            if value > datetime.datetime.now():
                raise ValueError("Invalid date. Birthday can't be in the future.")
            super().__init__(value)
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")