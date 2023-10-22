def specialize(f, *args, **kwargs):
    def partial_func(*more_args, **more_kwargs):
        return f(*args, *more_args, **kwargs, **more_kwargs)

    return partial_func


def sum(x, y):
    return x + y


plus_one = specialize(sum, y=1)
just_two = specialize(sum, 1, 1)

print(plus_one(10))
print(just_two())
