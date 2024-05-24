def input_error_decorator_factory(
        message = "Enter the arguments for the command"):
    """A factory for creating input error decorators."""

    def input_error(func):
        def inner(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except(ValueError, IndexError, KeyError) as err:
                print(f"Error: {err}")

            except(TypeError):
                print(f"Invalid Command: {message}")

        return inner
    return input_error