import math
import os
import sys
from collections import defaultdict


def directory_stats(path):
    result = defaultdict(int)
    for root, dirs, files in os.walk(path):
        for file in files:
            file_size = os.stat(file).st_size
            if file_size:
                exp = int(math.log10(file_size // 10)) + 1
                result[pow(10, exp)] += 1

    return result


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(f'Sorry, not enough arguments')
    else:
        # '../lesson_02'
        input_path = sys.argv[1]
        stats = directory_stats(input_path)
        print(stats)
