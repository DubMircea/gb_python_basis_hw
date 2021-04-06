import os

import yaml


def recursive_parse(structure_dict, prev=None):
    for root_dir, children in structure_dict.items():
        root_dirs = [root_dir] if not prev else prev + [root_dir]
        local_path = os.path.join(*root_dirs)
        if not os.path.exists(local_path):
            os.makedirs(local_path)
        if type(children) == list:
            for child in children:
                if type(child) == str:
                    local_path = os.path.join(*root_dirs, child)
                    if child.endswith('.py') or child.endswith('.html'):
                        with open(local_path, 'a+') as f:
                            pass
                elif type(child) == dict:
                    recursive_parse(child, root_dirs)
        elif type(children) == dict:
            recursive_parse(children, root_dirs)


def parse_config(path_to_file):
    with open(path_to_file) as file:
        structure = yaml.full_load(file)

    recursive_parse(structure)


def parse_config_line_by_line(path_to_file):
    result = []
    with open(path_to_file, 'r') as file:
        line = file.readline()
        line = line.replace('\n', '')
        prev_pos = 0
        keys = []
        while line:
            current_pos = len(line) - len(line.lstrip(' '))
            tmp_key = line.replace(':', '').replace('-', '').replace(' ', '')

            if current_pos == 0:
                keys.append(tmp_key)
            elif current_pos > prev_pos:
                keys.append(tmp_key)
            elif prev_pos == current_pos:
                result.append(keys[:])
                keys[-1] = tmp_key
            elif prev_pos > current_pos:
                result.append(keys[:])
                keys = keys[:int(current_pos / 2)]
                keys.append(tmp_key)

            prev_pos = current_pos

            line = file.readline()
            line = line.replace('\n', '')
            if not line:
                result.append(keys[:])

    for item in result:
        if item[-1].endswith('.py') or item[-1].endswith('.html'):
            folders_path = os.path.join(*item[:-1])
            if not os.path.exists(folders_path):
                os.makedirs(folders_path)

            file_path = os.path.join(*item)
            if not os.path.exists(file_path):
                with open(file_path, 'a+') as f:
                    pass
        else:
            folders_path = os.path.join(*item)
            if not os.path.exists(folders_path):
                os.makedirs(folders_path)


path = 'config.yaml'
# with yaml lib
# parse_config(path)
# read file line by line
parse_config_line_by_line(path)
