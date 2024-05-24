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
- `add_email <name> <email>` to add an email to a contact
- `edit_email <name> <oldEmail> <newEmail>` to edit an email for a contact
- `remove_email <name> <email>` to remove an email from a contact
- `show_contact <name>` to show contact
- `find_contacts <query1> <queryN>` to find contacts by multiple queries
- `show_birthday <name>` to show birthday for a contact
- `birthdays <days>` to show the upcoming birthdays in the next days, default days is `7`
- `change <name> <oldPhone> <newPhone>` to change the phone number of a contact
- `phone <name>` to show the phone numbers of a contact
- `all` to show all contacts
- `delete` to delete contact
- `delete_all` to delete all contacts
- `delete_address <name>` to delete address
- `delete_note <title>` to delete a note
- `add-note <title> <text>` to add a note
- `find-note <title>` to find a note by title
- `edit_note <title> <text>` to edit a note
- `show_notes` - to show all notes that were saved
- `add_tags` - to add many tags to note
- `remove_tags` - to remove tags from note
- `find_by_tags` - to show notes with mentioned tags
- `help` to show the help message
- `exit` to exit the application
- `close` to close the application

User can use check dialogs to select the action or exit.
