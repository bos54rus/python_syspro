import itertools

def chain(*iterables):
    for it in iterables:
        yield from it

my_list = [42, 13, 7]
result = list(itertools.chain([1, 2, 3], ['a', 'b'], my_list))
print(result)
