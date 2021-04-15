import re


def email_parse(email_str):
    regex = re.compile(r'(\w+)@(\w+\.\w{2,})')

    match = regex.match(email_str)
    if match:
        groups = match.groups()
        result = {'username': groups[0], 'domain': groups[1]}
    else:
        raise ValueError(f'wrong email: {email_str}')

    return result


# test_str = 'someone@geekbrains.ru'
test_str = 'someone@geekbrainsru'
print(email_parse(test_str))
