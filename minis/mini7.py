def flatten(lst, depth=None):
    result = []
    for item in lst:
        if depth is None or depth > 0:
            if isinstance(item, list):
                result.extend(flatten(item, depth=None if depth is None else depth - 1))
            else:
                result.append(item)
        else:
            result.append(item)
    return result
print(flatten([1, 2, [4, 5], [6, [7]], 8], depth=1))