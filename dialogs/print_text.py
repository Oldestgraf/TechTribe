"""This module contains a function to print text with color."""

from prompt_toolkit import print_formatted_text
from prompt_toolkit.formatted_text import FormattedText
from models import Colors

_print = print_formatted_text

def print_text(text: str, color: Colors = Colors.PRIMARY):
    """Prints text with color."""
    _print(FormattedText([(color.value, text)]))