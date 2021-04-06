src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]


# result = [23, 1, 3, 10, 4, 11]

# bad version
# def unique_numbers(lst):
#     return  (n for n in lst if lst.count(n) == 1)


def unique_numbers(lst):
    unique_nrs = set()
    tmp = set()
    for el in lst:
        if el not in tmp:
            unique_nrs.add(el)
        else:
            unique_nrs.discard(el)

        tmp.add(el)

    return (el for el in lst if el in unique_nrs)


result = unique_numbers(src)
print(next(result))
print(next(result))
print(next(result))
print(*result)
