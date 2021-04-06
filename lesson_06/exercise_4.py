import pickle
from itertools import zip_longest


def users_hobbies():
    users = []
    hobbies = []
    with open('users.csv', 'r', encoding='utf-8') as users_file:
        line = users_file.readline()
        while line:
            users.append(tuple(line.replace('\n', '').split(',')))
            line = users_file.readline()

    with open('hobby.csv', 'r', encoding='utf-8') as hobby_file:
        line = hobby_file.readline()
        while line:
            hobbies.append(tuple(line.replace('\n', '').split(',')))
            line = hobby_file.readline()

    if len(hobbies) > len(users):
        return 1

    users_hobbies_dict = dict(zip_longest(users, hobbies, fillvalue=None))
    print('Before saving')
    print(users_hobbies_dict)
    with open('users_hobbies.pickle', 'wb') as pickle_file:
        pickle.dump(users_hobbies_dict, pickle_file)

    with open('users_hobbies.pickle', 'rb') as pickle_file:
        users_hobbies_dict_from_file = pickle.load(pickle_file)

    print('From file')
    print(users_hobbies_dict_from_file)


if __name__ == '__main__':
    users_hobbies()
