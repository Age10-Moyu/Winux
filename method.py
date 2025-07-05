from shared import *

def skip(func):
    def wrapper(*args, **kwargs):
        raise NameError(f"name '{func.__name__}' is not defined")
    return wrapper
