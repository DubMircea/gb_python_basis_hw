def file_logs_parser():
    result = []
    with open('nginx_logs.txt', 'r', encoding='utf-8') as log_file:
        line = log_file.readline()
        while line:
            line = line.replace('"', '').replace('-', '')
            elements = line.split()
            result.append((elements[0], elements[3], elements[4]))
            line = log_file.readline()

    return result


if __name__ == '__main__':
    logs = file_logs_parser()
    print(logs)
