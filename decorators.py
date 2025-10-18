from functools import wraps

def input_error(func):
    @wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Enter the argument for the command"
        except KeyError:
            return "Contact not found"
        except IndexError:
            return "Enter the argument for the command"
        except AttributeError:
            return "Contact not found"
    return inner