def thesaurus(*args):
    result = {}

    for arg in args:
        result.setdefault(arg[0], [])
        result[arg[0]].append(arg)

    result = dict(sorted(result.items()))
    return result


input_data = ["Петр", "Иван", "Мария", "Илья"]
print(thesaurus("Петр", "Иван", "Мария", "Илья"))
print(thesaurus(*input_data))
