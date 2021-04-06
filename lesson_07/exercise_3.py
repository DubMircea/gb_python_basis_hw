import os
import shutil

root_dir = 'my_project'
look_up_folder = 'templates'


def parse_structure():
    path = os.path.join(root_dir, look_up_folder)
    if os.path.exists(path):
        shutil.rmtree(path)

    for root, dirs, files in os.walk(root_dir):
        for directory in dirs:
            if directory == look_up_folder:
                rel_path = os.path.join(root, directory)

                shutil.copytree(rel_path, path, dirs_exist_ok=True)


parse_structure()
