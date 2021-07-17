import os
import json
from typing import Any


DEFAULT_PATH = "C:\\Users\\madpe\\moves_json\\json"


class MovesData():

    BASE_DIR: str = DEFAULT_PATH

    def __init__(self, path: str = None) -> None:
        if path is not None and os.path.exists(path):
            self.BASE_DIR = path
        print('initialized')

    def __call__(self, url: str) -> dict:
        print('called')
        return {}


if __name__ == '__main__':
    user_request = "daily activities"
    requested_path = os.path.join(DEFAULT_PATH, os.sep.join(user_request.split()))
    print(requested_path)
    print(os.listdir(requested_path)[:5])