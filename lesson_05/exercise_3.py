tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
classes = [
    '9А', '7В', '9Б',
    # '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А',

]


def zip_function(tutors_list, classes_list):
    for i in range(len(tutors_list)):
        tutor = tutors_list[i]
        class_name = classes_list[i] if i < len(classes_list) else None

        yield tutor, class_name


zipped = zip_function(tutors, classes)
print(f'type {type(zipped)}')
print(next(zipped))
print(next(zipped))
print(next(zipped))
print(next(zipped))
print(next(zipped))
print(next(zipped))
print(next(zipped))
print(next(zipped))
