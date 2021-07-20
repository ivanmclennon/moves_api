import os
import json


DEFAULT_DIR = "C:\\Users\\madpe\\moves_json\\json"


class MovesData():

    BASE_DIR: str = DEFAULT_DIR

    def __init__(self, base_dir: str = None) -> None:
        if base_dir is not None and os.path.exists(base_dir):
            self.BASE_DIR = base_dir

    async def get_json(self, date: str) -> dict:
        filename = f"activities_{date}.json"
        path = os.path.join(self.BASE_DIR, os.sep.join(
            ['daily', 'activities', filename]))
        if os.path.exists(path):
            with open(path, 'r', encoding='utf-8') as f:
                json_response = json.load(f)
            return json_response[0]
        return {}


if __name__ == '__main__':
    print('file_engine.py executed')
