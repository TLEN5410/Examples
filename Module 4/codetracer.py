import sys

def logger(func):
    def inner(*args, **kwargs):
        msg = "{0}.{1}(".format(args[0], func.__name__)
        msg += ', '.join([str(arg) for arg in args[1:]])
        msg += ")\n"
        sys.stderr.write(msg)
        return func(*args, **kwargs)
    return inner
