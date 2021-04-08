import re


def file_logs_parser():
    result = []
    with open('nginx_logs.txt', 'r', encoding='utf-8') as log_file:
        # regex = re.compile(r'(\d+\.\d+\.\d+\.\d+).+\[(.+)] \"(.+) (/.+)\" (\d+) (\d+) (.+) \"(.+)\"')
        # regex = re.compile(r'(\d+\.\d+\.\d+\.\d+).+\[(.+)] \"(.+) (/.+)\" (\d+) (\d+)')
        # regex = re.compile(r'((:*[0-9a-z]*:*)+|(\d+\.\d+\.\d+\.\d+)).+\[(.+)] \"(.+) (/.+)\" (\d+) (\d+)')
        regex = re.compile(r'([0-9.]+) .+\[(.+)] \"(.+) (/.+)\" (\d+) (\d+)')
        line = log_file.readline()
        while line:
            match = regex.match(line)
            if match:
                groups = match.groups()
                result.append(groups)
            else:
                reg = re.compile(r'([0-9a-z:]+) .+\[(.+)] \"(.+) (/.+)\" (\d+) (\d+)')
                match = reg.match(line)
                if match:
                    groups = match.groups()
                    result.append(groups)
                else:
                    print(f'No match, line:{line}')
            line = log_file.readline()

    return result


def parsed_raw(raw_str):
    regex = re.compile(r'([0-9.]+) .+\[(.+)] \"(.+) (/.+)\" (\d+) (\d+)')
    match = regex.match(raw_str)
    if match:
        groups = match.groups()
        return groups
    else:
        reg = re.compile(r'([0-9a-z:]+) .+\[(.+)] \"(.+) (/.+)\" (\d+) (\d+)')
        match = reg.match(raw_str)
        if match:
            groups = match.groups()
            return groups
        else:
            print(f'No match, line:{raw_str}')


if __name__ == '__main__':
    # logs = file_logs_parser()
    raw = '188.138.60.101 - - [17/May/2015:08:05:49 +0000] "GET /downloads/product_2 HTTP/1.1" 304 0 "-" "Debian APT-HTTP/1.3 (0.9.7.9)"'
    parsed = parsed_raw(raw)
    print(parsed)
