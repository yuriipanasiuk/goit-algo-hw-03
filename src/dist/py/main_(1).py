"""
Module for managing a simple address book.

Provides classes for contact fields, individual contact records,
and an address book that stores multiple records.
"""

from collections import UserDict
import pickle
import re
from datetime import datetime, date, timedelta


class CustomValueError(ValueError):
    """Class for handle custom errors"""

    def __init__(self, message="Something went wrong"):
        self.message = message
        super().__init__(self.message)


class Field:
    """Base class for contact fields."""

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    """Class for contact name."""

    def __init__(self, value):
        if not value or not value.strip():
            raise CustomValueError("Name cannot be empty")

        super().__init__(value)


class Birthday(Field):
    """Class for user birthday"""

    def __init__(self, value):
        try:
            if isinstance(value, date):
                data_object = value
            else:
                data_object = datetime.strptime(value, "%d.%m.%Y").date()

            super().__init__(data_object)
        except ValueError:
            raise CustomValueError("Invalid date format. Use DD.MM.YYYY")


class Phone(Field):
    """Class for phone number."""

    def __init__(self, value):
        validate_value = self.validate_number(value)

        super().__init__(validate_value)

    @staticmethod
    def validate_number(phone_number):
        """Validate phone number"""

        if not phone_number or not phone_number.strip():
            raise CustomValueError("Phone number cannot be empty")

        if not re.fullmatch(r"\d{10}", phone_number):
            raise CustomValueError(
                f"Number {phone_number} is invalid. Must be exactly 10 digits."
            )

        return phone_number


class Record:
    """Class representing a single contact with a name and a list of phones."""

    def __init__(self, name=None):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_phone(self, phone_number):
        """Validate and add phone number to contact book"""

        validated_number = Phone(phone_number)
        self.phones.append(validated_number)

    def find_phone(self, phone_number):
        """Find phone number in contact book"""

        for number in self.phones:
            if number.value == phone_number:
                return number

        return None

    def remove_phone(self, phone_number):
        """Remove phone number from contact book"""

        phone = self.find_phone(phone_number)

        if phone:
            self.phones.remove(phone)

    def edit_phone(self, old_phone_number, new_phone_number):
        """Edit phone number in contact book"""

        phone_to_edit = self.find_phone(old_phone_number)

        if phone_to_edit:
            validated_new_phone = Phone(new_phone_number)
            phone_to_edit.value = validated_new_phone.value

    def add_birthday(self, data_of_birth):
        """Add birthday"""
        self.birthday = Birthday(data_of_birth)

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    """Class representing an address book, where keys are names and values are Record instances."""

    def add_record(self, record):
        """Add recort to contact book"""

        self.data[record.name.value] = record

    def find(self, name):
        """Find contact in contact book"""

        return self.data.get(name)

    def delete(self, name):
        """Delete contact from contact book"""

        if name in self.data:
            del self.data[name]

    def get_upcoming_birthdays(self):
        """Returns a list of users to be congratulated by day of the week."""

        today = datetime.today().date()
        date_format = "%d.%m.%Y"
        user_birthdays = []

        for user in self.data.values():
            if not user.birthday:
                continue

            user_birthday = user.birthday.value
            birthday_this_year = user_birthday.replace(year=today.year)

            if birthday_this_year < today:
                birthday_this_year = user_birthday.replace(year=today.year + 1)

            days_to_birthday = (birthday_this_year - today).days

            if 0 <= days_to_birthday <= 7:
                if birthday_this_year.weekday() == 5:
                    congratulation_date = birthday_this_year + timedelta(days=2)

                elif birthday_this_year.weekday() == 6:
                    congratulation_date = birthday_this_year + timedelta(days=1)

                else:
                    congratulation_date = birthday_this_year

                user_birthdays.append(
                    {
                        "name": user.name.value,
                        "birthday": user.birthday.value.strftime(date_format),
                        "congratulation_date": congratulation_date.strftime(
                            date_format
                        ),
                    }
                )

        return user_birthdays


def input_error(func):
    """
    Decorator to handle common input-related errors for functions.
    """

    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except CustomValueError as e:
            return str(e)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Enter correct name."
        except IndexError:
            return "Not enough arguments. Please provide required data."
        except AttributeError:
            return "Contact not found."

    return inner


@input_error
def parse_input(user_input: str):
    """Parse user input into a command and its arguments."""
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()

    return cmd, *args


@input_error
def add_contact(args, book: AddressBook):
    """Add contact to contact book"""
    name, phone, *_ = args
    record = book.find(name)
    message = "Contact updated."

    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."

    if phone:
        record.add_phone(phone)

    return message


@input_error
def change_contact(args, book: AddressBook):
    """Change the phone number of an existing contact."""

    name, old_phone_number, new_phone_number, *_ = args
    record = book.find(name)

    record.edit_phone(old_phone_number, new_phone_number)
    return "Contact updated."


@input_error
def show_phone(args, book: AddressBook):
    """Return the phone number of a contact."""

    name = args[0]
    record = book.find(name)
    if record:
        phones = ", ".join(p.value for p in record.phones)
        return f"{name}'s phone number is {phones}"


def show_all(book: AddressBook) -> str:
    """Return all contacts as a formatted string."""

    if not book.data:
        return "Contacts list are empty"

    result = []
    for record in book.data.values():
        phones = ", ".join(p.value for p in record.phones) or "No phones"
        birthday = (
            record.birthday.value.strftime("%d.%m.%Y")
            if record.birthday
            else "No birthday"
        )
        result.append(
            f"Contact name: {record.name.value}, phones: {phones}, birthday: {birthday}"
        )
    return "\n".join(result)


@input_error
def add_birthday(args, book: AddressBook):
    """Add birthday for user"""
    name, birthday, *_ = args
    record = book.find(name)

    if record is None:
        record = Record(name)
        book.add_record(record)

    record.add_birthday(birthday)
    return f"Birthday added for {name}."


@input_error
def show_birthday(args, book: AddressBook):
    """Show birthday function"""
    name = args[0]
    record = book.find(name)

    if record and record.birthday:
        return f"{name}'s birthday is in {record.birthday.value.strftime('%d.%m.%Y')}"

    return "Birthday not found"


@input_error
def birthdays(book: AddressBook):
    """Show upcoming birthday function"""
    upcoming = book.get_upcoming_birthdays()
    result = ""

    if not upcoming:
        return "No birthdays"

    for user_birthday in upcoming:
        result += f"name: {user_birthday['name']}, congratulate on: {user_birthday['congratulation_date']}\n"

    return result


def save_data(book, filename="addressbook.pkl"):
    """Save contacts"""
    with open(filename, "wb") as f:
        pickle.dump(book, f)


def load_data(filename="addressbook.pkl"):
    """Load contacts"""
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook()


def main():
    """Main function to run the assistant bot."""
    print("Welcome to the assistant bot!")
    book = load_data()

    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        match command:
            case "hello":
                print("How can I help you?")
            case "add":
                print(add_contact(args, book))
            case "change":
                print(change_contact(args, book))
            case "phone":
                print(show_phone(args, book))
            case "all":
                print(show_all(book))
            case "add-birthday":
                print(add_birthday(args, book))
            case "show-birthday":
                print(show_birthday(args, book))
            case "birthdays":
                print(birthdays(book))
            case "close" | "exit":
                save_data(book)
                print("Good bye!")
                break
            case _:
                print("Invalid command")


if __name__ == "__main__":
    main()
