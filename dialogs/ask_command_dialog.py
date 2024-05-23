"""
This module contains the function that asks the user to select a command and enter arguments.
"""

from prompt_toolkit.formatted_text import HTML
from prompt_toolkit.shortcuts import radiolist_dialog
from prompt_toolkit import prompt

from dialogs.print_text import print_text
from models import Commands, commands_config, Colors, prompt_style

def ask_command() -> tuple[str, list[str]]:
    """Asks user to select a command and enter arguments."""

    values = []
    for command, config in commands_config.items():
        values.append((command, HTML(f"<b>{command}</b>: {config.description}")))

    selected_command: Commands = radiolist_dialog(
        values=values,
        title="Command selection dialog",
        text="Please select a command:",
        cancel_text="Exit",
    ).run()

    if not selected_command:
        return Commands.EXIT.value, None

    print_text(f"Selected command: {selected_command}\n", Colors.INFO)

    if not commands_config[selected_command].hasParams:
        return selected_command.value, []

    message = f"{commands_config[selected_command].ask_args_message or "Enter arguments"}\n"
    answer = prompt([(
                             "",
                             message
                             )]
        , style=prompt_style)
    arguments = answer.split()
    result = (selected_command.value, arguments)

    return result
