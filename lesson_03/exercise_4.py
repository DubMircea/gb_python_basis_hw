def thesaurus_adv(*args):
    result = {}

    for arg in args:
        name, surname = arg.split()
        result.setdefault(surname[0], {}).setdefault(name[0], [])
        result[surname[0]][name[0]].append(arg)

    result = dict(sorted(result.items()))
    return result


input_data = ["Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"]
print(thesaurus_adv(*input_data))
