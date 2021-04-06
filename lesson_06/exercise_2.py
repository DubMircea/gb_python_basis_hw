from collections import defaultdict


def file_logs_parser():
    spammers = {}
    spammers_count = defaultdict(int)

    with open('nginx_logs.txt', 'r', encoding='utf-8') as log_file:
        line = log_file.readline()
        while line:
            line = line.replace('"', '').replace('-', '')
            elements = line.split()
            spammers[elements[0]] = (elements[0], elements[3], elements[4])
            spammers_count[elements[0]] += 1

            line = log_file.readline()

    sorted_spammers = sorted(spammers_count.items(), key=lambda item: item[1])
    spammer = spammers.get(sorted_spammers[-1][0])

    return spammer


if __name__ == '__main__':
    spammer = file_logs_parser()
    print(spammer)
