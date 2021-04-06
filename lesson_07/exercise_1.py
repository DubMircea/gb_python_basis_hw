import os

structure_dict = {
    'my_project': {
        'settings',
        'mainapp',
        'adminapp',
        'authapp'
    }
}


def create_structure(project_structure):
    for roo_dir, dirs in project_structure.items():
        for child_dir in dirs:
            path = os.path.join(roo_dir, child_dir)
            if not os.path.exists(path):
                os.makedirs(path)


create_structure(structure_dict)
