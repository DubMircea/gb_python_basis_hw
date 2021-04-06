import math
import os
import sys
from collections import defaultdict


def directory_stats(path):
    result = defaultdict(tuple)
    for root, dirs, files in os.walk(path):
        for file in files:
            file_size = os.stat(file).st_size
            ext = file.rsplit('.', maxsplit=1)[-1].lower()
            if file_size:
                exp = int(math.log10(file_size // 10)) + 1
                if not result[pow(10, exp)]:
                    result[pow(10, exp)] = (1, [ext])
                else:
                    val = result[pow(10, exp)][0]
                    extensions = result[pow(10, exp)][1]
                    if ext not in extensions:
                        extensions.append(ext)
                    result[pow(10, exp)] = (val + 1, extensions)

    return result


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(f'Sorry, not enough arguments')
    else:
        # '../lesson_02'
        input_path = sys.argv[1]
        stats = directory_stats(input_path)
        print(stats)
