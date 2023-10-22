import functools

def deprecated(f=None, since=None, will_be_removed=None):
    if f is None:
        return functools.partial(
            deprecated, since=since, will_be_removed=will_be_removed
        )

    message = f"Warning: function {f.__name__} is deprecated"
    if since is not None:
        message += f" since version {since}"
    if will_be_removed is not None:
        message += f". It will be removed in version {will_be_removed}"
    else:
        message += ". It will be removed in future versions"

    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        print(message)
        return f(*args, **kwargs)

    return wrapper



@deprecated
def foo():
    print("Hello from foo")


@deprecated(since="4.2.0", will_be_removed="5.0.1")
def bar():
    print("Hello from bar")


foo()
bar()