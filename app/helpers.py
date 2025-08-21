import os

import os

def get_weapon_list():
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_file = os.path.join(project_root, "data", "weapon_list.txt")
    with open(data_file, mode="r", encoding="utf-8") as weapon_list:
        return weapon_list.read().split()
