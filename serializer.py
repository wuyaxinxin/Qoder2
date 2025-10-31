# 始终生效

import json
from data_model import DataModel


def save_to_file(obj, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(obj.to_dict(), f, ensure_ascii=False, indent=2)


def load_from_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return DataModel.from_dict(json.load(f))
