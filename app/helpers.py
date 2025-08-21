import bson
import os


def get_weapon_list():
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_file = os.path.join(project_root, "data", "weapon_list.txt")
    with open(data_file, mode="r", encoding="utf-8") as weapon_list:
        return weapon_list.read().split()


def convert_bson_types(obj):
    if isinstance(obj, dict):
        return {k: convert_bson_types(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [convert_bson_types(i) for i in obj]
    elif isinstance(obj, bson.objectid.ObjectId):
        return str(obj)
    else:
        return obj