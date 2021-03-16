translations = {
    'zero': 'ноль',
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять',
}


def num_translate_adv(number_str):
    """
    Function return  translation of digits from english to russian
    :param number_str: str / english word digit
    :return: str / russian word digit
    """
    result = translations.get(number_str.lower())
    if result and number_str.istitle():
        return result.capitalize()

    return result


print(num_translate_adv('One'))
print(num_translate_adv('two'))
