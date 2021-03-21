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


def num_translate(number_str):
    """
    Function return  translation of digits from english to russian
    :param number_str: str / english word digit
    :return: str / russian word digit
    """
    return translations.get(number_str)


print(num_translate('seven'))
