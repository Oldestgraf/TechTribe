# TechTribe
Final project for Python Programming: Foundations and Best Practices 2.0

## Description
A terminal application that allows users to create, read, update, and delete contacts.
Users can also view all contacts, view contact by name, and search for contacts by keyword.
Also implemented opportunity to save notes separate from contacts.
User can save, edit, delete and search note by title.
Also added opportunity to add tags to any note, delete tag and find note by tag.

## Installation
1. Clone the repository
2. Create a virtual environment in the project directory: python -m venv .venv
3. Activate the virtual environment: source .venv/bin/activate
4. Install the required packages: pip install -r requirements.txt
5. Run the application: python main.py

## Usage
Write a command in the terminal to interact with the application 
User can use the next commands:
- `add <name> <phone>` to add a new contact
- `add_birthday <name> <date>` to add a birthday to a contact
- `add_address <name> <street> <city> <postal_code> <country>` to add an address to a contact
- `edit_address <name> <street> <city> <postal_code> <country>` to edit an address for a contact
- `show_contact <name>` to show contact
- `find_contacts <query1> <aueryN>` to find contacts by multiple queries
- `show_birthday <name>` to show birthday for a contact
- `birthdays <days>` to show the upcoming birthdays in the next days, default days is `7`
- `change <name> <oldPhone> <newPhone>` to change the phone number of a contact
- `phone <name>` to show the phone numbers of a contact
- `all` to show all contacts
- `add-note <title> <text>` to add a note
- `find-note <title>` to find a note by title
- `edit_note <title> <text>` to edit a note
- `delete_note <title>` to delete a note

- `help` to show the help message
- `exit` to exit the application
- `close` to close the application

User can use check dialogs to select the action or exit.

## Authors
- [Luisa Fernanda Sosa](    )
