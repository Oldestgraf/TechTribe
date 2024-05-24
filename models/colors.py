"""Colors enum class."""
from enum import Enum
from prompt_toolkit.styles import Style

class Colors(Enum):
    """Colors enum class."""
    SUCCESS = "ansibrightgreen"
    ERROR = "ansired"
    INFO = "ansiyellow"
    PRIMARY = "ansiwhite"
    WARNING = "ansibrightred"

prompt_style = Style.from_dict(
    {
        # Default style.
        "": Colors.PRIMARY.value,
    }
)
