import typing


def reverse_dictionary(dictionary):
    reverse_dict = {}

    for key, value in dictionary.items():
        if not isinstance(value, typing.Hashable):
            raise TypeError("Values must be hashable.")

        if value in reverse_dict:
            reverse_dict[value] = (reverse_dict[value], key)
        else:
            reverse_dict[value] = key

    return reverse_dict


dictionary = {("Ivanov", 1): 97832, "Petrov": 55521, ("Kuznecov", 1): 97832}
# dictionary = {"Ivanov": 97832, "Petrov": 55521, "Kuznecov": 97832}
rev_dictionary = reverse_dictionary(dictionary)
print(rev_dictionary)
