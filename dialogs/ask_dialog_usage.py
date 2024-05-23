"""This module contains the function to show a button dialog."""
from prompt_toolkit.shortcuts import button_dialog

def ask_dialog_usage():
    """Show button dialog."""
    return button_dialog(
        title="Welcome to the address book bot",
        text="Do you want to enable command selection dialog?",
        buttons=[("Yes", True), ("No", False),],
    ).run()
