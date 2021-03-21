from random import choices, randrange

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(nr, repeat_word=True):
    """
    Function to generate jokes
    :param nr: int number of jokes
    :param repeat_word: bool repeat word in joke
    :return: list of jokes
    """
    result = []

    if repeat_word:
        nouns_temp = choices(nouns, k=nr)
        adverbs_temp = choices(adverbs, k=nr)
        adjectives_temp = choices(adjectives, k=nr)
    else:
        nouns_temp, adverbs_temp, adjectives_temp = [], [], []
        for i in range(nr):
            nouns_temp.append(nouns.pop(randrange(len(nouns))))
            adverbs_temp.append(adverbs.pop(randrange(len(adverbs))))
            adjectives_temp.append(adjectives.pop(randrange(len(adjectives))))

    for noun, adverb, adjective in zip(nouns_temp, adverbs_temp, adjectives_temp):
        result.append(f'{noun} {adverb} {adjective}')

    return result


print(get_jokes(2))
print(get_jokes(2, False))
print(get_jokes(2, False))
