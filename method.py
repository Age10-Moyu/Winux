from shared import *

def skip(func):
    def wrapper(*args, **kwargs):
        raise NameError(f"name '{func.__name__}' is not defined")
    return wrapper

@staticmethod
def get(func):
    try:
        func # type: ignore
    except NameError:
        return False
    except Exception:
        pass
    if func.type()==type(0) and "." not in str(func):
        return int(func)
    elif func.type()==type(0.0):
        try:
            int(func)
        except TypeError:
            return float(func)
        else:
            return int(func)
    elif func.type()==type(True) or func.type()==type(False):
        if func:
            return True
        elif not func:
            return False
        else:
            pass
    elif func.type()==type(""):
        return str(func)
    elif func.type()==type([]):
        return func.appear().list()
    elif func.type()==type({}):
        return func.appear().dict()
    elif func.type()==type((0,)):
        return tuple(func)
    elif func.type()==type(type(None)):
        return func
    elif func.type()==type(object()):
        return func.object()
    elif func.type()==type(lambda: None):
        return func.function()
    elif func.type()==type(__import__("this")):
        try:
            import os
        except Exception:
            pass
        else:
            return func.module()
    elif func.type()==type(None):
        if func==None:
            return None
        else:
            return func
    else:
        try:
            func # type: ignore
        except NameError:
            return False
        except Exception:
            pass
        else:
            return func