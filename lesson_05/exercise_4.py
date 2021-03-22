src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]


# result = [12, 44, 4, 10, 78, 123]


def bigger_num(lst):
    rs = []

    previous = None
    for num in lst:
        if previous is not None and num > previous:
            rs.append(num)

        previous = num

    return rs


result = bigger_num(src)
print(result)
