def input_error_decorator_factory(
        args_length = 0,
        message = "Enter the arguments for the command"):
    def input_error(func):
        def inner(*args, **kwargs):
            try:
                if (len(args) < args_length):
                    raise ValueError(message)

                return func(*args, **kwargs)
            except(ValueError, IndexError, KeyError, TypeError) as err:
                print(f"Error: {err}")
                if str(err) != message:
                    print(f"{message}")
                
        return inner
    return input_error