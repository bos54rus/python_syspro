import itertools

def take(iterable, n):
    return list(itertools.islice(iterable, n))

def cycle(iterable):
    while True:
        for element in iterable:
            yield element

result = take(cycle([1, 2, 3]), 10)
print(result)
