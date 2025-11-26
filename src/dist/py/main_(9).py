"""
Simple assistant bot for managing contacts.

Commands:
- hello: Greets the user
- add: Adds a new contact
- change: Changes an existing contact
- phone: Shows phone number of a contact
- all: Shows all contacts
- close / exit: Exits the program
"""

from helpers import (
    parse_input,
    add_contact,
    change_contact,
    show_phone,
    show_all,
)


def main():
    """Main function to run the assistant bot."""
    print("Welcome to the assistant bot!")
    contacts = {}

    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        match command:
            case "hello":
                print("How can I help you?")
            case "add":
                print(add_contact(args, contacts))
            case "change":
                print(change_contact(args, contacts))
            case "phone":
                print(show_phone(args, contacts))
            case "all":
                print(show_all(contacts))
            case "close" | "exit":
                print("Good bye!")
                break
            case _:
                print("Invalid command")


if __name__ == "__main__":
    main()
