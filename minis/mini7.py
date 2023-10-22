def flatten(lst, depth=float("inf")):
    result = []
    for item in lst:
        if isinstance(item, list) and depth != 0:
            result.extend(flatten(item, depth - 1))
        else:
            result.append(item)
    return result


print(flatten([1, 2, [4, 5], [6, [7]], 8], depth=1))