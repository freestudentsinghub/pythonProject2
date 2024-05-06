import json
from typing import List


def transaction(filename: str) -> List[dict]:
    ''''''
    try:
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, list):
                return data
            else:
                return []
    except FileNotFoundError:
        print("file not found")
        return []
    except json.JSONDecodeError:
        print("Wrong format")
        return []


filename = "data/operations.json"
nwe_list = transaction(filename)
#print(nwe_list)
